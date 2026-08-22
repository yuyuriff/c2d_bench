from fastmcp import FastMCP

from pathlib import Path
import json
import os

DATA_DIR = Path(os.getenv("MCP_DATA_DIR", "/workspace/mcp-data"))

mcp = FastMCP("c2d-context")

def resolve_rel_path(repo_dir: Path, rel_path: str) -> Path:
    repo_path = (repo_dir / rel_path).resolve()
    root = repo_dir.resolve()

    if repo_path != root and root not in repo_path.parents:
        raise RuntimeError("Relative path not in folder")

    return repo_path

def resolve_data_path(rel_path: str) -> Path:
    resolve_rel_path(DATA_DIR, rel_path)

@mcp.tool
def list_mcp_files() -> str:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    files = [
        str(path.relative_to(DATA_DIR)).replace("\\", "/")
        for path in DATA_DIR.rglob("*")
        if path.is_file()
    ]

    if not files:
        return "<No MCP files found>"

    return "\n".join(files)

@mcp.tool
def read_mcp_file(path: str, max_chars = 15_000) -> str:
    res_path = resolve_data_path(path)

    if not res_path.is_file():
        return f"Error! path is not a file: {res_path}"

    text = res_path.read_text(encoding="utf-8", errors="ignore")
    if len(text) > max_chars:
        text = text[:max_chars] + "\n<...>"

    return text

def find_snippet(text: str, query: str) -> str:
    position = text.lower().find(query.lower())

    start = max(0, position - 500)
    end = min(len(text), position + len(query) + 500)
    snippet = text[start:end]

    return snippet

def search_in_repo(repo_dir: Path, query: str, max_results: int = 20, max_chars: int = 15_000) -> str:
    if not query:
        return "<No matches>"

    query_lower = query.lower()
    matches = []

    for path in repo_dir.rglob("*"):
        if not path.is_file():
            continue

        rel_path = str(path.relative_to(repo_dir)).replace("\\", "/")
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        snippet = ""
        if query_lower in text.lower():
            snippet = find_snippet(text, query)
        elif query_lower in rel_path.lower():
            snippet = text[:1_000]
        else:
            continue

        matches.append(f"{rel_path}: {snippet}")

        if len(matches) >= max_results:
            break

    joined = "\n".join(matches)
    if len(joined) > max_chars:
        joined = joined[:max_chars] + "\n<...>"

    return joined or "<No matches>"

@mcp.tool
def search_mcp(query: str, max_results: int = 20, max_chars: int = 15_000) -> str:
    return search_in_repo(DATA_DIR, query, max_results, max_chars)


def project_graph_name(path: Path) -> str:
    stem = path.stem
    prefix = "documentation_graph_"
    if stem.startswith(prefix):
        return stem[len(prefix):]
    return stem

def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception as e:
        raise RuntimeError(f"Invalid json file: {e}")

@mcp.tool
def list_documentation_graphs() -> str:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    graphs = []

    for path in sorted(DATA_DIR.rglob("documentation_graph_*.json")):
        rel_path = str(path.relative_to(DATA_DIR)).replace("\\", "/")
        try:
            graph = load_json(path)
        except Exception as e:
            continue

        graphs.append({
            "project": project_graph_name(path),
            "path": rel_path,
            "name": graph.get("name"),
            "statistics": graph.get("statistics", {}),
        })

    return json.dumps(graphs, ensure_ascii=False) if graphs else "<No documentation graphs>"

def find_documentation_graph(project: str | None = None, path: str | None = None) -> Path:
    if path:
        res_path = resolve_data_path(path)

        if not res_path.is_file():
            raise RuntimeError(f"Documentation graph path is not a file: {path}")
        return res_path

    if not project:
        raise RuntimeError("Either project or path is required")

    doc_graphs = sorted(DATA_DIR.rglob(f"documentation_graph_{project}.json"))

    if not doc_graphs:
        raise FileNotFoundError(f"No documentation graph for project: {project}")

    return doc_graphs[0]


def get_node(node: dict) -> dict:
    node_info = {
        "node_id": node.get("node_id"),
        "node_type": node.get("node_type"),
        "title": node.get("title", ""),
        "tags": node.get("tags", []),
        "url": node.get("url"),
        "score": node.get("score"),
        "depth": node.get("depth"),
        "parent_id": node.get("parent_id"),
        "parent_type": node.get("parent_type"),
        "code_snippets_count": node.get("code_snippets_count"),
        "key_fragments": node.get("key_fragments", []),
    }

    code_snippets = []
    for snippet in node.get("code_snippets", []):
        code_snippets.append({
            "language": snippet.get("language"),
            "source": snippet.get("source"),
            "snippet_index": snippet.get("snippet_index"),
            "code": snippet.get("code", "")
        })
    if code_snippets:
        node_info["code_snippets"] = code_snippets

    return {key: value for key, value in node_info.items()}


@mcp.tool
def read_documentation_graph(project: str | None = None, path: str | None = None, max_nodes: int = 100) -> str:
    try:
        graph_path = find_documentation_graph(project, path)
        graph = load_json(graph_path)
    except Exception as e:
        return "Error! Invalid graph path"

    nodes = graph.get("nodes", {})
    selected_ids = sorted(
        nodes,
        key=lambda node_id: (
            nodes[node_id].get("depth"),
            -int(nodes[node_id].get("score")),
            node_id,
        )
    )[:max_nodes]
    
    selected_nodes = {
        node_id: get_node(nodes[node_id])
        for node_id in selected_ids
    }
    selected_id_set = set(selected_ids)
    selected_edges = [
        edge for edge in graph.get("edges", [])
        if edge.get("from") in selected_id_set and edge.get("to") in selected_id_set
    ]

    output_graph = {
        "name": graph.get("name"),
        "statistics": graph.get("statistics", {}),
        "nodes_returned": len(selected_nodes),
        "total_nodes": len(nodes),
        "nodes": selected_nodes,
        "edges": selected_edges,
    }

    return json.dumps(output_graph, ensure_ascii=False)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=9000)

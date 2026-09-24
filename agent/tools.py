import os
from pathlib import Path
import subprocess

from .mcp import call_mcp_tool

SKIP_DIRS = {
    ".git",
    "node_modules",
    "target",
    "build",
    "dist",
    "docs",
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_repo_tree",
            "description": "Return repository tree for the current project",
            "parameters": {
                "type": "object",
                "properties": {},
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_repo_file",
            "description": "Read a file from the repo by relative path",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Relative path inside repository"
                    }
                },
                "required": ["path"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_text",
            "description": "Search for query text in repository",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Text to search"
                    }
                },
                "required": ["query"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_mcp_files",
            "description": "List context files on the MCP server",
            "parameters": {
                "type": "object",
                "properties": {},
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_mcp_file",
            "description": "Read a context file from the MCP server by relative path",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Relative path of a context file"
                    }
                },
                "required": ["path"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_mcp",
            "description": "Search context on the MCP server",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Text to search for"
                    }
                },
                "required": ["query"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_documentation_graphs",
            "description": "List documentation knowledge graphs on the MCP server",
            "parameters": {
                "type": "object",
                "properties": {},
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_documentation_graph",
            "description": "Read a documentation knowledge graph in JSON format",
            "parameters": {
                "type": "object",
                "properties": {
                    "project": {
                        "type": "string",
                        "description": "Project name"
                    },
                    "path": {
                        "type": "string",
                        "description": "Relative path of a graph file"
                    },
                },
                "required": ["path"],
            }
        }
    },
]

def read_file(path: Path, max_chars: int = 15_000) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return f"Error reading file: {e}"

    if len(text) > max_chars:
        text = text[:max_chars] + "\n<...>"
    return text

def resolve_rel_path(repo_dir: Path, rel_path: str) -> Path:
    repo_path = (repo_dir / rel_path).resolve()
    root = repo_dir.resolve()

    if repo_path != root and root not in repo_path.parents:
        raise RuntimeError("Relative path not in repo folder")

    return repo_path

def walk_repo(repo_dir: Path):
    for root, dirs, files in os.walk(repo_dir):
        dirs[:] = [
            d
            for d in dirs
            if d not in SKIP_DIRS
        ]

        root_path = Path(root)

        for d in dirs:
            yield root_path / d

        for f in files:
            yield root_path / f


def walk_files(repo_dir: Path):
    for root, dirs, files in os.walk(repo_dir):
        dirs[:] = [
            d
            for d in dirs
            if d not in SKIP_DIRS
        ]

        root_path = Path(root)

        for f in files:
            yield root_path / f


def get_repo_tree(repo_dir: Path, max_nodes: int = 100) -> str:
    nodes = []

    for path in walk_repo(repo_dir):
        rel_path = str(path.relative_to(repo_dir)).replace("\\", "/")
        rel_path += "/" if path.is_dir() else ""

        nodes.append(rel_path)

        if len(nodes) >= max_nodes:
            break

    return "\n".join(sorted(nodes))


def read_repo_file(repo_dir: Path, rel_path: str, max_chars: int = 15_000) -> str:
    path = resolve_rel_path(repo_dir, rel_path)

    if not path.exists():
        return f"File does not exist: {rel_path}"
    if not path.is_file():
        return f"Path is not a file: {rel_path}"

    return read_file(path, max_chars)


def find_snippet(text: str, query: str) -> str:
    position = text.lower().find(query.lower())

    start = max(0, position - 500)
    end = min(len(text), position + len(query) + 500)
    snippet = text[start:end]

    return snippet

def limit_matches(matches: str, max_results: int = 20, max_per_file: int = 3) -> str:
    counts = {}
    selected = []

    snippets = matches.split("\n--\n")

    for snippet in snippets:
        lines = snippet.splitlines()
        file_path = ""
        path_count = 0

        for line in lines:
            parts = line.split(":", 2)
            if len(parts) == 3 and parts[1].isdigit():
                file_path = parts[0]
                path_count = counts.get(file_path, 0)
                break

        if not file_path:
            continue
        
        if path_count >= max_per_file:
            continue

        selected.append("\n".join(lines))
        counts[file_path] = path_count + 1

        if len(selected) >= max_results:
            break

    return "\n\n".join(selected)


def search_in_repo(repo_dir: Path, query: str, max_results: int = 30, max_matches_per_file: int = 3, max_chars: int = 15_000) -> str:
    if not query:
        return "<No matches>"

    try:
        result = subprocess.run(
            [
                "git",
                "--no-pager",
                "-C",
                str(repo_dir),
                "grep",
                "-n",
                "-i",
                "-B",
                "2",
                "-A",
                "2",
                query,
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except Exception as e:
        return f"<Search error: {e}>"

    if result.returncode > 1:
        return f"<Search error: {result.stderr.strip()}>"

    lines = result.stdout.splitlines()[:max_results]

    if not lines:
        return "<No matches>"
    
    output = limit_matches(result.stdout)

    if len(output) > max_chars:
        output = output[:max_chars] + "\n<...>"

    return output


# tool handling

def handle_get_repo_tree(repo_dir: Path, arguments: dict, max_chars_per_file: int) -> str:
    return get_repo_tree(repo_dir)


def handle_read_repo_file(repo_dir: Path, arguments: dict, max_chars_per_file: int) -> str:
    return read_repo_file(
        repo_dir,
        arguments.get("path", ""),
        max_chars=max_chars_per_file,
    )


def handle_search_text(repo_dir: Path, arguments: dict, max_chars_per_file: int) -> str:
    return search_in_repo(
        repo_dir=repo_dir,
        query=arguments.get("query", ""),
        max_chars=max_chars_per_file,
    )


def handle_list_mcp_files(repo_dir: Path, arguments: dict, max_chars_per_file: int) -> str:
    return call_mcp_tool(
        "list_mcp_files",
        {},
    )


def handle_read_mcp_file(repo_dir: Path, arguments: dict, max_chars_per_file: int) -> str:
    return call_mcp_tool(
        "read_mcp_file",
        {
            "path": arguments.get("path", ""),
        },
    )


def handle_search_mcp(repo_dir: Path, arguments: dict, max_chars_per_file: int) -> str:
    return call_mcp_tool(
        "search_mcp",
        {
            "query": arguments.get("query", ""),
        },
    )


def handle_list_documentation_graphs(repo_dir: Path, arguments: dict, max_chars_per_file: int) -> str:
    return call_mcp_tool(
        "list_documentation_graphs",
        {},
    )


def handle_read_documentation_graph(repo_dir: Path, arguments: dict, max_chars_per_file: int) -> str:
    return call_mcp_tool(
        "read_documentation_graph",
        {
            "project": arguments.get("project", ""),
            "path": arguments.get("path", ""),
        },
    )


TOOL_HANDLERS = {
    "get_repo_tree": handle_get_repo_tree,
    "read_repo_file": handle_read_repo_file,
    "search_text": handle_search_text,
    "list_mcp_files": handle_list_mcp_files,
    "read_mcp_file": handle_read_mcp_file,
    "search_mcp": handle_search_mcp,
    "list_documentation_graphs": handle_list_documentation_graphs,
    "read_documentation_graph": handle_read_documentation_graph,
}


def execute_tool(repo_dir: Path, tool_name: str, arguments: dict, max_chars_per_file: int = 15_000) -> str:
    handler = TOOL_HANDLERS.get(tool_name)

    if handler is None:
        return f"Unavailable tool: {tool_name}"

    return handler(
        repo_dir,
        arguments,
        max_chars_per_file,
    )
    
from fastmcp import Client

from pathlib import Path
import os
import asyncio

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

def get_repo_tree(repo_dir: Path, max_nodes: int = 500) -> str:
    nodes = []

    for path in repo_dir.rglob("*"):
        rel_path = str(path.relative_to(repo_dir)).replace("\\", "/")
        rel_path += "/" if path.is_dir() else ""

        nodes.append(rel_path)

    nodes = sorted(nodes)[:max_nodes]
    return "\n".join(nodes)


def read_repo_file(repo_dir: Path, rel_path: str, max_chars: int) -> str:
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

def get_mcp_url() -> str:
    return os.getenv("MCP_SERVER_URL", "http://mcp-server:9000/mcp/")

async def call_mcp_client(tool_name: str, arguments: dict) -> str:
    client = Client(get_mcp_url())
    async with client:
        result = await client.call_tool(tool_name, arguments, timeout=60)
    return result

def call_mcp_tool(tool_name: str, arguments: dict) -> str:
    try:
        return asyncio.run(call_mcp_client(tool_name, arguments))
    except Exception as e:
        return f"Error calling MCP server: {e}"

def execute_tool(repo_dir: Path, tool_name: str, arguments: dict, max_chars_per_file: int = 15_000) -> str:
    if tool_name == "get_repo_tree":
        return get_repo_tree(repo_dir)

    if tool_name == "read_repo_file":
        path = arguments.get("path", "")
        return read_repo_file(repo_dir, path, max_chars=max_chars_per_file)

    if tool_name == "search_text":
        query = arguments.get("query", "")
        return search_in_repo(repo_dir, query)

    if tool_name == "list_mcp_files":
        return call_mcp_tool("list_mcp_files", {})

    if tool_name == "read_mcp_file":
        path = arguments.get("path", "")
        return call_mcp_tool("read_mcp_file", {"path": path})

    if tool_name == "search_mcp":
        query = arguments.get("query", "")
        return call_mcp_tool("search_mcp", {"query": query})

    if tool_name == "list_documentation_graphs":
        return call_mcp_tool("list_documentation_graphs", {})

    if tool_name == "read_documentation_graph":
        return call_mcp_tool("read_documentation_graph", {
            "project": arguments.get("project", ""),
            "path": arguments.get("path", ""),
        })

    return f"Unavailable tool: {tool_name}"
    
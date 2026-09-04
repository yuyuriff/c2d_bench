from fastmcp import Client

import asyncio
import os

def get_mcp_url() -> str:
    return os.getenv("MCP_SERVER_URL", "http://mcp-server:9000/mcp/")

def mcp_result_to_str(result) -> str:
    if result.is_error:
        return f"MCP tool error: {result}"

    content_parts = []
    for item in result.content:
        if hasattr(item, "text"):
            content_parts.append(item.text)
        else:
            content_parts.append(str(item))

    return "\n".join(content_parts)

async def call_mcp_client(tool_name: str, arguments: dict) -> str:
    client = Client(get_mcp_url())
    async with client:
        result = await client.call_tool(tool_name, arguments, timeout=60)
    return mcp_result_to_str(result)

def call_mcp_tool(tool_name: str, arguments: dict) -> str:
    try:
        return asyncio.run(call_mcp_client(tool_name, arguments))
    except Exception as e:
        return f"Error calling MCP server: {e}"

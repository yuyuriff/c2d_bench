import pytest
from pathlib import Path
from types import SimpleNamespace

import agent.mcp as mcp

def test_get_mcp_url_from_env(monkeypatch):
    monkeypatch.setenv(
        "MCP_SERVER_URL",
        "http://test-server:6767/mcp/",
    )

    result = mcp.get_mcp_url()

    assert result == "http://test-server:6767/mcp/"

def test_get_mcp_url_default(monkeypatch):
    monkeypatch.delenv("MCP_SERVER_URL", raising=False)

    result = mcp.get_mcp_url()

    assert result == "http://mcp-server:9000/mcp/"

def test_mcp_result_to_str():
    result = SimpleNamespace(
        is_error=False,
        content=[
            SimpleNamespace(text="six"),
            SimpleNamespace(text="seven"),
        ],
    )

    output = mcp.mcp_result_to_str(result)

    assert output == "six\nseven"


def test_mcp_result_to_str_content():
    result = SimpleNamespace(
        is_error=False,
        content=[
            123,
        ],
    )

    output = mcp.mcp_result_to_str(result)

    assert output == "123"


def test_mcp_result_to_str_error():
    result = SimpleNamespace(
        is_error=True,
        content=[],
    )

    output = mcp.mcp_result_to_str(result)

    assert output.startswith("MCP tool error:")

def test_call_mcp_tool(monkeypatch):
    async def mock_call_mcp_client(tool_name, arguments):
        assert tool_name == "search_mcp"
        assert arguments == {"query": "hello"}

        return "MCP result"

    monkeypatch.setattr(
        mcp,
        "call_mcp_client",
        mock_call_mcp_client,
    )

    result = mcp.call_mcp_tool("search_mcp", {"query": "hello"})

    assert result == "MCP result"

def test_call_mcp_tool_handles_exception(monkeypatch):
    async def mock_call_mcp_client(tool_name, arguments):
        raise RuntimeError("aaaa")

    monkeypatch.setattr(
        mcp,
        "call_mcp_client",
        mock_call_mcp_client,
    )

    result = mcp.call_mcp_tool("search_mcp", {})

    assert result == "Error calling MCP server: aaaa"
    
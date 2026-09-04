from pathlib import Path
from types import SimpleNamespace

import pytest
from unittest.mock import MagicMock

import agent.agent as agent_module

def test_get_default_prompt(tmp_path):
    prompts_dir = tmp_path / "prompts"
    prompts_dir.mkdir()

    prompt_file = prompts_dir / "default.md"
    prompt_file.write_text("Test prompt", encoding="utf-8")

    result = agent_module.get_default_prompt(tmp_path)

    assert result == "Test prompt"


def test_get_client(monkeypatch):
    monkeypatch.setenv("TEST_API_KEY", "secret")

    created = {}

    def mock_openai(**kwargs):
        created.update(kwargs)
        return "fake-client"

    monkeypatch.setattr(agent_module, "OpenAI", mock_openai)

    config = {
        "api_key_env": "TEST_API_KEY",
        "base_url": "http://example.com",
    }

    result = agent_module.get_client(config, model_timeout=120)

    assert result == "fake-client"
    assert created == {
        "api_key": "secret",
        "base_url": "http://example.com",
        "timeout": 120,
    }


def test_get_client_api_key_missing(monkeypatch):
    monkeypatch.delenv("TEST_API_KEY", raising=False)

    config = {
        "api_key_env": "TEST_API_KEY",
        "base_url": "http://example.com",
    }

    with pytest.raises(RuntimeError, match="TEST_API_KEY is not set"):
        agent_module.get_client(config, 120)


def test_call_llm_call_model(monkeypatch, tmp_path):
    client = MagicMock()

    message = MagicMock()
    message.content = "Final answer"
    message.tool_calls = None

    response = MagicMock()
    response.choices[0].message = message

    client.chat.completions.create.return_value = response

    monkeypatch.setattr(
        agent_module,
        "get_agent_limits",
        lambda config: {
            "model_timeout": 120,
            "max_chars_per_file": 15000,
            "max_turns": 5,
            "max_tool_calls": 3,
        },
    )

    monkeypatch.setattr(
        agent_module,
        "get_client",
        lambda config, timeout: client,
    )

    result, stats = agent_module.call_llm(
        tmp_path,
        {"model_name": "llm-model"},
        prompt="My prompt",
    )

    assert result == "Final answer"

    client.chat.completions.create.assert_called_once()

    kwargs = client.chat.completions.create.call_args.kwargs

    assert kwargs["model"] == "llm-model"
    assert kwargs["tool_choice"] == "auto"
    assert kwargs["temperature"] == 0.1


def test_call_llm_execute_tool(monkeypatch, tmp_path):
    client = MagicMock()

    tool_call = MagicMock()
    tool_call.id = "call-1"
    tool_call.function.name = "read_repo_file"
    tool_call.function.arguments = '{"path": "README.md"}'

    first_message = MagicMock()
    first_message.content = None
    first_message.tool_calls = [tool_call]
    first_message.model_dump.return_value = {
        "role": "assistant",
        "tool_calls": [],
    }

    first_response = MagicMock()
    first_response.choices[0].message = first_message

    second_message = MagicMock()
    second_message.content = "Final docs"
    second_message.tool_calls = None

    second_response = MagicMock()
    second_response.choices[0].message = second_message

    client.chat.completions.create.side_effect = [
        first_response,
        second_response,
    ]

    monkeypatch.setattr(
        agent_module,
        "get_agent_limits",
        lambda config: {
            "model_timeout": 120,
            "max_chars_per_file": 1234,
            "max_turns": 5,
            "max_tool_calls": 3,
        },
    )

    monkeypatch.setattr(
        agent_module,
        "get_client",
        lambda config, timeout: client,
    )

    execute_tool = MagicMock(return_value="README contents")
    monkeypatch.setattr(
        agent_module,
        "execute_tool",
        execute_tool,
    )

    result, stats = agent_module.call_llm(
        tmp_path,
        {"model_name": "llm-model"},
        prompt="Write docs",
        instance_id="instance-1",
    )

    assert result == "Final docs"

    execute_tool.assert_called_once_with(
        repo_dir=tmp_path,
        tool_name="read_repo_file",
        arguments={"path": "README.md"},
        max_chars_per_file=1234,
    )

    assert stats["tool_calls_used"] == 1
    assert stats["tool_calls_failed"] == 0
    assert stats["tool_calls_stats"]["read_repo_file"] == 1


def test_call_llm_tool_error(monkeypatch, tmp_path):
    client = MagicMock()

    tool_call = MagicMock()
    tool_call.id = "call-1"
    tool_call.function.name = "search_text"
    tool_call.function.arguments = '{"query": "hello"}'

    first_message = MagicMock()
    first_message.tool_calls = [tool_call]
    first_message.model_dump.return_value = {
        "role": "assistant",
        "tool_calls": [],
    }

    second_message = MagicMock()
    second_message.tool_calls = None
    second_message.content = "answer"

    first_response = MagicMock()
    first_response.choices[0].message = first_message

    second_response = MagicMock()
    second_response.choices[0].message = second_message

    client.chat.completions.create.side_effect = [
        first_response,
        second_response,
    ]

    monkeypatch.setattr(
        agent_module,
        "get_agent_limits",
        lambda config: {
            "model_timeout": 120,
            "max_chars_per_file": 15000,
            "max_turns": 5,
            "max_tool_calls": 3,
        },
    )

    monkeypatch.setattr(
        agent_module,
        "get_client",
        lambda config, timeout: client,
    )

    def broken_tool(**kwargs):
        raise RuntimeError("aaaa")

    monkeypatch.setattr(
        agent_module,
        "execute_tool",
        broken_tool,
    )

    result, stats = agent_module.call_llm(
        tmp_path,
        {"model_name": "llm-model"},
        prompt="test",
    )

    assert result == "answer"
    assert stats["tool_calls_used"] == 1
    assert stats["tool_calls_failed"] == 1
    assert stats["tool_calls"][0]["status"] == "error"


def test_call_llm_invalid_tool_args(monkeypatch, tmp_path):
    client = MagicMock()

    tool_call = MagicMock()
    tool_call.id = "call-1"
    tool_call.function.name = "search_text"
    tool_call.function.arguments = "{invalid-input"

    first_message = MagicMock()
    first_message.tool_calls = [tool_call]
    first_message.model_dump.return_value = {
        "role": "assistant",
        "tool_calls": [],
    }

    second_message = MagicMock()
    second_message.tool_calls = None
    second_message.content = "done"

    first_response = MagicMock()
    first_response.choices[0].message = first_message

    second_response = MagicMock()
    second_response.choices[0].message = second_message

    client.chat.completions.create.side_effect = [
        first_response,
        second_response,
    ]

    monkeypatch.setattr(
        agent_module,
        "get_agent_limits",
        lambda config: {
            "model_timeout": 120,
            "max_chars_per_file": 15000,
            "max_turns": 5,
            "max_tool_calls": 3,
        },
    )

    monkeypatch.setattr(
        agent_module,
        "get_client",
        lambda config, timeout: client,
    )

    execute_tool = MagicMock(return_value="result")
    monkeypatch.setattr(
        agent_module,
        "execute_tool",
        execute_tool,
    )

    agent_module.call_llm(
        tmp_path,
        {"model_name": "llm-model"},
        prompt="test",
    )

    assert execute_tool.call_args.kwargs["arguments"] == {}


def test_call_llm_execute_tool(monkeypatch, tmp_path):
    client = MagicMock()

    tool_call = MagicMock()
    tool_call.id = "call-1"
    tool_call.function.name = "read_repo_file"
    tool_call.function.arguments = '{"path": "README.md"}'

    first_message = MagicMock()
    first_message.content = None
    first_message.tool_calls = [tool_call]
    first_message.model_dump.return_value = {
        "role": "assistant",
        "tool_calls": [],
    }

    first_response = MagicMock()
    first_response.choices[0].message = first_message

    second_message = MagicMock()
    second_message.content = "Final docs"
    second_message.tool_calls = None

    second_response = MagicMock()
    second_response.choices[0].message = second_message

    client.chat.completions.create.side_effect = [
        first_response,
        first_response,
        second_response,
    ]

    monkeypatch.setattr(
        agent_module,
        "get_agent_limits",
        lambda config: {
            "model_timeout": 120,
            "max_chars_per_file": 1234,
            "max_turns": 5,
            "max_tool_calls": 1,
        },
    )

    monkeypatch.setattr(
        agent_module,
        "get_client",
        lambda config, timeout: client,
    )

    execute_tool = MagicMock(return_value="README contents")
    monkeypatch.setattr(
        agent_module,
        "execute_tool",
        execute_tool,
    )

    result, stats = agent_module.call_llm(
        tmp_path,
        {"model_name": "llm-model"},
        prompt="Write docs",
        instance_id="instance-1",
    )

    assert result == "Final docs"

    assert execute_tool.call_count == 1
    assert stats["tool_calls_failed"] == 1
    assert stats["stop_reason"] == "Reached max tool calls (1)"
    
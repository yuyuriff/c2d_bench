import pytest
import json

import agent.config as config

def test_set_limits_merges_dicts():
    default_limits = {
        "max_turns": 50,
        "max_tool_calls": 30,
    }

    model_limits = {
        "max_turns": 10,
    }

    result = config.set_limits(default_limits, model_limits)

    assert result == {
        "max_turns": 10,
        "max_tool_calls": 30,
    }


def test_load_models_config(tmp_path):
    test_config = {
        "test-model": {
            "model_name": "fake",
            "base_url": "http://api-test.com"
        }
    }

    config_file = tmp_path / "models.json"
    config_file.write_text(json.dumps(test_config),encoding="utf-8")

    result = config.load_models_config(tmp_path)

    assert result == test_config
    

def test_get_model_config(monkeypatch):
    monkeypatch.setattr(
        config,
        "load_models_config",
        lambda: {
            "test-model": {
                "model_name": "fake",
                "base_url": "http://api-test.com"
            }
        }
    )

    result = config.get_model_config("test-model")

    assert result["model_name"] == "fake"
    assert result["alias"] == "test-model"


def test_unavailable_model(monkeypatch):
    monkeypatch.setattr(
        config,
        "load_models_config",
        lambda: {
            "test-model": {
                "model_name": "fake",
                "base_url": "http://api-test.com"
            }
        }
    )

    with pytest.raises(RuntimeError, match="Unknown model alias"):
        config.get_model_config("gpt-5")


def test_load_limits_config(tmp_path):
    test_config = {
        "agent": {
            "max_turns": 50,
            "max_tool_calls": 30,
            "model_timeout": 120,
        },
        "models": {
            "deepseek-chat": {
                "max_turns": 10,
                "max_tool_calls": 10,
            }
        },
    }

    config_file = tmp_path / "limits.json"
    config_file.write_text(json.dumps(test_config),encoding="utf-8")

    result = config.load_limits_config(tmp_path)

    assert result == test_config


def test_get_agent_limits_model(monkeypatch):
    monkeypatch.setattr(
        config,
        "load_limits_config",
        lambda: {
            "agent": {
                "max_turns": 50,
                "max_tool_calls": 30,
                "model_timeout": 120,
            },
            "models": {
                "deepseek-chat": {
                    "max_turns": 10,
                    "max_tool_calls": 10,
                }
            },
        },
    )

    model_config = {
        "alias": "deepseek-chat",
    }

    result = config.get_agent_limits(model_config)

    assert result["max_turns"] == 10
    assert result["max_tool_calls"] == 10
    assert result["model_timeout"] == 120

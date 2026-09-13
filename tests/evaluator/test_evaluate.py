import pytest
import os
from unittest.mock import MagicMock

import evaluator.evaluate as evaluate_module

def test_get_judge_config(monkeypatch):
    monkeypatch.setenv("JUDGE_API_KEY", "test-key")
    monkeypatch.setenv("JUDGE_BASE_URL", "http://judge.com")
    monkeypatch.setenv("JUDGE_MODEL", "judge-model")

    result = evaluate_module.get_judge_config()

    assert result == {
        "api_key": "test-key",
        "base_url": "http://judge.com",
        "model": "judge-model",
    }

    assert os.environ["OPENAI_API_KEY"] == "test-key"
    assert os.environ["OPENAI_BASE_URL"] == "http://judge.com"


def test_evaluate_missing_api_key(monkeypatch):
    monkeypatch.delenv("JUDGE_API_KEY", raising=False)
    monkeypatch.setenv("JUDGE_BASE_URL", "http://judge.com")
    monkeypatch.setenv("JUDGE_MODEL", "judge-model")

    with pytest.raises(RuntimeError, match="JUDGE_API_KEY is not set"):
        evaluate_module.evaluate("instance-1", "gold", "generated")


def test_evaluate_missing_base_url(monkeypatch):
    monkeypatch.setenv("JUDGE_API_KEY", "key")
    monkeypatch.delenv("JUDGE_BASE_URL", raising=False)
    monkeypatch.setenv("JUDGE_MODEL", "judge-model")

    with pytest.raises(RuntimeError, match="JUDGE_BASE_URL is not set"):
        evaluate_module.evaluate("instance-1", "gold", "generated")


def test_evaluate_missing_model(monkeypatch):
    monkeypatch.setenv("JUDGE_API_KEY", "key")
    monkeypatch.setenv("JUDGE_BASE_URL", "http://judge.com")
    monkeypatch.delenv("JUDGE_MODEL", raising=False)

    with pytest.raises(RuntimeError, match="JUDGE_MODEL is not set"):
        evaluate_module.evaluate("instance-1", "gold", "generated")


def test_build_metrics(monkeypatch):
    created = []

    def mock_geval(**kwargs):
        created.append(kwargs)
        return MagicMock(name=kwargs["name"])

    monkeypatch.setattr(
        evaluate_module,
        "GEval",
        mock_geval,
    )

    result = evaluate_module.build_metrics("judge-model")

    assert len(result) == 3
    assert [item["name"] for item in created] == [
        "alignment_to_gold",
        "coverage_of_gold",
        "structure_and_readability",
    ]

    assert all(
        item["model"] == "judge-model"
        for item in created
    )


def test_evaluate_none_score(monkeypatch):
    monkeypatch.setenv("JUDGE_API_KEY", "key")
    monkeypatch.setenv("JUDGE_BASE_URL", "http://judge.com")
    monkeypatch.setenv("JUDGE_MODEL", "judge-model")

    metric = MagicMock()
    metric.name = "metric"
    metric.score = None
    metric.reason = None

    monkeypatch.setattr(
        evaluate_module,
        "build_metrics",
        lambda model: [metric],
    )

    result = evaluate_module.evaluate("instance-1", "gold", "generated")

    assert result["avg_score"] == 0.0
    assert result["metrics"]["metric"] == {
        "score": 0.0,
        "reason": "",
    }


def test_evaluate_no_metrics(monkeypatch):
    monkeypatch.setenv("JUDGE_API_KEY", "key")
    monkeypatch.setenv("JUDGE_BASE_URL", "http://judge.com")
    monkeypatch.setenv("JUDGE_MODEL", "judge-model")

    monkeypatch.setattr(
        evaluate_module,
        "build_metrics",
        lambda model: [],
    )

    result = evaluate_module.evaluate("instance-1", "gold", "generated")

    assert result == {
        "avg_score": 0.0,
        "metrics": {},
    }


def test_evaluate(monkeypatch):
    monkeypatch.setenv("JUDGE_API_KEY", "key")
    monkeypatch.setenv("JUDGE_BASE_URL", "http://judge.local")
    monkeypatch.setenv("JUDGE_MODEL", "judge-model")

    metric1 = MagicMock()
    metric1.name = "metric1"
    metric1.score = 0.8
    metric1.reason = "Good"

    metric2 = MagicMock()
    metric2.name = "metric2"
    metric2.score = 0.6
    metric2.reason = "Okay"

    def measure1(test_case):
        pass

    def measure2(test_case):
        pass

    metric1.measure = measure1
    metric2.measure = measure2

    monkeypatch.setattr(
        evaluate_module,
        "build_metrics",
        lambda model: [metric1, metric2],
    )

    result = evaluate_module.evaluate("instance-1", "gold", "generated")

    assert result == {
        "avg_score": 0.7,
        "metrics": {
            "metric1": {
                "score": 0.8,
                "reason": "Good",
            },
            "metric2": {
                "score": 0.6,
                "reason": "Okay",
            },
        },
    }
import pytest
import json
from unittest.mock import MagicMock

import evaluator.main as judge

def test_load_jsonl(tmp_path):
    datasets = '{"instance_id":"bookkeeper","repo_url":"https://github.com/apache/bookkeeper.git","gold_md_path":"/workspace/benchmark/gold/bookkeeper.md"}\n{"instance_id":"rocketmq","repo_url":"https://github.com/apache/rocketmq.git","gold_md_path":"/workspace/benchmark/gold/rocketmq.md"}'

    dataset_file = tmp_path / "run_001.jsonl"
    dataset_file.write_text(datasets, encoding="utf-8")

    result = judge.load_jsonl(dataset_file)

    assert result == [{"instance_id":"bookkeeper","repo_url":"https://github.com/apache/bookkeeper.git","gold_md_path":"/workspace/benchmark/gold/bookkeeper.md"},
                      {"instance_id":"rocketmq","repo_url":"https://github.com/apache/rocketmq.git","gold_md_path":"/workspace/benchmark/gold/rocketmq.md"}]


def test_load_jsonl_missing_file(tmp_path):
    path = tmp_path / "run_002.jsonl"

    result = judge.load_jsonl(path)

    assert result == []

def test_get_gold_dict():
    dataset = [{"instance_id":"bookkeeper","repo_url":"https://github.com/apache/bookkeeper.git","gold_md_path":"/workspace/benchmark/gold/bookkeeper.md"},
                      {"instance_id":"rocketmq","repo_url":"https://github.com/apache/rocketmq.git","gold_md_path":"/workspace/benchmark/gold/rocketmq.md"}]

    result = judge.get_gold_dict(dataset)

    assert result["bookkeeper"] == "/workspace/benchmark/gold/bookkeeper.md"
    assert result["rocketmq"] == "/workspace/benchmark/gold/rocketmq.md"


def test_get_gold_dict_without_instance_id():
    dataset = [
        {
            "instance_id": "one",
            "gold_md_path": "one.md",
        },
        {
            "gold_md_path": "unknown.md",
        },
    ]

    result = judge.get_gold_dict(dataset)

    assert result == {
        "one": "one.md",
    }


def test_get_gold_dict_missing_gold_path():
    dataset = [
        {
            "instance_id": "one",
        }
    ]

    result = judge.get_gold_dict(dataset)

    assert result == {}


def test_main_success(monkeypatch, tmp_path):
    generated_file = tmp_path / "generated.md"
    generated_file.write_text(
        "Generated documentation",
        encoding="utf-8",
    )

    gold_file = tmp_path / "gold.md"
    gold_file.write_text(
        "Gold documentation",
        encoding="utf-8",
    )

    report_dir = tmp_path / "reports"
    report_file = report_dir / "report.json"

    monkeypatch.setattr(
        judge,
        "REPORT_DIR",
        str(report_dir),
    )
    monkeypatch.setattr(
        judge,
        "REPORT_FILE",
        str(report_file),
    )

    monkeypatch.setattr(
        judge,
        "DATASET_FILE",
        "dataset.jsonl",
    )
    monkeypatch.setattr(
        judge,
        "RESULTS_FILE",
        "results.jsonl",
    )

    def mock_load_jsonl(path):
        if path == "dataset.jsonl":
            return [
                {
                    "instance_id": "case-1",
                    "gold_md_path": str(gold_file),
                }
            ]

        return [
            {
                "instance_id": "case-1",
                "status": "success",
                "output_md_path": str(generated_file),
            }
        ]

    monkeypatch.setattr(
        judge,
        "load_jsonl",
        mock_load_jsonl,
    )

    evaluate_mock = MagicMock(
        return_value={
            "avg_score": 0.8,
            "metrics": {},
        }
    )

    monkeypatch.setattr(
        judge,
        "evaluate",
        evaluate_mock,
    )

    judge.main()

    report = json.loads(
        report_file.read_text(encoding="utf-8")
    )

    assert report["total_cases"] == 1
    assert report["success_cases"] == 1
    assert report["error_cases"] == 0
    assert report["evaluated_cases"] == 1

    assert report["details"][0]["judge"] == {
        "avg_score": 0.8,
        "metrics": {},
    }

    evaluate_mock.assert_called_once_with(
        instance_id="case-1",
        gold_doc="Gold documentation",
        generated_doc="Generated documentation",
    )


def test_main_failed_case(monkeypatch, tmp_path):
    report_dir = tmp_path / "reports"
    report_file = report_dir / "report.json"

    monkeypatch.setattr(judge, "REPORT_DIR", str(report_dir))
    monkeypatch.setattr(judge, "REPORT_FILE", str(report_file))
    monkeypatch.setattr(judge, "DATASET_FILE", "dataset")
    monkeypatch.setattr(judge, "RESULTS_FILE", "results")

    def mock_load_jsonl(path):
        if path == "dataset":
            return [
                {
                    "instance_id": "case-1",
                    "gold_md_path": "unused.md",
                }
            ]

        return [
            {
                "instance_id": "case-1",
                "status": "error",
                "error": "Agent failed",
            }
        ]

    monkeypatch.setattr(
        judge,
        "load_jsonl",
        mock_load_jsonl,
    )

    evaluate_mock = MagicMock()
    monkeypatch.setattr(
        judge,
        "evaluate",
        evaluate_mock,
    )

    judge.main()

    report = json.loads(
        report_file.read_text(encoding="utf-8")
    )

    assert report["success_cases"] == 0
    assert report["error_cases"] == 1
    assert report["evaluated_cases"] == 0

    evaluate_mock.assert_not_called()


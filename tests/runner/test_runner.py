import pytest
import json
from unittest.mock import MagicMock

import runner.main as runner

def test_get_update_true(monkeypatch):
    monkeypatch.setattr(runner, "UPDATE", "true")

    assert runner.get_update() is True


def test_get_update_false(monkeypatch):
    monkeypatch.setattr(runner, "UPDATE", "false")

    assert runner.get_update() is False


def test_load_dataset(tmp_path):
    dataset = tmp_path / "data.jsonl"
    dataset.write_text(
        '{"instance_id": "1"}\n'
        '\n'
        '{"instance_id": "2"}\n',
        encoding="utf-8",
    )

    result = runner.load_dataset(dataset)

    assert result == [
        {"instance_id": "1"},
        {"instance_id": "2"},
    ]


def test_load_dataset_invalid_json(tmp_path):
    dataset = tmp_path / "data.jsonl"
    dataset.write_text(
        '{"instance_id": "1"}\n'
        'aaaa\n',
        encoding="utf-8",
    )

    with pytest.raises(json.JSONDecodeError):
        runner.load_dataset(dataset)


def test_clone_repo(monkeypatch, tmp_path):
    monkeypatch.setattr(runner, "REPOS_DIR", str(tmp_path))

    run_mock = MagicMock()
    monkeypatch.setattr(runner.subprocess, "run", run_mock)

    result = runner.clone_repo(
        instance_id="repo-1",
        repo_url="https://example.com/repo.git",
    )

    expected = tmp_path / "repo-1"

    assert result == str(expected)

    run_mock.assert_called_once_with(
        [
            "git",
            "clone",
            "https://example.com/repo.git",
            str(expected),
        ],
        check=True,
    )


def test_clone_repo_existing_repo(monkeypatch, tmp_path):
    monkeypatch.setattr(runner, "REPOS_DIR", str(tmp_path))

    repo = tmp_path / "repo-1"
    repo.mkdir()

    run_mock = MagicMock()
    monkeypatch.setattr(runner.subprocess, "run", run_mock)

    result = runner.clone_repo(
        "repo-1",
        "https://example.com/repo.git",
    )

    assert result == str(repo)
    run_mock.assert_not_called()


def test_clone_repo_update_true(monkeypatch, tmp_path):
    monkeypatch.setattr(runner, "REPOS_DIR", str(tmp_path))

    repo = tmp_path / "repo-1"
    repo.mkdir()

    run_mock = MagicMock()
    monkeypatch.setattr(runner.subprocess, "run", run_mock)

    runner.clone_repo(
        "repo-1",
        "https://example.com/repo.git",
        update=True,
    )

    run_mock.assert_called_once()


def test_save_to_md(monkeypatch, tmp_path):
    monkeypatch.setattr(runner, "OUTPUT_DIR", str(tmp_path))

    result = runner.save_to_md(
        "instance-1",
        "# Documentation",
    )

    path = tmp_path / "instance-1.md"

    assert result == str(path)
    assert path.read_text(encoding="utf-8") == "# Documentation"


def test_log_tool_stats_removes_tool_calls(monkeypatch):
    logger = MagicMock()
    monkeypatch.setattr(runner, "logger", logger)

    stats = {
        "tool_calls_used": 1,
        "tool_calls": [
            {"tool_name": "read_repo_file"}
        ],
    }

    runner.log_tool_stats("instance-1", stats)

    assert "tool_calls" not in stats


def test_main_success(monkeypatch, tmp_path):
    output_dir = tmp_path / "output"
    results_file = output_dir / "results.jsonl"

    monkeypatch.setattr(runner, "OUTPUT_DIR", str(output_dir))
    monkeypatch.setattr(runner, "RESULTS_FILE", str(results_file))
    monkeypatch.setattr(runner, "MODEL_ALIAS", "test-model")
    monkeypatch.setattr(runner, "DATASET_FILE", "ignored")

    monkeypatch.setattr(
        runner,
        "load_dataset",
        lambda path: [
            {
                "instance_id": "case-1",
                "repo_url": "https://example.com/repo.git",
            }
        ],
    )

    monkeypatch.setattr(
        runner,
        "clone_repo",
        lambda **kwargs: "/tmp/repo",
    )

    monkeypatch.setattr(
        runner,
        "save_to_md",
        lambda instance_id, output_md: "/tmp/case-1.md",
    )

    monkeypatch.setattr(
        runner,
        "log_tool_stats",
        lambda instance_id, stats: None,
    )

    response = MagicMock()
    response.ok = True
    response.json.return_value = {
        "output_md": "generated docs",
        "tool_call_stats": {},
    }

    post_mock = MagicMock(return_value=response)
    monkeypatch.setattr(runner.requests, "post", post_mock)

    runner.main()

    records = [
        json.loads(line)
        for line in results_file.read_text(
            encoding="utf-8"
        ).splitlines()
    ]

    assert records == [
        {
            "instance_id": "case-1",
            "repo_path": "/tmp/repo",
            "output_md_path": "/tmp/case-1.md",
            "status": "success",
        }
    ]


def test_main_agent_fails(monkeypatch, tmp_path):
    output_dir = tmp_path / "output"
    results_file = output_dir / "results.jsonl"

    monkeypatch.setattr(runner, "OUTPUT_DIR", str(output_dir))
    monkeypatch.setattr(runner, "RESULTS_FILE", str(results_file))
    monkeypatch.setattr(runner, "DATASET_FILE", "ignored")

    monkeypatch.setattr(
        runner,
        "load_dataset",
        lambda path: [
            {
                "instance_id": "case-1",
                "repo_url": "repo-url",
            }
        ],
    )

    monkeypatch.setattr(
        runner,
        "clone_repo",
        lambda **kwargs: "/tmp/repo",
    )

    response = MagicMock()
    response.ok = False
    response.status_code = 500
    response.text = "boom"

    monkeypatch.setattr(
        runner.requests,
        "post",
        MagicMock(return_value=response),
    )

    runner.main()

    record = json.loads(
        results_file.read_text(
            encoding="utf-8"
        ).strip()
    )

    assert record["instance_id"] == "case-1"
    assert record["status"] == "error"
    assert "Agent returned code 500" in record["error"]

def test_main_missing_repo_url(monkeypatch, tmp_path):
    output_dir = tmp_path / "output"
    results_file = output_dir / "results.jsonl"

    monkeypatch.setattr(runner, "OUTPUT_DIR", str(output_dir))
    monkeypatch.setattr(runner, "RESULTS_FILE", str(results_file))
    monkeypatch.setattr(runner, "DATASET_FILE", "ignored")

    monkeypatch.setattr(
        runner,
        "load_dataset",
        lambda path: [
            {
                "instance_id": "case-1"
            }
        ],
    )

    monkeypatch.setattr(
        runner,
        "clone_repo",
        lambda **kwargs: "/tmp/repo",
    )

    runner.main()

    record = json.loads(
        results_file.read_text(
            encoding="utf-8"
        ).strip()
    )

    assert record["status"] == "error"
    assert "Repo url is missing" in record["error"]

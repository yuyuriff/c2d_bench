import pytest

import agent.tools as tools

def test_read_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("six seven", encoding="utf-8")

    result = tools.read_file(file)

    assert result == "six seven"


def test_read_file_trunc(tmp_path):
    file = tmp_path / "large.txt"
    file.write_text("six seven six seven", encoding="utf-8")

    result = tools.read_file(file, max_chars=5)

    assert result == "six s\n<...>"


def test_read_file_missing(tmp_path):
    file = tmp_path / "missing.txt"

    result = tools.read_file(file)

    assert result.startswith("Error reading file:")

def test_resolve_rel_path(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    result = tools.resolve_rel_path(repo, "src/main.py")

    assert result == (repo / "src/main.py").resolve()


def test_resolve_rel_path_out_of_folder(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    with pytest.raises(RuntimeError, match="Relative path not in repo folder"):
        tools.resolve_rel_path(repo, "../something.txt")

def test_get_repo_tree(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    (repo / "README.md").write_text("empty?", encoding="utf-8")

    src = repo / "src"
    src.mkdir()

    (src / "main.py").write_text("print('hello')", encoding="utf-8")

    result = tools.get_repo_tree(repo)

    lines = result.splitlines()

    assert "README.md" in lines
    assert "src/" in lines
    assert "src/main.py" in lines

def test_get_repo_tree_max_nodes(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    for i in range(10):
        (repo / f"file_{i}.txt").write_text("x", encoding="utf-8")

    result = tools.get_repo_tree(repo, max_nodes=5)

    assert len(result.splitlines()) == 5

def test_read_repo_file(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    file = repo / "README.md"
    file.write_text("empty?", encoding="utf-8")

    result = tools.read_repo_file(repo, "README.md")

    assert result == "empty?"


def test_read_repo_file_missing(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    result = tools.read_repo_file(repo, "missing.txt")

    assert result == "File does not exist: missing.txt"


def test_read_repo_file_directory(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    directory = repo / "src"
    directory.mkdir()

    result = tools.read_repo_file(repo, "src")

    assert result == "Path is not a file: src"


def test_read_repo_file_outside(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    outside = tmp_path / "something.txt"
    outside.write_text("secret", encoding="utf-8")

    with pytest.raises(RuntimeError):
        tools.read_repo_file(repo, "../something.txt")


def test_find_snippet():
    text = "blah blah blah " * 100 + "qUeRy" + " blah blah" * 100

    result = tools.find_snippet(text, "query")

    assert "qUeRy" in result


def test_search_in_repo_by_content(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    (repo / "file1.txt").write_text("hello docker something", encoding="utf-8")
    (repo / "file2.txt").write_text("something else", encoding="utf-8",)

    result = tools.search_in_repo(repo, "docker")

    assert "file1.txt" in result
    assert "docker" in result
    assert "file2.txt" not in result


def test_search_in_repo_by_filename(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()

    file = repo / "deepseek_config.txt"
    file.write_text("some config", encoding="utf-8")

    result = tools.search_in_repo(repo, "deepseek")

    assert "deepseek_config.txt" in result
    assert "some config" in result


def test_search_in_repo_empty_query(tmp_path):
    result = tools.search_in_repo(tmp_path, "")

    assert result == "<No matches>"

def test_search_in_repo_no_matches(tmp_path):
    (tmp_path / "test.txt").write_text("hello", encoding="utf-8")

    result = tools.search_in_repo(tmp_path, "docker")

    assert result == "<No matches>"


def test_search_in_repo_respects_max_results(tmp_path):
    for i in range(10):
        (tmp_path / f"file_{i}.txt").write_text(
            "docker compose",
            encoding="utf-8",
        )

    result = tools.search_in_repo(tmp_path, "Docker Compose", max_results=5)

    assert len(result.splitlines()) == 5


def test_execute_tool_read_repo_file(monkeypatch, tmp_path):
    args = {}

    def mock_read_repo_file(repo_dir, rel_path, max_chars):
        args["repo_dir"] = repo_dir
        args["rel_path"] = rel_path
        args["max_chars"] = max_chars

        return "file contents"

    monkeypatch.setattr(
        tools,
        "read_repo_file",
        mock_read_repo_file,
    )

    result = tools.execute_tool(
        repo_dir=tmp_path,
        tool_name="read_repo_file",
        arguments={"path": "src/main.py"},
        max_chars_per_file=1234,
    )

    assert result == "file contents"
    assert args["repo_dir"] == tmp_path
    assert args["rel_path"] == "src/main.py"
    assert args["max_chars"] == 1234


def test_execute_tool_unknown_tool(tmp_path):
    result = tools.execute_tool(
        tmp_path,
        "dance",
        {},
    )

    assert result == "Unavailable tool: dance"

def test_execute_tool_search_mcp(monkeypatch, tmp_path):
    calls = []

    def mock_call_mcp_tool(tool_name, arguments):
        calls.append((tool_name, arguments))
        return "MCP response"

    monkeypatch.setattr(
        tools,
        "call_mcp_tool",
        mock_call_mcp_tool,
    )

    result = tools.execute_tool(
        tmp_path,
        "search_mcp",
        {"query": "FastAPI"},
    )

    assert result == "MCP response"
    assert calls == [
        ("search_mcp", {"query": "FastAPI"})
    ]

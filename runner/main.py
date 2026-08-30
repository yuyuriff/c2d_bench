import os
import json
import subprocess
from pathlib import Path
import shutil
import logging

import requests

AGENT_URL = os.getenv("AGENT_URL", "http://localhost:8000/generate")

DATASET_DIR = "/workspace/benchmark/datasets"
DATASET_FILE_ENV = os.getenv("DATASET_FILE", "run_001.jsonl")
DATASET_FILE =  os.path.join(DATASET_DIR, DATASET_FILE_ENV)

RUN_ID = os.getenv("RUN_ID", "001")
RUN_NAME = f"run_{RUN_ID}"
MODEL_ALIAS = os.getenv("MODEL_ALIAS", "")

REPOS_DIR = "/workspace/repos"
OUTPUT_DIR = os.path.join("/workspace/benchmark/agent_output", RUN_NAME)
RESULTS_FILE = os.path.join(OUTPUT_DIR, f"{RUN_NAME}.jsonl")

LOG_DIR = "/workspace/benchmark/logs"
LOG_FILE = os.path.join(LOG_DIR, f"{RUN_NAME}.log")

UPDATE = os.getenv("UPDATE", "false")

def get_update() -> bool:
    if UPDATE == "true":
        return True
    return False

def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        filemode="w",
        level=logging.INFO,
        force=True,
    )
    return logging.getLogger("runner")

logger = setup_logging()

def load_dataset(path: Path):
    cases = []
    with open(path, "r", encoding="utf-8") as dataset_file:
        for line in dataset_file:
            line = line.strip()
            if not line:
                continue
            cases.append(json.loads(line))

    return cases

def clone_repo(instance_id: str, repo_url: str, update: bool = False) -> str:
    os.makedirs(REPOS_DIR, exist_ok=True)
    repo_path = Path(os.path.join(REPOS_DIR, instance_id))

    if not repo_path.exists() or update:
        logger.info("Cloning %s to %s", repo_url, repo_path)
        subprocess.run(["git", "clone", repo_url, str(repo_path)], check=True)
    else:
        logger.info("Repo already exists at: %s", repo_path)

    return str(repo_path)

def save_to_md(instance_id: str, output_md: str) -> str:
    filename = f"{instance_id}.md"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as md:
        md.write(output_md)

    return path

def log_tool_stats(instance_id: str, stats : dict):
    calls = stats.pop("tool_calls", [])
    logger.info("Tool call stats for instance %s: %s", instance_id, json.dumps(stats))
    for call in calls:
        logger.info("Tool call: %s", json.dumps(call))

def main():
    logger.info(
        "Benchmark run started: run_id=%s dataset=%s results=%s logs=%s",
        RUN_NAME, DATASET_FILE_ENV, RESULTS_FILE, LOG_FILE,
    )

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    cases = load_dataset(DATASET_FILE)
    logger.info("Loaded %s cases", len(cases))
    logger.info("Using %s model", MODEL_ALIAS)

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        for case in cases:
            instance_id = case.get("instance_id", "unknown")
            repo_url = case.get("repo_url")

            logger.info("Processing instance: %s", instance_id)

            try:
                if not repo_url:
                    raise RuntimeError(f"Repo url is missing in case {instance_id}")

                repo_path = clone_repo(instance_id=instance_id, repo_url=repo_url, update=get_update())
                request = {
                    "instance_id": instance_id,
                    "repo_path": repo_path,
                    "llm_model_alias": MODEL_ALIAS,
                }
                response = requests.post(AGENT_URL, json=request)
                if not response.ok:
                    raise RuntimeError(f"Agent returned code {response.status_code}: {response.text}")

                result = response.json()
                output_md = result.get("output_md", "")
                tool_call_stats = result.get("tool_call_stats", {})

                log_tool_stats(instance_id, tool_call_stats)
                md = save_to_md(instance_id, output_md)

                case_result = {
                    "instance_id": instance_id,
                    "repo_path": repo_path,
                    "output_md_path": md,
                    "status": "success",
                }
                results_file.write(json.dumps(case_result) + "\n")
                logger.info("Instance processed: %s", instance_id)

            except Exception as e:
                logger.exception("Instance failed: %s", instance_id)
                error_record = {
                    "instance_id": instance_id,
                    "status": "error",
                    "error": str(e),
                }
                results_file.write(json.dumps(error_record) + "\n")

    logger.info("Benchmark run finished. Results: %s", RESULTS_FILE)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Benchmark run failed")
        raise SystemExit(1)
    
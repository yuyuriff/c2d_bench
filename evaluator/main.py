import json
import os
import logging
from pathlib import Path

from evaluate import evaluate

DATASET_DIR = "/workspace/benchmark/datasets/"
DATASET_FILE_ENV = os.getenv("DATASET_FILE", "run_001.jsonl")
DATASET_FILE = DATASET_DIR + DATASET_FILE_ENV

RUN_ID = os.getenv("RUN_ID", "001")
RUN_NAME = f"run_{RUN_ID}"

OUTPUT_DIR = os.path.join("/workspace/benchmark/agent_output", RUN_NAME)
RESULTS_FILE = os.path.join(OUTPUT_DIR, f"{RUN_NAME}.jsonl")
REPORT_DIR = os.path.join("/workspace/benchmark/reports", RUN_NAME)
REPORT_FILE = os.path.join(REPORT_DIR, f"{RUN_NAME}.json")

LOG_DIR = "/workspace/benchmark/logs"
LOG_FILE = os.path.join(LOG_DIR, f"{RUN_NAME}.log")

def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        filemode="w",
    )
    return logging.getLogger("evaluator")

logger = setup_logging()

def load_jsonl(path):
    rows = []
    if not os.path.exists(path):
        return rows

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows

def get_gold_dict(dataset) -> dict[str, str]:
    instances = {}
    for case in dataset:
        instance_id = case.get("instance_id")
        if instance_id:
            instances[instance_id] = case.get("gold_md_path")
    return instances

def main():
    os.makedirs(REPORT_DIR, exist_ok=True)
    logger.info(
        "Evaluator run started: run_id=%s dataset=%s results=%s report=%s",
        RUN_NAME, DATASET_FILE, RESULTS_FILE, REPORT_FILE,
    )

    dataset = load_jsonl(DATASET_FILE)
    results = load_jsonl(RESULTS_FILE)
    gold_mds = get_gold_dict(dataset)

    total_cases = len(dataset)
    success_cases = 0
    error_cases = 0
    evaluated_cases = 0

    details = []

    for case in results:
        instance_id = case.get("instance_id", "unknown")
        status = case.get("status")
        md_path = case.get("output_md_path")
        gold_path = gold_mds.get(instance_id, "")

        generated_doc = Path(md_path).read_text()
        gold_doc = Path(gold_path).read_text()
        output_exists = bool(generated_doc)
        gold_exists = bool(gold_doc)

        if status == "success":
            success_cases += 1
        else:
            error_cases += 1

        detail = {
            "instance_id": instance_id,
            "status": status,
            "error": case.get("error", ""),
            "output_md_path": md_path,
            "gold_md_path": gold_path,
            "output_md_exists": output_exists,
            "gold_md_exists": gold_exists,
        }

        if status == "success" and output_exists and gold_exists:
            try:
                logger.info("Evaluating instance: %s", instance_id)
                eval_result = evaluate(
                    instance_id=instance_id,
                    gold_doc=gold_doc,
                    generated_doc=generated_doc,
                )

                evaluated_cases += 1
                detail["judge"] = eval_result

            except Exception as e:
                detail["judge_error"] = str(e)
                logger.exception("Evaluation error on case %s", instance_id)

        details.append(detail)

    report = {
        "run_id": RUN_ID,
        "dataset_file": DATASET_FILE,
        "total_cases": total_cases,
        "success_cases": success_cases,
        "error_cases": error_cases,
        "evaluated_cases": evaluated_cases,
        "details": details,
    }
    with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
        json.dump(report, report_file, indent=2)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Evaluation failed")
        raise SystemExit(1)

import os
import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument("--model", required=True)
parser.add_argument("--run_id")
parser.add_argument("--dataset_file", required=True)
parser.add_argument("--update_repo", action="store_true")

args = parser.parse_args()

env = os.environ.copy()
env["MODEL_ALIAS"] = args.model 
env["RUN_ID"] = args.run_id or "run_001"
env["DATASET_FILE"] = args.dataset_file
env["UPDATE"] = str(args.update_repo).lower()

result = subprocess.run(
    ["docker", "compose", "up", "--build", "--exit-code-from", "evaluator"],
    env=env,
)

raise SystemExit(result.returncode)
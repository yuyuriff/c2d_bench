import os
import argparse
import subprocess

def config_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model", required=True)
    parser.add_argument("--run_id", default="001")
    parser.add_argument("--dataset_file", required=True)
    parser.add_argument("--update_repo", action="store_true")
    parser.add_argument("--prompt")

    return parser

def fill_env(env, args):
    env["MODEL_ALIAS"] = args.model 
    env["RUN_ID"] = args.run_id
    env["DATASET_FILE"] = args.dataset_file
    env["UPDATE"] = str(args.update_repo).lower()

def run(cmd, env):
    print("$", " ".join(cmd))
    result = subprocess.run(cmd, env=env)

    print(f"Exit code: {result.returncode}")
    return result.returncode


def main():
    parser = config_parser()
    args = parser.parse_args()

    env = os.environ.copy()
    fill_env(env, args)

    try:
        code = run(
            ["docker", "compose", "up", "-d", "--build", "api-agent", "mcp-server"],
            env,
        )
        if code != 0:
            return code

        code = run(
            ["docker", "compose", "run", "--rm", "runner"],
            env,
        )
        if code != 0:
            return code

        code = run(
            ["docker", "compose", "run", "--rm", "--no-deps", "evaluator"],
            env,
        )

        return code

    except Exception as e:
        print(f"Launcher error: {e}")
        return 1

    finally:
        subprocess.run(
            ["docker", "compose", "down"],
            env=env,
        )

if __name__ == "__main__":
    raise SystemExit(main())
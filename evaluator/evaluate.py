import os

from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams

def get_judge_config() -> dict[str, str | None]:
    api_key = os.getenv("JUDGE_API_KEY")
    base_url = os.getenv("JUDGE_BASE_URL")
    model = os.getenv("JUDGE_MODEL")

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    if base_url:
        os.environ["OPENAI_BASE_URL"] = base_url

    return {
        "api_key": api_key,
        "base_url": base_url,
        "model": model,
    }

def build_metrics(model: str | None = None):
    return [
        GEval(
            name="alignment_to_gold",
            criteria=(
                "Evaluate how factually aligned the generated documentation is with the provided gold doc. "
                "Reduce points for misinformation and hallucinations."
            ),
            evaluation_params=[
                SingleTurnParams.ACTUAL_OUTPUT,
                SingleTurnParams.EXPECTED_OUTPUT,
            ],
            model = model,
        ),
        GEval(
            name="coverage_of_gold",
            criteria=(
                "Evaluate the coverage of the gold doc, if any entities are missed."
            ),
            evaluation_params=[
                SingleTurnParams.ACTUAL_OUTPUT,
                SingleTurnParams.EXPECTED_OUTPUT,
            ],
            model = model,
        ),
        GEval(
            name="structure_and_readability",
            criteria=(
                "Evaluate whether the generated documentation is readable, easy to navigate, structured, "
                "clear, and useful as technical documentation."
            ),
            evaluation_params=[
                SingleTurnParams.ACTUAL_OUTPUT,
            ],
            model = model,
        ),
    ]

def evaluate(instance_id: str, gold_doc: str, generated_doc: str) -> dict:
    config = get_judge_config()

    if not config.get("api_key"):
        raise RuntimeError("JUDGE_API_KEY is not set")

    if not config.get("base_url"):
        raise RuntimeError("JUDGE_BASE_URL is not set")

    if not config.get("model"):
        raise RuntimeError("JUDGE_MODEL is not set")

    test_case = LLMTestCase(
        input=f"Generate technical documentation for instance {instance_id}",
        actual_output=generated_doc,
        expected_output=gold_doc,
    )

    metrics = build_metrics(config.get("model"))
    
    eval_result = {}
    scores = []

    for metric in metrics:
        metric.measure(test_case)
        score = float(metric.score or 0.0)
        scores.append(score)
        eval_result[metric.name] = {
            "score": score,
            "reason": metric.reason or "",
        }

    avg = sum(scores) / len(scores) if scores else 0.0

    return {
        "avg_score": avg,
        "metrics": eval_result,
    }

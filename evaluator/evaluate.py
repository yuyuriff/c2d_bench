import os

from openai import OpenAI
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

JUDGE_API_KEY = os.getenv("JUDGE_API_KEY")
JUDGE_BASE_URL = os.getenv("JUDGE_BASE_URL")
JUDGE_MODEL = os.getenv("JUDGE_MODEL")

# default for deepeval
os.environ.setdefault("OPENAI_API_KEY", JUDGE_API_KEY)
os.environ.setdefault("OPENAI_BASE_URL", JUDGE_BASE_URL)

def get_client() -> OpenAI:
    if not JUDGE_API_KEY:
        raise RuntimeError("JUDGE_API_KEY is not set")
    if not JUDGE_BASE_URL:
        raise RuntimeError("JUDGE_BASE_URL is not set")
    if not JUDGE_MODEL:
        raise RuntimeError("JUDGE_MODEL is not set")
    return OpenAI(
        api_key=JUDGE_API_KEY,
        base_url=JUDGE_BASE_URL,
    )

def build_metrics(model: str | None = None):
    return [
        GEval(
            name="alignment_to_gold",
            criteria=(
                "Evaluate how factually aligned the generated documentation is with the provided gold doc. "
                "Reduce points for misinformation and hallucinations."
            ),
            evaluation_params=[
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.EXPECTED_OUTPUT,
            ],
            model = model,
        ),
        GEval(
            name="coverage_of_gold",
            criteria=(
                "Evaluate the coverage of the gold doc, if any entities are missed."
            ),
            evaluation_params=[
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.EXPECTED_OUTPUT,
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
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
            model = model,
        ),
    ]

def evaluate(instance_id: str, gold_doc: str, generated_doc: str) -> dict:
    test_case = LLMTestCase(
        input=f"Generate technical documentation for instance {instance_id}",
        actual_output=generated_doc,
        expected_output=gold_doc,
    )

    metrics = build_metrics(JUDGE_MODEL)
    
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

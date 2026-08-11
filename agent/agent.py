from openai import OpenAI

import os
from pathlib import Path

def get_default_prompt() -> str:
    with open("/workspace/config/prompts/default.md", "r", encoding="utf-8") as f:
        return f.read()

def get_client(config: dict) -> OpenAI:
    api_key = os.environ.get(config["api_key_env"])
    base_url = config["base_url"]

    if not api_key:
        raise RuntimeError(f"{config["api_key_env"]} is not set")
    if not base_url:
        raise RuntimeError("Base url is not set")

    return OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

def call_llm(repo_dir: Path, config: dict, max_chars_per_file: int = 15_000, prompt: str | None = None) -> str:
    client = get_client(config)

    messages = [
        {
            "role": "system",
            "content": "You are a technical writer. You write accurate documentation."
        },
        {
            "role": "user",
            "content": f"{prompt or get_default_prompt()}"
        }
    ]

    model = config["model_name"]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=False,
        temperature=0.1
    )

    message = response.choices[0].message.content
    return message

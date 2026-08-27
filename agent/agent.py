from openai import OpenAI

import os
import json
from pathlib import Path

from tools import TOOLS, execute_tool

CONFIG_DIR = Path("/workspace/config")

def get_default_prompt() -> str:
    prompt_dir = CONFIG_DIR / "prompts/default.md"
    with prompt_dir.open("r", encoding="utf-8") as f:
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
    max_turns = config.get("max_turns") or 100

    for _ in range(max_turns):
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            stream=False,
            temperature=0.1,
        )

        message = response.choices[0].message
        if not getattr(message, "tool_calls", None):
            return message.content or "Something went wrong. Model did not produce any output"

        messages.append(message.model_dump())

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            args = tool_call.function.arguments or "{}"

            try:
                args = json.loads(args)
            except Exception:
                args = {}

            tool_result = ""
            try:
                tool_result = execute_tool(
                    repo_dir=repo_dir,
                    tool_name=tool_name,
                    arguments=args,
                    max_chars_per_file=max_chars_per_file,
                )
            except Exception as e:
                tool_result = f"Error executing tool: {e}"

            messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result,
            })

    messages.append({
        "role": "system",
        "content": (
            "Turn limit reached. Now write the best possible documentation using gathered information"
        )
    })

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=TOOLS,
        tool_choice="none",
        stream=False,
        temperature=0.1,
    )

    message = response.choices[0].message.content or "Something went wrong. Model did not produce any output"
    return message

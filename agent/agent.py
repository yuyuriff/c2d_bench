from openai import OpenAI

import os
import json
from pathlib import Path

from .tools import TOOLS, execute_tool
from .config import get_agent_limits, get_default_prompt

def get_client(config: dict, model_timeout: int) -> OpenAI:
    api_key = os.environ.get(config["api_key_env"])
    base_url = config["base_url"]

    if not api_key:
        raise RuntimeError(f"{config['api_key_env']} is not set")
    if not base_url:
        raise RuntimeError("Base url is not set")

    return OpenAI(
        api_key=api_key,
        base_url=base_url,
        timeout=model_timeout,
    )

def call_llm(repo_dir: Path, config: dict, prompt: str | None = None, instance_id: str = "") -> tuple[str, dict]:
    model = config["model_name"]
    limits = get_agent_limits(config)
    timeout = limits["model_timeout"]
    client = get_client(config, timeout)

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

    max_chars_per_file = limits["max_chars_per_file"]
    max_turns = limits["max_turns"]
    max_tool_calls = limits["max_tool_calls"]

    tool_calls_used = 0
    tool_calls_failed = 0
    tool_calls_stats = {}
    tool_calls = []
    stop_reason = f"Reached max turns ({max_turns})"
    tool_limit_reached = False

    stats = {
        "tool_calls_used": tool_calls_used,
        "tool_calls_failed": tool_calls_failed,
        "tool_calls_stats": tool_calls_stats,
        "tool_calls": tool_calls,
        "stop_reason": stop_reason,
    }

    for turn in range(max_turns):
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
            stats["tool_calls_used"] = tool_calls_used
            stats["tool_calls_failed"] = tool_calls_failed
            stats["tool_calls_stats"] = tool_calls_stats
            stats["tool_calls"] = tool_calls
            stats["stop_reason"] = "Final output"
            text = message.content or "Something went wrong. Model did not produce any output"
            return text, stats

        messages.append(message.model_dump())

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            args = tool_call.function.arguments or "{}"

            if tool_calls_used >= max_tool_calls:
                tool_calls_failed += 1
                tool_limit_reached = True
                tool_calls.append({
                    "instance_id": instance_id,
                    "model": model,
                    "turn": turn,
                    "tool_call_id": tool_call.id,
                    "tool_name": tool_name,
                    "arguments": args,
                    "status": "limited",
                    "message": "Tool limit reached",
                })
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": "Tool limit reached"
                })
                continue

            try:
                args = json.loads(args)
            except Exception:
                args = {}

            tool_result = ""
            status = "success"
            try:
                tool_result = execute_tool(
                    repo_dir=repo_dir,
                    tool_name=tool_name,
                    arguments=args,
                    max_chars_per_file=max_chars_per_file,
                )
            except Exception as e:
                status = "error"
                tool_calls_failed += 1
                tool_result = f"Error executing tool: {e}"

            tool_calls_stats[tool_name] = tool_calls_stats.get(tool_name, 0) + 1
            tool_calls.append({
                "instance_id": instance_id,
                "model": model,
                "turn": turn,
                "tool_call_id": tool_call.id,
                "tool_name": tool_name,
                "arguments": args,
                "status": status,
            })

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": tool_result,
            })

            tool_calls_used += 1

        if tool_limit_reached:
            stop_reason = f"Reached max tool calls ({max_tool_calls})"
            break

    messages.append({
        "role": "system",
        "content": (
            "Limit reached. Now write the best possible documentation using gathered information"
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
    stats["tool_calls_used"] = tool_calls_used
    stats["tool_calls_failed"] = tool_calls_failed
    stats["tool_calls_stats"] = tool_calls_stats
    stats["tool_calls"] = tool_calls
    stats["stop_reason"] = stop_reason
    return message, stats

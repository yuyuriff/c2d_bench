import json
from pathlib import Path

CONFIG_DIR = Path("/workspace/config")

def load_models_config(config_dir: Path = CONFIG_DIR):
    model_path = config_dir / "models.json"
    with model_path.open("r", encoding="utf-8") as config_file:
        return json.load(config_file)

def get_model_config(model_alias: str):
    available_models_config = load_models_config()
    if model_alias in available_models_config:
        return {**available_models_config[model_alias], "alias": model_alias}

    available_aliases = ", ".join(available_models_config.keys())
    raise RuntimeError(
        f"Unknown model alias: {model_alias}. Available aliases: {available_aliases}"
    )

def load_limits_config(config_dir: Path = CONFIG_DIR):
    limits_path = config_dir / "limits.json"
    if not limits_path.exists():
        return {}

    with limits_path.open("r", encoding="utf-8") as limits:
        return json.load(limits)

def set_limits(*limits: dict | None) -> dict:
    new_limits = {}
    for line in limits:
        if line:
            new_limits.update(line)
    return new_limits

def get_agent_limits(config: dict | None = None) -> dict:
    limits_config = load_limits_config()
    special_limits = {}

    if config:
        models_limits = limits_config.get("models", {})
        alias = config.get("alias")

        if alias in models_limits:
            special_limits.update(models_limits[alias])

    limits = set_limits(limits_config.get("agent"), special_limits)
    return {key: int(value) for key, value in limits.items()}

def get_default_prompt(config_dir: Path = CONFIG_DIR) -> str:
    prompt_dir = config_dir / "prompts" / "default.md"
    with prompt_dir.open("r", encoding="utf-8") as f:
        return f.read()


def load_prompt(prompt_name: str | None, config_dir: Path = CONFIG_DIR):
    if not prompt_name:
        return get_default_prompt()
    
    prompt_path = config_dir / "prompts" / f"{prompt_name}.md"

    if not prompt_path.exists():
        raise RuntimeError(f"Prompt does not exist: {prompt_path}")

    if not prompt_path.is_file():
        raise RuntimeError(f"Prompt path is not a file: {prompt_path}")

    prompt_text = prompt_path.read_text(encoding="utf-8").strip()

    if not prompt_text:
        raise RuntimeError(f"Prompt is empty: {prompt_path}")

    return prompt_text
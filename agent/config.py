import json
from pathlib import Path

CONFIG_DIR = Path("/workspace/config")

def load_models_config():
    model_path = CONFIG_DIR / "models.json"
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

def load_limits_config():
    limits_path = CONFIG_DIR / "limits.json"
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

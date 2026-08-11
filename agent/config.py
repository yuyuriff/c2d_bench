import json

def load_models_config():
    with open("workspace/config/models.json", "r", encoding="utf-8") as config_file:
        return json.load(config_file)

def get_model_config(model_alias: str):
    available_models_config = load_models_config
    if model_alias in available_models_config:
        return {**available_models_config[model_alias], "alias": model_alias}

    available_aliases = ", ".join(available_models_config.keys())
    raise RuntimeError(
        f"Unknown model alias: {model_alias}. Available aliases: {available_aliases}"
    )

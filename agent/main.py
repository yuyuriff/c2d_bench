from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from pathlib import Path

from .config import get_model_config, load_prompt
from .agent import call_llm

app = FastAPI()

class GenerateRequest(BaseModel):
    instance_id: str
    repo_path: str
    llm_model_alias: str
    prompt: str | None = None

@app.post("/generate")
def generate(request: GenerateRequest):
    instance_id = request.instance_id
    repo_dir = Path(request.repo_path)
    prompt_name = request.prompt

    if not repo_dir.exists():
        raise HTTPException(status_code=400,
                            detail=f"Repo path does not exist: {repo_dir}")
    if not repo_dir.is_dir():
        raise HTTPException(status_code=400,
                            detail=f"Repo path is not a directory: {repo_dir}")

    try:
        model_alias = request.llm_model_alias
        model_config = get_model_config(model_alias)
        prompt = load_prompt(prompt_name)

        output_md, stats = call_llm(repo_dir=repo_dir, config=model_config, instance_id=instance_id, prompt=prompt)

        return {
            "instance_id": request.instance_id,
            "output_md": output_md,
            "tool_call_stats": stats,
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

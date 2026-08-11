from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from pathlib import Path

from config import get_model_config
from agent import call_llm

app = FastAPI()

class GenerateRequest(BaseModel):
    instance_id: str
    repo_path: str
    llm_model_alias: str

@app.post("/generate")
def generate(request: GenerateRequest):
    repo_dir = Path(request.repo_path)

    if not repo_dir.exists():
        raise HTTPException(status_code=400,
                            detail=f"Repo path does not exist: {repo_dir}")
    if not repo_dir.is_dir():
        raise HTTPException(status_code=400,
                            detail=f"Repo path is not a directory: {repo_dir}")

    try:
        model_alias = request.llm_model_alias
        model_config = get_model_config(model_alias)

        output_md = call_llm(repo_dir, model_config)

        return {
            "instance_id": request.instance_id,
            "output_md": output_md,
        }
    
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=str(e))

from fastapi import FastAPI
from src.utils.response_evaluator import evaluate_llm_response

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/evaluate_response")
def score_response(response: str):
    result = evaluate_llm_response(response)
    return {"result": result}

@app.get("/health")
def health_check():
    return {"status": "ok"}

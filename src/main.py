from fastapi import FastAPI
from src.utils.response_evaluator import evaluate_llm_response
from src.utils.db import supabase
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class ResponseInput(BaseModel):
    response: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/evaluate_response")
def score_response(user_input: ResponseInput):
    result = evaluate_llm_response(user_input.response)
    # {'gibberish': {'class': 'noise', 'score': 4.261982440948486}, 'hallucination': 0.4346300959587097}
    supabase.table("sentence_data").insert({
        "sentence": user_input.response,
        "gibberish_model_class": result["gibberish"]["class"],
        "gibberish_model_score": result["gibberish"]["score"],
        "hallucination_model_score": result["hallucination"],
    }).execute()

    return {"result": result}

@app.get("/get_all_data")
def get_all_data():
    response = supabase.table("sentence_data").select("sentence, gibberish_model_class, gibberish_model_score, hallucination_model_score").execute()
    return response.data
@app.get("/health")
def health_check():
    return {"status": "ok"}

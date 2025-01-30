from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.utils.response_evaluator import evaluate_llm_response

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/evaluate_response")
async def score_response(request: Request):
    response_text = await request.body()
    result = evaluate_llm_response(response_text.decode())
    return {"result": result}

@app.get("/health")
def health_check():
    return {"status": "ok"}

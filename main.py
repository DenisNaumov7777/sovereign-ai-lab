from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Data model for input (what we expect from the API)
class UserInput(BaseModel):
    prompt: str

@app.post("/chat")
def chat_with_ai(message: UserInput):
    # 1. Construct request to Ollama (running on the host Mac)
    # host.docker.internal allows Docker to access the host machine
    ollama_url = "http://host.docker.internal:11434/api/generate"
    
    payload = {
        "model": "mistral",
        "prompt": message.prompt,
        "stream": False  # We wait for the full response
    }

    try:
        # 2. Send request to the "Brain"
        response = requests.post(ollama_url, json=payload)
        
        # 3. Extract response text
        result = response.json()
        return {"response": result["response"], "model": "mistral-local"}
        
    except Exception as e:
        return {"error": str(e), "hint": "Is Ollama running?"}

@app.get("/")
def health_check():
    return {"status": "Sovereign AI is Running", "device": "MacBook M4 Pro Max"}
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# CORS liberado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

def gerar_resposta(mensagem: str) -> str:
    # Simula resposta de IA de irrigação
    respostas = [
        "Irrigue por 15 minutos hoje.",
        "Solo úmido, não irrigue agora.",
        "Previsão de chuva, adie a irrigação.",
        "Irrigue por 10 minutos amanhã cedo.",
    ]
    return random.choice(respostas)

@app.post("/chat")
async def chat(request: ChatRequest, x_api_key: str = Header(...)):
    if x_api_key != "minha-chave-secreta":
        raise HTTPException(status_code=403, detail="API key inválida")
    resposta = gerar_resposta(request.message)
    return {"resposta": resposta}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

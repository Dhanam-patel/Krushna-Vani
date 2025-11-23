from fastapi import FastAPI, HTTPException
from Schemas.Chat_validator import Chat_Validator
from Embedding_Pipeline.vector_db.pinecone_vector import Pinecone_vector
from Vector_Search.Search import Vector_searching   
from AI_Pipeline.client import Generate_response

app = FastAPI(title="Krushna-Vani")

@app.get("/")
def home():
    return {"message": "Krushna Vani an RAG based AI to chat with Bhagavad Gita"}

@app.get("/health")
def health():
    return {
        "status": "OK",
        "Model": "Krushna-Vani",
        "Version": "1.0.0"
    }

@app.post("/Chat")
def Chat(data: Chat_Validator):
    user_input = [data.Input]
    vector = Pinecone_vector(user_input)
    result = Vector_searching(vector[0])
    AI_Output = Generate_response(user_input, result)
    return {"response":AI_Output}    


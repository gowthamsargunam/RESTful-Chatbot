# Load Env
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_TOKEN")

#login
from huggingface_hub import login, whoami

login(token)
prof = whoami()
print("Logged in as:", prof.get("name", "unknown user"))

# Needed Dependencies
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import datetime

# Fast API
app = FastAPI()

#Requests
class ChatRequest(BaseModel):
    message: str
    prompt: str = "You are a helpful assistant."

# Model
MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
dev = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {dev.upper()}")

tokenizer = AutoTokenizer.from_pretrained(MODEL, token=token)

model = AutoModelForCausalLM.from_pretrained( MODEL, torch_dtype=torch.float16 if dev == "cuda" else torch.float32, device_map={"": dev} )

# Logging Function
def log_conversation(user_input, bot_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", mode="a", encoding="utf-8") as logfile:
        logfile.write(f"\n[{timestamp}]\nUser: {user_input}\nBot : {bot_response}\n")

# Endpoint
@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    msg = req.message.strip()
    prompt = req.prompt.strip()

    if not msg:
        return {"response": "Error: message is empty!"}

    prompt = f"<|system|>{prompt}<|user|>{msg}<|assistant|>"

    tensor = tokenizer(prompt, return_tensors="pt").to(dev)

    with torch.no_grad():
        response_ids = model.generate(tensor.input_ids, max_new_tokens=100, do_sample=True, temperature=0.7, top_p=0.9)
    decode = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    reply = decode.split("<|assistant|>")[-1].strip()

    log_conversation(msg, reply)
    return {"response": reply}

# Test
@app.get("/")
async def index():
    return {
        "message": "Chatbot is running!",
        "usage": "Chat with JSON { 'message': 'Hi there!' }"
    }
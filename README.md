# RESTful - Chatbot
A simple **RESTful chatbot** service in Python using Llama Model

![image](https://sdmntprcentralus.oaiusercontent.com/files/00000000-97cc-61f5-b1f7-8bb457acb2d4/raw?se=2025-07-26T15%3A44%3A25Z&sp=r&sv=2024-08-04&sr=b&scid=e43dc29a-8c1b-527a-9b8a-e82fe30e21f3&skoid=add8ee7d-5fc7-451e-b06e-a82b2276cf62&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-26T12%3A09%3A52Z&ske=2025-07-27T12%3A09%3A52Z&sks=b&skv=2024-08-04&sig=H8oOQISL6dcJ1iUTC4Uw6rMH1DmkJwka0b3XJ/isNZM%3D)

### This project implements a basic RESTful API chatbot service in Python using FastAPI, powered by the TinyLlama language model. It allows users to send messages via HTTP POST requests and receive AI-generated responses.

### STEP 1

### Installation Needed Libraries
 
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt
```

### STEP 2 

### Setup ⚙ 
Create a .env file in the root directory:

```
Hf_Token = " your_huggingface_token_here "
```

Login or Signup Hugging Face through : https://huggingface.co/

Create a token Copy that and Get your Hugging Face token from: https://huggingface.co/settings/tokens

### STEP 3

### Running the Server
Run the file **bot.py** by
Starting the FastAPI chatbot server with:

```
uvicorn bot:app --reload
```

Once running, the API will be available at:

```
http://127.0.0.1:8000
```

### STEP 4

### Testing the Chatbot
You can test the chatbot by running the file data.py

```
python data.py
```


### Features:

**RESTful API:** Exposes a /chat endpoint for conversational interaction.

**Llama Integration:** Uses the **TinyLlama-1.1B-Chat-v1.0** model for response generation.

**FastAPI Backend:** Built with FastAPI for high performance and easy API development.

**Hugging Face Integration:** Loads models from Hugging Face Hub using a token.

**GPU Acceleration:** Automatically leverages CUDA (GPU) if available for faster inference, otherwise falls back to CPU.

**Conversation Logging:** Records all user inputs and bot responses to a log file.

**Simple Client:** Includes a basic Python script to demonstrate interacting with the service.


### Note:

## This project uses the TinyLlama 1.1B Chat model:
https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
Use this Model for best performance, run on a machine with a GPU.

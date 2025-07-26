import requests

url = "http://127.0.0.1:8000/chat"

#data
data = {
    "message": "what is Postgre SQL?",
    "system_prompt": "You are a helpful assistant."
}

# Request
req = requests.post(url, json=data)

# Answer
if req.ok:
    print("Bot:", req.json()["response"])
else:
    print("Error:", req.status_code, req.text)

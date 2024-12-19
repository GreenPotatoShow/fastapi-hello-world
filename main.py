import requests
import httpx
from fastapi import FastAPI, Request

app = FastAPI()
my_token="7898884050:AAFkWzlGrlJ03pZ9dLUMh7nhZBR5xzucvWY"

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/bot/")
async def bot(request: Request):
    message = await request.json()
    chat_id=message["message"]["chat"]["id"]
    user_name=message["message"]["chat"]["username"]
    async with httpx.AsyncClient() as client:
        await client.get(f'https://api.telegram.org/bot{my_token}/sendMessage',
                    params = {
                        'chat_id': chat_id,
                        'text': f'Привет, {user_name}!'
                        }
                    )
    return message





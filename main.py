import re
import httpx
from fastapi import FastAPI, Request

app = FastAPI()
my_token="7898884050:AAFkWzlGrlJ03pZ9dLUMh7nhZBR5xzucvWY"

async def sum_n_ones(n):
    result=0
    for i in range(10**n):
        result+=1
    return result

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/bot/")
async def bot(request: Request):
    message = await request.json()
    chat_id=message["message"]["chat"]["id"]
    text=message["message"]["text"]
    if re.findall(r'\D', text):
        async with httpx.AsyncClient() as client:
            await client.get(f'https://api.telegram.org/bot{my_token}/sendMessage',
                        params = {
                            'chat_id': chat_id,
                            'text': f'Введите число n, а я посчитаю сумму 10^n единиц'
                            }
                        )
    else:
        n=int(text)
        result = await sum_n_ones(n)
        async with httpx.AsyncClient() as client:
            await client.get(f'https://api.telegram.org/bot{my_token}/sendMessage',
                        params = {
                            'chat_id': chat_id,
                            'text': f'Ответ: {result}'
                            }
                        )
    return message





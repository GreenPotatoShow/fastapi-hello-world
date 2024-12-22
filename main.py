import re
import httpx
from asyncio import create_task
from fastapi import FastAPI, Request

app = FastAPI()
my_token="7898884050:AAFkWzlGrlJ03pZ9dLUMh7nhZBR5xzucvWY"
tasks = {}


async def sum_n_ones(n):
    result=0
    for i in range(10**n):
        result+=1
    return result

async def send_message(chat_id, text):
    async with httpx.AsyncClient() as client:
        await client.get(f'https://api.telegram.org/bot{my_token}/sendMessage',
                    params = {
                        'chat_id': chat_id,
                        'text': text
                        }
                    )

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/bot/")
async def bot(request: Request):
    message = await request.json()
    chat_id=message["message"]["chat"]["id"]
    text=message["message"]["text"]
    if re.findall(r'\D', text):
        await send_message(chat_id,f'Введите число n, а я посчитаю сумму 10^n единиц')
    else:
        update_id=message["update_id"]
        n=int(text)
        tasks[update_id]=create_task(sum_n_ones(n))
        result = await tasks[update_id]
        await send_message(chat_id,f'Ответ: {result}')
        del tasks[update_id]
    return message


# @app.post("/bot/")
# async def bot(request: Request):
#     message = await request.json()
#     if "message" in message:
#         chat_id=message["message"]["chat"]["id"]
#         text=message["message"]["text"]
#         async with httpx.AsyncClient() as client:
#                 await client.get(f'https://api.telegram.org/bot{my_token}/sendMessage',
#                             params = {
#                                 'chat_id': chat_id,
#                                 'text': f'Введите число n, а я посчитаю сумму 10^n единиц'
#                                 }
#                             )
#     return message




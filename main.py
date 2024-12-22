import re
import httpx
from fastapi import FastAPI, Request
import asyncio

app = FastAPI()
my_token="7898884050:AAFkWzlGrlJ03pZ9dLUMh7nhZBR5xzucvWY"

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
    await send_message(chat_id,f'Введите число n, а я посчитаю сумму 10^n единиц')
#     if re.findall(r'\D', text):
#         await send_message(chat_id,f'Введите число n, а я посчитаю сумму 10^n единиц')
#     else:
#         asyncio.create_task(send_result(chat_id, int(text)))

#     return message

# async def send_result(chat_id, n):
#     await send_message(chat_id, 'Сейчас вычислю...')
#     result = await sum_n_ones(n)
#     await send_message(chat_id, f'Ответ: {result}')


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




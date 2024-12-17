import requests
#import time
from fastapi import FastAPI, Request

app = FastAPI()
my_token="7898884050:AAFkWzlGrlJ03pZ9dLUMh7nhZBR5xzucvWY"

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/bot")
async def bot(request: Request):
    if request.status_code==200:
        pass
        # message = await request.json()
        # requests.get(f'https://api.telegram.org/bot{my_token}/sendMessage',
        #                 params = {
        #                     'chat_id': message["message"]["chat"]["id"],
        #                     'text': f'Привет'
        #                     }
        #                 )
    return {"message": "agaga"}


# my_token="7898884050:AAFkWzlGrlJ03pZ9dLUMh7nhZBR5xzucvWY"
# prev_update_id=0

# while True:
#     source = requests.get(f'http://greenpotato.alwaysdata.net/')
#     if source.ok:
#         message=source.json()
#         #print(message["update_id"])
#         if "photo" in message['message']:
#             pic_path = requests.get(f'https://api.telegram.org/bot{my_token}/getFile', params={"file_id": message["message"]['photo'][-1]["file_id"]})
#             pic = requests.get(f'https://api.telegram.org/file/bot{my_token}/{pic_path.json()["result"]["file_path"]}')
#             width=message["message"]["photo"][-1]["width"]
#             height=message["message"]["photo"][-1]["height"]
#             image = Image.open(BytesIO(pic.content))     
#             image=image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
#             buffered = BytesIO()
#             image.save(buffered, format="PNG")
#             buffered.seek(0)  

#             requests.post(f'https://api.telegram.org/bot{my_token}/sendPhoto',
#                         params = {'chat_id': message["message"]["chat"]["id"]},
#                         files={'photo': buffered}
#                         )
#             print(pic)
#         elif "update_id" in message:
#             requests.get(f'https://api.telegram.org/bot{my_token}/sendMessage',
#                         params = {
#                             'chat_id': message["message"]["chat"]["id"],
#                             'text': f'Отправьте фото, оно будет отзеркалено'
#                             }
#                         )
#     time.sleep(0.1)





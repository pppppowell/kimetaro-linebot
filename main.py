from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
import random

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ[]
YOUR_CHANNEL_SECRET = os.environ[]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

start=False

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    #get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handler_message(event):
    global start
    global texts
    if (event.message.text == "決め太郎" and start==False):
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="なに"))
        start=True
    if (start == True):
        get_text(event.message.text)
    if (event.message.text == "決めて" and start == True):
        start = False
        rand = random.randrange(len(texts))
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="「"+texts[rand]+"」でええんちゃう！？！？"))
        texts=[]

def get_text(text):
    texts.append = text

if __name__ == "__main__":
# app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
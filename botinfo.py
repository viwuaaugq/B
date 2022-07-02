import requests
import telebot
from telebot import types
import flask
import logging
from flask import Flask,request
import os,sys,random
tk = "5553093456:AAHclqgIcNiyPPdkSHbdWNsVvAYWrAmIcQM"
bot = telebot.TeleBot(tk)

server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
def s(message):
    cc = types.InlineKeyboardMarkup()
    b = types.InlineKeyboardButton(text="معلومات التوكن",callback_data="bs")
    cc.add(b)
    bot.send_message(message.chat.id,"اهلا بك في بوت معلومات التوكن\nاضغط على زر معلومات التوكن\nوارسل توكنك للحصول على جميع المعلومات \nDev : @E_4_1",reply_markup=cc)

@bot.callback_query_handler(func=lambda m:True)
def s(call):
    if call.message:
        if call.data == "bs":
            bot.register_next_step_handler(call.message,mm)
            bot.send_message(call.message.chat.id,"ارسل التوكن الان :")
def mm(message):
    token = message.text
    try:
        url = "https://api.telegram.org/bot"+token+"/getme"
        uel = "https://api.telegram.org/bot"+token+"/getwebhookinfo"
        r = requests.get(url).json()
        re = requests.get(uel).json()
        usl = re['result']['url']
        idu = r['result']['id']
        fs = r['result']['first_name']
        us = r['result']['username']
        bot.send_message(message.chat.id,f"""
⌯ مـعـلـومـات الـتـوكـن :
━━━━━━━━━━━━━
• مـعـرف الـبـوت : @{us} ⭐
• ايـدي الـبـوت : {idu} ❄️
• اسـم الـبـوت : {fs} 🔥
• رابـط الـمـلـف : {usl}] ⚡
━━━━━━━━━━━━━
    """)
    except:
        bot.send_message(message.chat.id,"التوكن غلط")

@server.route(f"/{tk}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
  
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://tokeninfobot2.herokuapp.com/"+str(tk))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

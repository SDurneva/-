# -*- coding: utf-8 -*-
import flask
import telebot
import conf

#WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
#WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)

#bot.remove_webhook()

#bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

#app = flask.Flask(__name__)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Это бот, который считает, сколько слов в вашем сообщении.")


@bot.message_handler(func=lambda m: True)
def send_len(message):
    k = len(message.text.split())
    if str(k).endswith(str(1)):
        ending = 'о'
    elif str(k).endswith(str(2)) or str(k).endswith(str(3)) or str(k).endswith(str(4)):
        ending = 'а'
    else:
        ending = ''
    bot.send_message(message.chat.id, ('В вашем сообщении {} слов' + ending).format(k)


#@app.route('/', methods=['GET', 'HEAD'])
#def index():
#    return 'ok'

if __name__ == '__main__':
    bot.polling(none_stop=True)
#@app.route(WEBHOOK_URL_PATH, methods=['POST'])
#def webhook():
#    if flask.request.headers.get('content-type') == 'application/json':
#        json_string = flask.request.get_data().decode('utf-8')
#        update = telebot.types.Update.de_json(json_string)
#        bot.process_new_updates([update])
#        return ''
#    else:
#        flask.abort(403)

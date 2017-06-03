# -*- coding: utf-8 -*-
import flask
import telebot
import conf
import pymorphy2
import random
import json

morph = pymorphy2.MorphAnalyzer()

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)

bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Это бот, который меняет ваши сообщения до неузнаваемости, заменяя "
                                      "ваши слова на слова из \"Мастер и Маргарита\".")


@bot.message_handler(func=lambda m: True)
def send_len(message):
    mess = message.text
    mess1 = mess.split()
    mess2 = []
    for word in mess1:
        word = word.strip('.,!?():;–«»…[]“„…—№')
        mess2.append(word)
    allwords = json.loads(open('words.json', 'r', encoding='utf-8').read())
    new_words = []
    for word in mess2:
        if {'NOUN', 'masc'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[0])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.number, tags.case})
            new_words.append(new_word.word)
        elif {'NOUN', 'femn'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[1])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.number, tags.case})
            new_words.append(new_word.word)
        elif {'NOUN', 'neut'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[2])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.number, tags.case})
            new_words.append(new_word.word)
        elif {'ADJF'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[3])
            tags = morph.parse(word)[0].tag
            if 'sing' in tags:
                new_word = morph.parse(w)[0].inflect({tags.number, tags.case, tags.gender})
            else:
                new_word = morph.parse(w)[0].inflect({tags.number, tags.case})
            new_words.append(new_word.word)
        elif {'ADJS'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[3])
            tags = morph.parse(word)[0].tag
            if 'sing' in tags:
                new_word = morph.parse(w)[0].inflect({tags.POS, tags.number, tags.gender})
            else:
                new_word = morph.parse(w)[0].inflect({tags.POS, tags.number})
            new_words.append(new_word.word)
        elif {'COMP'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[3])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.POS})
            new_words.append(new_word.word)
        elif {'INFN', 'perf', 'intr'} in (morph.parse(word)[0]).tag:
            new_word = random.choice(allwords[4])
            new_words.append(new_word)
        elif {'INFN', 'perf', 'tran'} in (morph.parse(word)[0]).tag:
            new_word = random.choice(allwords[5])
            new_words.append(new_word)
        elif {'INFN', 'impf', 'intr'} in (morph.parse(word)[0]).tag:
            new_word = random.choice(allwords[6])
            new_words.append(new_word)
        elif {'INFN', 'impf', 'tran'} in (morph.parse(word)[0]).tag:
            new_word = random.choice(allwords[7])
            new_words.append(new_word)
        elif {'VERB', 'perf', 'intr'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[4])
            tags = morph.parse(word)[0].tag
            if 'past' in tags:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.gender, tags.mood})
            elif 'pres' in tags:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.person, tags.mood})
            elif 'impr' in tags:
                new_word = morph.parse(w)[0].inflect({tags.number, tags.mood})
            else:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.mood})
            new_words.append(new_word.word)
        elif {'VERB', 'perf', 'tran'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[5])
            tags = morph.parse(word)[0].tag
            if 'past' in tags:
                if 'sing' in tags:
                    new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.gender, tags.mood})
                else:
                    new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.mood})
            elif 'pres' in tags:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.person, tags.mood})
            elif 'impr' in tags:
                new_word = morph.parse(w)[0].inflect({tags.number, tags.mood})
            else:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.mood})
            new_words.append(new_word.word)
        elif {'VERB', 'impf', 'intr'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[6])
            tags = morph.parse(word)[0].tag
            if 'past' in tags:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.gender, tags.mood})
            elif 'pres' in tags:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.person, tags.mood})
            elif 'impr' in tags:
                new_word = morph.parse(w)[0].inflect({tags.number, tags.mood})
            elif morph.parse(word)[0].normal_form == 'быть':
                new_word = morph.parse(word)[0]
            else:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.mood, tags.person})
            new_words.append(new_word.word)
        elif {'VERB', 'impf', 'tran'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[7])
            tags = morph.parse(word)[0].tag
            if 'past' in tags:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.gender, tags.mood})
            elif 'pres' in tags:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.person, tags.mood})
            elif 'impr' in tags:
                new_word = morph.parse(w)[0].inflect({tags.number, tags.mood})
            elif morph.parse(word)[0].normal_form == 'иметь':
                new_word = morph.parse(word)[0]
            else:
                new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.mood})
            new_words.append(new_word.word)
        elif {'PRTF', 'pssv'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[8])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.gender, tags.case})
            new_words.append(new_word.word)
        elif {'PRTF', 'actv', 'intr'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[9])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.gender, tags.case})
            new_words.append(new_word.word)
        elif {'PRTF', 'actv', 'tran'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[10])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.gender, tags.case})
            new_words.append(new_word.word)
        elif {'PRTS'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[5])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.tense, tags.number, tags.gender})
            new_words.append(new_word.word)
        elif {'GRND', 'perf', 'intr'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[4])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.tense})
            new_words.append(new_word.word)
        elif {'GRND', 'perf', 'tran'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[5])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.tense})
            new_words.append(new_word.word)
        elif {'GRND', 'impf', 'intr'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[6])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.tense})
            new_words.append(new_word.word)
        elif {'GRND', 'impf', 'tran'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[7])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.tense})
            new_words.append(new_word.word)
        elif {'NUMR'} in (morph.parse(word)[0]).tag:
            w = random.choice(allwords[11])
            tags = morph.parse(word)[0].tag
            new_word = morph.parse(w)[0].inflect({tags.case})
            new_words.append(new_word.word)
        elif {'ADVB'} in (morph.parse(word)[0]).tag:
            new_word = random.choice(allwords[12])
            new_words.append(new_word)
        elif {'NPRO'} in (morph.parse(word)[0]).tag:
            new_word = word
            new_words.append(new_word)
        elif {'PRED'} in (morph.parse(word)[0]).tag:
            new_word = random.choice(allwords[14])
            new_words.append(new_word)
        elif {'CONJ'} in (morph.parse(word)[0]).tag:
            new_word = random.choice(allwords[15])
            new_words.append(new_word)
        elif {'PRCL'} in (morph.parse(word)[0]).tag:
            new_word = random.choice(allwords[16])
            new_words.append(new_word)
        elif {'INTJ'} in (morph.parse(word)[0]).tag:
            new_word = random.choice(allwords[17])
            new_words.append(new_word)
        else:
            new_word = word
            new_words.append(new_word)
    pairs = dict(zip(mess2, new_words))
    for key in pairs:
        mess = mess.replace(key, pairs[key]).capitalize()
    bot.send_message(message.chat.id, mess)


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'

if __name__ == '__main__':
    bot.polling(none_stop=True)
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)
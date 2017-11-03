from telegram.ext import Updater, MessageHandler, Filters 
from telegram import Update
from multiprocessing import Process
from flask import Flask
from flask import request
from dialog import dialog
import json
import os

def handleTelegramMessage(bot, update):
	byte_data = dialog(update.message.text)
	string_data = byte_data.decode(encoding='utf-8')
	update.message.reply_text(string_data)

def pollForTelegram():
	updater = Updater('460893798:AAFeyxyeakEO4soBpw4hWLyiXNGkj865dkU')
	updater.dispatcher.add_handler(MessageHandler(Filters.text, handleTelegramMessage))
	updater.start_polling()
	updater.idle()

app = Flask(__name__)
@app.route('/')
def homepage():
	text = u'Hello, world!'
	target = 'ru'
	translation = translate_client.translate(text, target_language=target)
	return u'Text: {}'.format(text) + u'Translation: {}'.format(translation['translatedText'])

@app.route('/translate', methods=['POST'])
def translate():
	target = 'en'
	raw_message = request.data.decode(encoding='utf-8')
	message = json.loads(raw_message)
	byte_data = dialog(message.raw_message)
	string_data = byte_data.decode(encoding='utf-8')
	return string_data

if __name__ == '__main__':
	# p2 = Process(target=pollForTelegram)
	# p2.start()

	p1 = Process(target=app.run(debug=True, use_reloader=True))
	p1.start()

	p1.join()
	# p2.join()



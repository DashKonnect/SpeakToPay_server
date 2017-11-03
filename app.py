from flask import Flask
from flask import request
from dialog import dialog
import json
import os

app = Flask(__name__)
@app.route('/')
def homepage():
	text = u'Hello, world!'
	target = 'ru'
	translation = translate_client.translate(text, target_language=target)
	return u'Text: {}'.format(text) + u'Translation: {}'.format(translation['translatedText'])

@app.route('/translater', methods=['POST'])
def translater():
	target = 'en'
	raw_message = request.data.decode(encoding='utf-8')
	return dialog(raw_message)
	

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)


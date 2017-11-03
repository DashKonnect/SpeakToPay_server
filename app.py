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

@app.route('/translate', methods=['POST'])
def translate():
	target = 'en'
	final = []
	raw_message = request.data.decode(encoding='utf-8')
	byte_data = dialog(raw_message)
	string_data = byte_data.decode(encoding='utf-8')
	return string_data
	
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)


from flask import Flask
from flask import request
from google.cloud import translate
import json
import os

app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./SpeakToPay-696d8f6e86f0.json"
translate_client = translate.Client()

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
	translation = translate_client.translate(raw_message,target_language=target)
	return json.dumps(translation)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)


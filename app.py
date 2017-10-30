from flask import Flask
from google.cloud import translate
import os

app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./SpeakToPay-696d8f6e86f0.json"
@app.route('/')
def homepage():
    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = u'Hello, world!'
    # The target language
    target = 'ru'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    return u'Text: {}'.format(text) + u'Translation: {}'.format(translation['translatedText'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


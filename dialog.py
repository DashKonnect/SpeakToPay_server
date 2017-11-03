from google.cloud import translate
import apiai
import os
import json


CLIENT_ACCESS_TOKEN = '7ff3c98a51fd4664be02a6ec78b52a79'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./SpeakToPay-696d8f6e86f0.json"
translate_client = translate.Client()
target = 'en'
def dialog(raw_message):

	src_lang = translate_client.detect_language(raw_message);
	translation = translate_client.translate(raw_message,target_language=target)
	ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
	req = ai.text_request()
	req.lang = 'en'  # optional, default value equal 'en'
	req.session_id = "1234"
	text = translation['translatedText']
	text = text.lower()
	for i in range(len(text)):
		if text[i] == '₹':
			text = text[:i]+"rupees "+text[i+1:]

	req.query = text
	response = req.getresponse()
	# return response.read()
	string_data = response.read()
	obj = json.loads(string_data.decode());
	message = obj["result"]["fulfillment"]["speech"]
	translation = translate_client.translate(message,target_language=src_lang['language'])
	return translation['translatedText']

# dialog("शाहरुख को ₹50 भेज द")
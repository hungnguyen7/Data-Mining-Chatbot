import requests
import json
import speech_recognition as sr
from speechToText import speechToText_EN
from textToSpeech import textToSpeech_EN
from types import SimpleNamespace
# sender=input('What is your name?\n')
bot_message=''
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        ques=speechToText_EN()
        # print(ques)
    if len(ques)==0:
        # print('I can\'t hear anything')
        continue
    print('Sending question to chatbot...')
    # print(ques)
    response = requests.post('http://localhost:5002/webhooks/rest/webhook', json={'message': ques})
    # print(response.json())
    data=response.json()
    #Chi tra loi text, khong doc
    bot_message=data[0]['text']
    textToSpeech_EN(bot_message)
    # say bye or stop to stop chat
    if(ques=='bye' or ques=='stop'):
        break
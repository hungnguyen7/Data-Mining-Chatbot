import requests
import json
import speech_recognition as sr
from speechToText import speechToText_EN
from textToSpeech import textToSpeech_EN
from types import SimpleNamespace
# sender=input('What is your name?\n')
bot_message=''
r = sr.Recognizer()
while bot_message !='Bye' or bot_message!='thanks':
    with sr.Microphone() as source:
        ques=speechToText_EN()
        # print(ques)
    if len(ques)==0:
        print('I can\'t hear anything')
        continue
    print('Sending question to chatbot...')

    response = requests.post('http://localhost:5002/webhooks/rest/webhook', json={'message': ques})
    print(response.json())
    data=json.loads(response.json(), object_hook= lambda d: SimpleNamespace(**d))
    print('Bot says: ', end=' ')
    for i in data:
        print(type(i))
    
    textToSpeech_EN(bot_message) 
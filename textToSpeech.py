from gtts import gTTS
import playsound
import requests
import urllib.request
import os
import time
def textToSpeech_EN(text):
    output=gTTS(text, lang='en', slow=False)
    output.save('output.mp3')
    playsound.playsound('output.mp3', True)

def textToSpeech_VI(text):
    url = 'https://api.fpt.ai/hmi/tts/v5'
    payload = text
    headers = {
        'api-key': 'Vp7RiN2kg6HyHie7sjIRq9qIZHaD57sE',
        'speed': '',
        'voice': 'banmai'
    }

    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
    print(response.text)
    response=response.json()
    link_mp3=response['async']
    return link_mp3

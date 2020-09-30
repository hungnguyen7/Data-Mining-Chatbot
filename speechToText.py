import speech_recognition as sr
import pyaudio
r=sr.Recognizer()
def speechToText_VI():
    with sr.Microphone() as source:
        print('Mời bạn nói:')
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio, language='vi_VI')
            print('Bạn đã nói: {}'.format(text))
        except:
            print('Xin lỗi! tôi không nhận được giọng nói của bạn')
    return text

def speechToText_EN():
    text=''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Ask me something...')
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio, language='en_EN')
            print('You said: {}'.format(text))
        except:
            print('Sorry i could not recognize your voice')
    return text


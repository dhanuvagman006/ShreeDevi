import pyttsx3

def init_speaker():
    speak = pyttsx3.init()
    voices = speak.getProperty('voices')
    speak.setProperty('rate', 160)
    speak.setProperty('volume', 0.9)
    speak.setProperty('voice', voices[1].id)
    return speak

def speakfun(speak, text):
    speak.say(text)
    speak.runAndWait()

speak = init_speaker()
speakfun(speak, "Hello, how can I assist you?")

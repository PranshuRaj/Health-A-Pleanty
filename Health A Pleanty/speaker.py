import pyttsx3


def speak(string):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 175)
    engine.setProperty('voice', voices[1].id)
    engine.say(string)
    engine.runAndWait()
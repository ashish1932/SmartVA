import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"🤖 AARYA: {text}")
    engine.say(text)
    engine.runAndWait()

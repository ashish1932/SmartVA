import datetime
import pyjokes

def get_reply(command):
    if "time" in command:
        return "The time is " + datetime.datetime.now().strftime("%I:%M %p")
    elif "joke" in command:
        return pyjokes.get_joke()
    elif "hello" in command:
        return "Hello! I’m AARYA. How can I assist you today?"
    elif "exit" in command or "goodbye" in command:
        return "Goodbye! See you soon."
    else:
        return "I'm still learning that feature."

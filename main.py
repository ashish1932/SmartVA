from assistant.voice_recognition import listen_command
from assistant.text_to_speech import speak
from assistant.basic_reply import get_reply

def run_assistant():
    speak("AARYA initialized. Awaiting your command.")
    while True:
        command = listen_command()
        reply = get_reply(command)
        speak(reply)
        if "exit" in command or "goodbye" in command:
            break

if __name__ == "__main__":
    run_assistant()

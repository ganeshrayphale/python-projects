import speech_recognition as sr
import webbrowser
import pyttsx3
import time

recognizer = sr.Recognizer()  # Create recognizer once
engine = pyttsx3.init()       # Create engine once

def speak(text):
    engine.say(text)
    engine.runAndWait()

def Process_command(command):
    print(f"Processing command: {command}")
    # Example of processing: open a website
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif "open instagram" in command.lower():
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    else:
        speak("Sorry, I did not understand the command.")

def listen_for_wake_word():
    print("Listening for wake word 'Jarvis'...")
    with sr.Microphone() as source:
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)  # Increase timeout to 10 seconds
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            if "jarvis" in command.lower():
                return True
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
        except sr.RequestError as e:
            print(f"Request error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return False

def listen_for_command():
    print("Listening for command...")
    with sr.Microphone() as source:
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)  # Increase timeout to 10 seconds
        try:
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand the command.")
        except sr.RequestError as e:
            print(f"Request error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return ""

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        if listen_for_wake_word():
            speak("Yes sir, how can I help you?")
            command = listen_for_command()

            if command:
                Process_command(command)
            else:
                speak("I did not hear any command.")
        else:
            print("Still listening for wake word...")  # For debugging

        # Delay to prevent 100% CPU usage
        time.sleep(1)

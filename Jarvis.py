import os
import threading
import speech_recognition as sr
import pyttsx3
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, phrase_time_limit=5)
    try:
        return r.recognize_google(audio).lower().strip()
    except:
        return ""


def open_calculator():
    os.system("calc")

def open_browser():
    os.system("start chrome")

def greet():
    speak("Hello, sir")

def time_reply():
    speak("I will tell time later")

def open_whatsapp():
    os.system("start whatsapp:")

def open_notepad():
    os.system("start notepad")

def open_vscode():
    os.system("start vscode:")

def open_terminal():
    os.system("start powershell")


WAKE_WORDS = ["jarvis", "hey jarvis"]
SLEEP_WORDS = ["bye", "ok bye", "goodbye"]
EXIT_WORDS  = ["exit", "quit", "stop jarvis"]

active = False
running = True


def jarvis_loop():
    global active, running
    speak("Jarvis is running in background")

    while running:
        command = listen()
        if not command:
            continue

     
        if any(w in command for w in EXIT_WORDS):
            speak("Shutting down")
            running = False
            break

        
        if active and any(w in command for w in SLEEP_WORDS):
            speak("Going to sleep")
            active = False
            continue

        if not active and any(w in command for w in WAKE_WORDS):
            speak("Yes?")
            active = True
            continue

        if not active:
            continue

        
        if "hello" in command or "hi" in command:
            greet()
        elif "time" in command:
            time_reply()
        elif "calculator" in command:
            open_calculator()
        elif "chrome" in command or "browser" in command:
            open_browser()
        elif "open whatsapp"in command:
            open_whatsapp()
        elif "open notepad"in command:
            open_notepad()
        elif "open vscode"in command:
            open_vscode()
        elif "open terminal" in command or "open powershell" in command:
            open_terminal()
        else:
            speak("Command not found")


def create_image():
    image = Image.new("RGB", (64, 64), "black")
    draw = ImageDraw.Draw(image)
    draw.text((10, 20), "J", fill="white")
    return image

def on_wake(icon, item):
    global active
    active = True
    speak("Yes?")

def on_exit(icon, item):
    global running
    running = False
    speak("Shutting down")
    icon.stop()

def tray_icon():
    menu = (
        item("Wake Jarvis", on_wake),
        item("Exit", on_exit)
    )
    icon = pystray.Icon("Jarvis", create_image(), "Jarvis Assistant", menu)
    icon.run()

threading.Thread(target=jarvis_loop, daemon=True).start()
tray_icon()

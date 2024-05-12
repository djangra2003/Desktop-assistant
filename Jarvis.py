import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import cv2
import pyautogui
import time
import requests
import sys
import operator
import urllib.parse
import random
import pyscreenshot

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Please tell me how may I help you sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Dobara bol bhai")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            print("Yes Sir")
            speak("Yes Sir")

        elif "who are you" in query:
            print("I am Jarvis")
            speak("I am Jarvis")
            print("I do everything my creator tells me ")
            speak("I do everything my creator tells me ")

        elif "who created you" in query:
            print("DJ ")
            speak("DJ")

        elif "what is" in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif ' open google' in query:
            webbrowser.open("google.com")

        elif 'search on google' in query:
            speak('what should i search')
            qry = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={qry}")
            result = wikipedia.summary(query, sentences=1)
            speak(result)


        elif ' youtube chla' in query:
            url = "youtube.com"
            webbrowser.open_new(url)

        elif 'open youtube' in query:
            speak("what should i search")
            qrry=takeCommand().lower()
            wk.playonyt(f"{qrry}")

        elif 'search on youtube' in query:
            query = query.replace("search on youtube","")
            encoded_query = urllib.parse.quote_plus(query)
            url = f"https://www.youtube.com/results?search_query={encoded_query}"
            webbrowser.open(url)

        
        elif "open brave" in query:
            npath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
            os.startfile(npath)

        elif 'close brave' in query:
            os.system("taskkill /f /im brave.exe")

        elif ' open shopping' in query:
            webbrowser.open('www.amazon.in')
            speak('sir I am opening amazon so you can shop whatever you want')

        elif ' take screenshot' in query:
            speak('tell the name of the file')
            name=takeCommand().lower()
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak('screenshot saved sir')

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'close command prompt' in query:
            os.system("taskkill /f /im cmd.exe")

        elif 'shut down the system' in query:
            os.system("shutdown /s/t 5")

        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(20)
                if k==15:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'increase volume' in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif 'decrease volume' in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif 'open notepad and write the notes' in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('notepad')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write('Here are the notes sir',interval=0.1)    

        elif 'open new tab' in query:
            pyautogui.hotkey('ctrl','n')

        elif 'close  tab' in query:
            pyautogui.hotkey('ctrl','w')

        elif 'open icognito tab' in query:
            pyautogui.hotkey('ctrl','shift','n') 

        elif 'minimize  window' in query:
            pyautogui.hotkey('alt','space')
            time.sleep(1)
            pyautogui.press('n')

        elif 'change  tab' in query:
            pyautogui.hotkey('ctrl','tab')

        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl','shift','tab')

        elif 'open history' in query:
            pyautogui.hotkey('ctrl','h')


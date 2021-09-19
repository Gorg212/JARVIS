#! python3.6
import os
import speech_recognition as sr
import pyautogui as p 
import time
import pyttsx3

# tts stuff
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)
engine.setProperty('rate', 180)
# engine.say("Hello, How are you ?")
engine.runAndWait()

def speak(str):
    engine.say(str)
    engine.runAndWait()

speak("Greetings master, how ,may I help you?")

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Speak Anything :")
#     audio = r.listen(source)

#------------------------------------------------------------

#big commands

    
#-------------------------------------------------------------
#main code 

while 1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSpeak Anything :")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"you said: {text}")

        if text == "stop" or text == "bye" or text == "exit" or text == "shut down":
            print("\n\nShutting down")
            speak("Bye have a good day!")
            break

        else:
            if "help" in text:
                speak("I can Do speech to text, and talk with you, also you can search google and open app from me, just ask me to open Chrome or Try converting speech to text, by saying type then your text. Example Type hello world")

            elif text == "hello" or text == "hai" or text == "hi":
                print("Hi! how are you?")
                speak("Hi! how are you?")
                continue

            elif text == "I am fine" or text == "I am fine what about you" or text == "I am fine how about you":
                speak("I'm also fine")
                print("I'm also fine")
                continue
            
            elif text == "hi how are you" or text == "How are you":
                speak("I'm fine")
                print("I'm fine")
                continue

            elif "type" in text:
                # SpeechToText()
                text = text.replace("type", "")
                speak("Typing text in 3 seconds...")
                print("Typing text in 3 seconds...")
                time.sleep(3)
                p.typewrite(text)
                continue

            elif 'open' in text:
                if 'Chrome' in text:
                    print("Opening chrome")
                    speak("Opening chrome")
                    path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(path)

                if 'Firefox' in text:
                    print("Opening Firefox")
                    speak("Opening Firefox")
                    path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                    os.startfile(path)
                
                if 'Teams' or 'Team' in text:
                    print("Opening Teams")
                    speak("Opening Teams.")
                    path = "C:\\Users\\Gorg\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
                    os.startfile(path)

                if 'Discord' in text:
                    print("Opening Discord")
                    speak("Opening Discord")
                    path = "C:\\Users\\Gorg\\AppData\\Local\\Discord\\app-1.0.9002\\Discord.exe"
                    os.startfile(path)
            
            else:
                print("I'm not sure I understand") 
                speak("I'm not sure I understand")      
                continue


        
    except:
        print("\nWaiting for your response")
        
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

        if text == "stop" or text == "bye" or text == "exit":
            print("\n\nShutting down")
            speak("Bye have a good day!")
            break

        else:

            if text == "hello" or text == "hai" or text == "hi":
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
                
                elif 'Teams' in text:
                    print("Feature hasn't been implemented yet")
                    speak("Feature hasn't been implemented yet.")

            
            else:
                print("I'm not sure I understand") 
                speak("I'm not sure I understand")      
                continue


        
    except:
        print("\nWaiting for your response")
        
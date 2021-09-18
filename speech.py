#! python3.6
import speech_recognition as sr
import pyautogui as p 
import time
import pyttsx3

# tts stuff
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
engine.setProperty('rate', 150)
# engine.say("Hello, How are you ?")
engine.runAndWait()

def speak(str):
    engine.say(str)
    engine.runAndWait()

speak("Hello, What's going on")

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Speak Anything :")
#     audio = r.listen(source)

#------------------------------------------------------------

#big commands

def SpeechToText():
    STT = sr.Recognizer()
    with sr.Microphone() as source:
        print("What do you want to convert to text?")
        speak("What do you want to convert to text?")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"you said: {text}")
            print("Typing test in 3 secs")
            speak("Typing test in 3 secs")
            time.sleep(3)
            p.typewrite(text)
        except:
            print("did not hear you")
            speak("did not hear you")
    
#-------------------------------------------------------------
#main code 

while 1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"you said: {text}")

        if text == "bye":
            print("\n\nShutting down")
            speak("Bye have a good day!")
            break

        else:
            if text == "hello":
                print("Hi! how are you?")
                speak("Hi! how are you?")
                continue

            elif text == "type":
                SpeechToText()
                continue

            else:
                print("I could not understand you")       
                continue


        
    except:
        print("\n\nSorry could not recognize what you said")
        
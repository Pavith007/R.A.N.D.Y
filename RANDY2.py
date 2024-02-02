import pyttsx3
import speech_recognition as sr
import datetime
import os

Engine = pyttsx3.init('sapi5')
voices= Engine.getProperty('voices')
Engine.setProperty('voices',voices[0].id)

def Speech(audio):
    Engine.say(audio)
    Engine.runAndWait()

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...Boss")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        Speech(f"User said: {query}\n")
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)    
        Speech("Pardon plzz.....")
        print("Pardon plzz.....")  
        return "None"
     
    return query
def Greeting():
    Hour = int(datetime.datetime.now().hour)
    if Hour>=0 and Hour<=12:
        print("Good Morning my King")
        Speech("Good Morning my king")
    elif Hour>12 and Hour<=4 :
        print("Good Afternoon my king")
        Speech("Good Afternoon my king")
    elif Hour>4 and Hour<=7:
        print("Good Evening my king")
        Speech("Good Evening my king")
    else:
        print("Good Night my king")
        Speech("Good Night my king")
        
if __name__=="__main__":
    Greeting()
    query=takeCommand()
    if 'time' in query:
        Strtime = datetime.datetime.now().strftime("%H:%M:%S")
        print(Strtime)
        Speech(f"Sire,the time is {Strtime}")
        

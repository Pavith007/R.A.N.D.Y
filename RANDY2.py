import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes
import webbrowser
import openai

openai.api_key= "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"

Engine = pyttsx3.init('sapi5')
voices= Engine.getProperty('voices')
Engine.setProperty('voices',voices[0].id)

def chat_gpt(prompt):
    response = openai.Completions.create(
    model="text-davinci-003"
    prompt=prompt,
    max_tokens=4000,
    n=1,
    stop=None,
    temperature=0.5,
    )
    return response["choices"][0]["text"]

def Speech(audio):
    Engine.say(audio)
    Engine.runAndWait()

def takeCommand():
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
         
        print("Listening...Boss")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=0.5)
        audio = r.listen(source)
        print("Wait a few minitues boss")
  
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
        print("Good Morning sir")
        Speech("Good Morning sir")
    elif Hour>12 and Hour<=16 :
        print("Good Afternoon sir")
        Speech("Good Afternoon sir")
    elif Hour>16 and Hour<=19:
        print("Good Evening sir")
        Speech("Good Evening sir")
    else:
        print("Good Night sir")
        Speech("Good Night sir")
def WakeUpCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         
        print("R.A.N.D.Y is Sleeping")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        query="none"
    return query



if __name__=="__main__":
    while True:
        query=WakeUpCommand().lower()
        if 'wake up' in query:
            Greeting() 
            Speech("Yes Sir ")
            while True:
                query=takeCommand().lower()
                if 'time' in query:
                    Strtime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(Strtime)
                    Speech(f"Sire,the time is {Strtime}")
                elif 'randy' in query:
                    Speech("Yes boss")
                    
                elif 'open edge' in query:
                    Speech("Opening the Edge...")
                    os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                elif 'wikipedia' in query:
                    Speech("Searching in wikipedia....")
                    try:
                        query=query.replace("wikipedia","")
                        results = wikipedia.summary(query,sentences=2)
                        Speech("Accoring to Wikipedia , ")
                        print(results)
                        Speech(results)
                    except:
                        Speech("No information found...")
                        print("No information found...") 
                elif 'play' in query:
                    query=query.replace('play','')
                    Speech('Playing the video' + query)
                    pywhatkit.playonyt(query)
                elif 'type' in query:
                    Speech("plzz tell me What should i write boss")
                    while True:
                        InNotepad=takeCommand()
                        if InNotepad=='exit':
                            Speech("Done sir")
                        else:
                            pyautogui.write(InNotepad)
                elif 'joke' in query:
                    joke=pyjokes.get_joke()
                    Speech(joke)
                    print(joke)
                elif 'Google' in query:
                    Speech("Opeing Google Sir...")
                    webbrowser.open("www.google.com")
                elif 'sleep' in query:
                    Speech("I am leaving sir, Bye!")
                    quit()
                    #make OpenAI /Whatapp Accesss / Google access ? Youtube / Hotkeys
                    #bug in wikipedia

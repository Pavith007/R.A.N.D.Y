import pyttsx3
import speech_recognition as sr

Engine = pyttsx3.init('sapi5')
voices= Engine.getProperty('voices')
Engine.setProperty('voices',voices[0].id)

def Speech(audio):
    Engine.say(audio)
    Engine.runAndWait()

def Orders():
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print("How can I help You...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(Source,duration=1)
        audio = r.listen(Source)
        
    try:
        print("Plz Wait...")
        query = r.recognize_google_cloud(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print(e)
        Speech("PARDON PLZ....")
        query="none"
    return query
query=Orders().lower()  
    

from playsound import playsound
import speech_recognition as sr
import subprocess
import time
import pyttsx3
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


assistantName = "jarvis"
assistantName = assistantName.lower()
r = sr.Recognizer()

operations = ["Open url", "fart"]
acrobatPath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def processOnCommand(command):
    if "url" in command:
        rawUrl = command.split("url", 1)[1]
        theurl = rawUrl.replace(" ", "")
        finalurl = theurl
        print("Opening..."+finalurl)
        speak("Opening..."+finalurl)
        webbrowser.open_new(finalurl)
    elif "fart" in command or "unleash the" in command:
        print("Unleashing the fart...")
        speak("Unleashing the fart...")
        playsound('fart-01.mp3')
        myInit()
    elif "search" in command or "google search" in command:
        searchQuery = command.split("search", 1)[1]
        print("Starting Search for..."+searchQuery)
        speak("Starting Search for..."+searchQuery)
        finalUrl = "google.co.in/search?q="+searchQuery
        finalUrl = finalUrl.replace(" ", "", 1)
        finalUrl = finalUrl.replace(" ", "+")
        subprocess.Popen("%s %s" % (acrobatPath, finalUrl))
    else:
        print("-------- I am currently in development state! You can command me following things-------- ")
        speak("I am currently in development state! You can command me following things")
        print(operations)

        
        
    
def startListening(source):
    print("I am Listening...")
    audio = r.listen(source, 5, 5)
  
    try:
        print(">")
        text = r.recognize_google(audio)
        text = format(text).lower()
    
        if text==assistantName:
            print("Yes sir, how may i help you?")
            speak("Yes sir, how may i help you?")
        elif assistantName in text:
            processOnCommand(text)
            # print(text)
        elif "stop" in text:
            print("Ok See you later!")
            speak("Ok See you later!")
        else:
            print(text)
            startListening(source)
    except:
        print("!")
        startListening(source)
        
def myInit():
    with sr.Microphone() as source:
        startListening(source)

myInit()
# processOnCommand("hey vishal unleash the fart")

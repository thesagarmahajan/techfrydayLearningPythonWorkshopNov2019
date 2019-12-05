import speech_recognition as sr
import webbrowser
import subprocess

r = sr.Recognizer()

def processing(text):
    if "calculate love between" in text:
        str1 = text.split("between")
        str2 = str1[1]
        names = str2.split("and")
        boyname, girlname = names[0],names[1]
        if len(boyname) is len(girlname):
            print("congratulations sabka katega")
        elif len(boyname) > len(girlname):
            print("bakra halal")
        elif len(girlname) > len(boyname):
            print("dhokebaaz")
    elif "write" in text:
        new1 = text.replace("write","",1)
        parts = new1.split("into")
        myfile=open(parts[1] +".txt","w+")
        myfile.write(parts[0])
        myfile.close()      
    elif "open url" in text:
        words = text.split("url ")
        final_url=words[1].replace(" ","")
        print(final_url)
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        subprocess.Popen("%s %s" % (chrome_path, final_url))

def listen():
    print("I am listening...")
    with sr.Microphone() as source:
        audio = r.listen(source, 10, 5)
        print("Audio heard.")
        text = r.recognize_google(audio)
        text = format(text).lower()
        processing(text)
        
listen()


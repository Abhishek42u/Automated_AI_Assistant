import pyttsx3,time
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import datetime


#from engine import Engine
p = pyttsx3.init()
voices = p.getProperty('voices')
p.setProperty('voice',voices[1].id)
#print(voices[1].id)
p.setProperty('rate',150)
t=datetime.datetime.now().strftime("%H:%M:%S")
p.say("Current time is")
p.say(t)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)     
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        speak(query)
    except Exception as e:
        print(e)
        speak("Unable to recognize sir")
        return "None"
    return query

def voicechange():
    voice = engine.getProperty('voices')
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    newVoiceRate = 170
    engine.setProperty('rate',newVoiceRate)

def tell():
    speak("Aapki kya hukum hain mere aaka?")


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():
    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day
    speak("The present day is {} and the month is {} and the year is {}".format(Day,Month,Year)) 

def sendemail(to = "cse2019109@rcciit.org.in", content = "Mail from Python"):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("athakur42u@gmail.com","CSE2019/109")
    server.sendmail("athakur42u@gmail.com",to,content)
    server.close()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        speak(query)

    except Exception as e:
        print(e)
        speak("Unable to recognize sir")
        return "None"

    return query

def speak(audio):
    p.say(audio)

    
voicechange()
tell()

if __name__=="__main__":
    while(true):
        
        query = takecommand().lower()
        
        if "date" in query:
            date()

        elif "time" in query:
            time()
        
        elif "virat" in query:
            i=0
            while(i<2):
                if i==0:
                    speak("Give your best today and you won't regret tomorrow")
                    #time.sleep(.01)
                elif (i==1):
                    speak("I repeat, Give your best today and you won't regret tomorrow")
                i=i+1
            time.sleep(.001)

        elif "email" in query:
            speak("Please tell the content of email?")    
            result = takecommand().lower()
            sendemail(content = result)
            speak("Email sent successfully")

        elif "exit" in query:
            break  

        else:
            speak("Sorry! Could you please repeat again?")

    p.runAndWait()


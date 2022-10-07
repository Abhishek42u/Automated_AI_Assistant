import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import contact
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) #where 0 indicatees male voice and 1 indicates female voice
engine.setProperty('voice', voices[1].id)


# defining speak function which takes string as input to speak it out during execution
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Defining wishme function to wish the user at the start of the program
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        print("Hi , very Good Morning ! \n")
        speak("Hi , very Good Morning !")
    elif hour >= 12 and hour <= 17:
        print("Hi , very Good Afternoon ! \n")
        speak("Hi , very Good Afternoon !")
    elif hour >= 17 and hour <= 21:
        print("Hi , very Good Evening ! \n")
        speak("Hi , very Good Evening !")
    else:
        pass
    speak("I'm Sona , your virtual assistant. How may I help you...")


# Defining take command function for taking input from your microphone
def takeCommand():
    # It takes microphone input of the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...\n")
        return "None"
    return query


# All activites are given here inside main
if __name__ == "__main__":
    wishMe()  # calling your wishme function

    if(1):
        # Taking command from user and converting it to lowercase
        query = takeCommand().lower()

        # logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            # Total no.of sentences to read out
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube, here you go...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Redirecting you to google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Redirecting you to satckoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open amazon' in query:
            speak("Opening Amazon, here you go...")
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            speak("Opening Flipkart, here you go...")
            webbrowser.open("flipkart.com")

        elif 'open instagram' in query:
            speak("Opening Instagram, here you go...")
            webbrowser.open("instagram.com")

        elif 'open geeksforgeeks' in query:
            speak("Redirecting you to geeksforgeeks")
            webbrowser.open("geeksforgeeks.org")

        elif 'open hackerrank' in query:
            speak("Redirecting you to Hackerrank")
            webbrowser.open("hackerrank.com")

        elif 'open github' in query:
            speak("Opening Github")
            webbrowser.open("github.com")

        elif 'open meet' in query:
            speak("Opening Google Meet")
            webbrowser.open("meet.com")

        elif 'open zoom' in query:
            speak("Opening Zoom Meeting")
            webbrowser.open("zoom.com")

        elif 'open hotstar' in query:
            speak("Opening Hotstar")
            webbrowser.open("hotstar.com")

        elif 'open netflix' in query:
            speak("Opening Netflix, here you go...")
            webbrowser.open("netflix.in")

        elif 'open prime video' in query:
            speak("Opening Prime Video, here you go...")
            webbrowser.open("primevideo.in")

        elif 'open pharmacy' in query:
            speak("Redirecting you to dhani Pharmacy")
            webbrowser.open("pharmacy.dhani.com")

        elif 'open netmeds' in query:
            speak("Redirecting you to Netmeds")
            webbrowser.open("m.netmeds.com")

        elif 'open myntra' in query:
            speak("Opening Myntra, here you go...")
            webbrowser.open("myntra.com")

        elif 'Emedicare' in query:
            speak("Redirecting you to apollo Medicare")
            webbrowser.open("apollomedicare.com")

        elif 'pharmacy' in query:
            speak("Redirecting you to apollo Medicare")
            webbrowser.open("apollopharmacy.in")

        # Music play through voice command
        elif 'play music' in query:
            speak("Opening Spotify")
            webbrowser.open("spotify.com")

        # Asking time through voice command
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        # Opening your VS code IDE through voice command
    #  elif 'open code' in query:
    #      codePath = "C:\\....your full code path.."
    #      speak("Opening Visual Studio Code, here you go...")
    #      os.startfile(codePath)

    # Some basic ones
        elif 'how are you' in query:
            speak("i'm fine, thank you for asking. ")
            speak("this is a challenging time for us. I hope you and your loved ones are staying safe and healthy.")

        elif 'what are you doing' in query:
            speak("Was making a fun list of cool nicknames.. hue hue hue")

        elif 'your nickname' in query:
            speak(
                "One day I hope to have a nickname as cool as Birbal , he was so knowledgeable .")

        elif 'make some noise' in query:
            speak("Mujhse ab nazar na phero , aao paas tum mere... Mujhko baho mein tum ghero samjhi na ... OOO senorita..Wohoo")

        elif 'quit' in query:
            speak("Lights out is usually up to you . I like staying up late, though your command is more special to me. Quiting..")
            exit()

# To be continued

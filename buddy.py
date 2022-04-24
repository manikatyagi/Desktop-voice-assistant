import ctypes
import shutil
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import smtplib
import pyjokes
import wolframalpha
import json
from GoogleNews import GoogleNews
from urllib.request import urlopen

#Initializing voices and googlenews and engine
googlenews = GoogleNews()
engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
engine.setProperty("rate", 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio) #text to speech
    engine.runAndWait() #makes speech audible in the system



def wishMe(): #checks current time of system gives output accordingly
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:  
        speak("Good Morning!")     

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    assname = ("Buddy")
    speak("I am your Artificial Intelligence Assistant"+assname)

def username(): #Interact with user to know their Name
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister" + uname)
    columns = shutil.get_terminal_size().columns

#Printing the users name
    print("#####################".center(columns))
    print(("Welcome Mr. " + uname).center(columns))
    print("#####################".center(columns))
    speak("Please tell me How can i Help you" + uname)


def takeCommand(): 
    # It takes microphone input from the user and returns string output

    #Speech recognition to understand what we say
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)  #Listens whatever passed in Microphone

#Exception handling - incase speech not recognized
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Recognized English
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Sorry Speak Again.....")
        return "None"
    return query


if _name_ == "_main_":
    # Calls wishme and username function 
    wishMe()
    username()
    
    while True:
        #Query is always checked for keywords and the appropriate function is called accordingly
        query = takeCommand().lower()

        # Logic for executing tasks based on query

#Checking for various keywords like 'Wikipedia','date','thanks' etc,
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            day = int(datetime.datetime.now().day)
            speak('Today date is')
            speak(day)
            speak(month)
            speak(year)
        
        elif 'thanks' in query:
            speak("Thanks for giving me your time, Will See you again")
            break

        elif 'open youtube' in query:
            speak("Opening Youtube for you")
            webbrowser.open("youtube.com")
        

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            speak('Current time is ' + time)
        
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            speak("This is what I found, for u Sir")
            webbrowser.open(query)

        elif "screenshot" in query:
            speak("Taking Screenshot")
            ss = pyautogui.screenshot()
            ss.save(r'E:\Screenshots\image_1.png')
            speak("Boss,Your Screenshot has been Successfully, saved")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open vtop' in query:
            webbrowser.open("vtop.vit.ac.in")

        elif 'open teams' in query:
            codepPath = "C:\\Users\\91882\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            os.startfile(codepPath)

        elif 'open teams' in query:
            codepPath = "C:\\Users\\91882\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            os.startfile(codepPath)
        
        elif 'D drive' in query:
            codepPath = "D:\\AI Class Materials"
            os.startfile(codepPath)

        elif 'E drive' in query:
            codepPath = "E:\\"
            os.startfile(codepPath)


        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif "how are you" in query or "What's up" in query:
            speak("I'm very well dude, Thanks for Asking")
            speak("What About you?")

#-------------------------- News Section ----------------------------
        elif 'headlines' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Today news') 
            googlenews.result()
            a=googlenews.gettext()
            print(*a[0:8],sep=',')
            speak(a[0:8])

        elif 'tech' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Tech')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[0:10],sep=',')
            speak(a[0:10])

        elif 'politics' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Politics')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[0:10],sep=',')
            speak(a[0:10])

        elif 'sports' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Sports')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[0:10],sep=',')
            speak(a[0:10])
            

        elif 'cricket' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('cricket')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[0:10],sep=',')
            speak(a[0:10])
            
        
#Checks for what, who and Calculate to filter questions 

        elif "what is" in query or "who is" in query or "Calculate" in query:
            client = wolframalpha.Client("YXYH4V-2YJ7RJKEV9")
            res = client.query(query)
        #Exception - If answer not found or Network error or Voice Unrecognized
            try:
                print('The answer is: ' + next(res.results).text)
                speak('The answer is: ' + next(res.results).text)
            except StopIteration:
                print("No results")

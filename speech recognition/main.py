from unittest import result
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import time

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print('The command you said is: ', Query)

        except Exception as e:
            print(e)
            print('Say that again please')
            return "None"

        return Query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is" + hour + "Hours and" + min + "Minutes")

def hello():
    speak("Hello there!")

def google(a):
    speak(f"Searching google for {a}")
    webbrowser.open(f"https://www.google.com/search?q={a}")

def take_query():
    hello()
    while(True):
        query = takeCommand().lower()

        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")
            continue
        elif "tell me the time" in query or "what's the time" in query or "what is the time" in query or "what time is it" in query:
            tellTime()
            continue

        elif "tell me your name" in query or "what is your name" in query or "what's your name" in query:
            speak("I am Jarvis. Your virtual assistant.")
            continue

        elif "what's" in query:
            query = query.replace("what's ", "")
            google(query)
            continue

        elif "what is" in query:
            query = query.replace("what is ", "")
            google(query)
            continue

        elif "which day is it" in query or "what day is it" in query:
            tellDay()
            continue

        elif "tell me about" in query:
            speak("Checking wikipedia")
            query = query.replace("tell me about ", "")
            result = wikipedia.summary(query, sentences = 4)
            speak("According to wikipedia")
            speak(result)
            continue

        elif "bye" in query:
            speak("Bye!")
            time.sleep(2)
            exit()

if __name__ == '__main__':
    take_query()

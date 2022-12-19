import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Hi, Good Morning!")
    elif 12 <= hour <= 18:
        speak("Hi, Good Afternoon!")
    else:
        speak("Hi, Good Evening!")
    speak("I am chirpy, your personalized voice chatbot, created using python. How can I help you?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:\n" + query)

    except Exception as e:
        speak("say that again please")
        print("Say that again please...")
        return "None"

    return query


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


def tellDateTime():
    currentTime=str(datetime.datetime.now())
    date=currentTime[0:10]
    hour=currentTime[11:13]
    min=currentTime[14:16]
    print('Today date is '+ date+'.'+'Time is '+hour+' hours and '+min+' minutes.')
    speak(currentTime)


if __name__ == "__main__":

    wishMe()

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.get('chrome').open("youtube.com")

        elif "open google" in query:
            webbrowser.get('chrome').open("google.com")

        elif "open linkedin" in query:
            webbrowser.get('chrome').open("linkedin.com")

        elif "which day is today" in query:
            tellDay()

        elif "what is the time now" in query:
            tellDateTime()

        elif "what is your name" in query:
            speak("I am Chirpy. Your Voice Chatbot")

        elif "play music" in query:
            webbrowser.get('chrome').open("https://open.spotify.com/")

        elif "what is the breaking news today" in query:
            webbrowser.get('chrome').open("https://www.indiatoday.in/")

        elif "quit" in query:
            speak("Bye! Have a Nice Day!")
            exit()

        elif "exit" in query:
            speak("Bye! Have a nice day!")
            exit()

        else:
            speak("I am sorry I did not understand. Please say again!")

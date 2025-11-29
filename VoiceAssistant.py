import pyttsx3
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os
import random
import smtplib
# import pyaudio
# import pywhatkit
# import pyjokes
import calendar
import speech_recognition as sr
from tkinter import messagebox
from wikipedia import summary

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

DictOfEmails = {'Ayush': "ayushbhagat8818967062@gmail.com"}  # This should be database


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak('Good Morning, sir')
    elif hour >= 12 and hour < 17:
        speak('Good Afternoon, sir')
    else:
        speak('Good Evening, sir')
    speak("How may i help you?")


def not_got():
    speak("Sorry coudnt get ")


def Abt_me():
    speak(
        "I Am Your Personal Assistant ,  I Can Search Web For You , Open App For You , Send Email , Play Music For You")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        r.energy_threshold = 3000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said: ", query)
    except Exception as e:
        print("say that again please...")
        return "None"
    return query


#
#
def startCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.energy_threshold = 3000
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print("say that again please...")
        return "None"

    return query


#
#
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    with open("F:\\Python Files\\Voice Assistant\\files\\email.txt") as f1:
        Econtents = f1.readlines()
    with open("F:\\Python Files\\Voice Assistant\\files\\pass.txt") as f2:
        Pcontents = f2.readlines()
    server.login(Econtents[0], Pcontents[0])
    server.sendmail(Econtents[0], to, content)
    f1.close()
    f2.close()
    server.close()


def send_email_ui():  # not working
    query = ""
    query = query.replace("send email to ", "")
    try:

        speak("what message you want to send sir")
        content = takeCommand()
        print(query)
        to = DictOfEmails[query]
        sendEmail(to, content)
        speak("your email has sent sir!!")
    except Exception as e:
        print(e)
        speak("sorry sir i am not able to send your email, you please try again...!!")


def wikipedia_01(query):  # not working
    speak("Searching wikipedia...")

    query = query.replace("wikipedia", "")
    try:
        print(query)
        results = wikipedia.summary(query, sentences=1)
        speak('According to wikipedia')
        print(results)
        speak(results)
        return results
    except Exception as e:
        print("Sorry, i didn't get the information from wikipedia...")
        speak("Sorry, i didn't get the information from wikipedia...")


def play_music():
    speak("playing music")
    songs = os.listdir("F:\\Songs")
    print(songs)
    os.startfile(os.path.join("F:\\Songs", songs[random.randint(0, len(songs) - 1)]))


def stop_music():
    speak("ok sir ,, music stopped")
    os.system('taskkill /f /im Music.UI.exe')


def youtube():
    speak("opening youtube")
    webbrowser.open("youtube.com")


def google():
    speak("opening google")
    webbrowser.open("google.com")


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(time)
    speak(f"it's {time}")


def single():
    speak('I am in a relationship with wifi')


def answer(query):
    try:

        query = query.replace("tell me", "")
        appID = 'JWWX5Q-PEUTTVWR8V'
        client = wolframalpha.Client(appID)
        res = client.query(query)
        answer = next(res.results).text
        print(answer)
        speak(answer)
        return answer

    except Exception as e:
        speak("sorry sir, could you please say that again...!!")
        print("sorry sir, could you please say that again...!!")




if __name__ == "__main__":
    speak("hello")
    while True:
        query = startCommand().lower()
        if 'ok jarvis' in query:
            wishMe()
            while True:
                query = takeCommand().lower()

                if 'wikipedia' in query:
                    speak("Searching wikipedia...")
                    query = query.replace("wikipedia", "")
                    try:
                        print(query)
                        results = wikipedia.summary(query, sentences=1)
                        speak('According to wikipedia')
                        print(results)
                        speak(results)
                    except Exception as e:
                        print("Sorry, i didn't get the information from wikipedia...")
                        speak("Sorry, i didn't get the information from wikipedia...")

                elif 'tell me' in query:
                    try:
                        query = query.replace("tell me", "")
                        appID = 'JWWX5Q-PEUTTVWR8V'
                        client = wolframalpha.Client(appID)
                        res = client.query(query)
                        answer = next(res.results).text
                        print(answer)
                        speak(answer)
                    except Exception as e:
                        speak("sorry sir, could you please say that again...!!")
                        print("sorry sir, could you please say that again...!!")
                # if 'play' in query:  # NEW
                #     song = query.replace('play', '')
                #     speak('playing ' + song)
                #     pywhatkit.playonyt(song)

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif "open" in query.lower():

                    if "chrome" in query.lower():  # NEW3
                        speak("Opening Google Chrome")
                        os.startfile(r"C:\Users\HP\AppData\Local\Google\Chrome\Application\chrome.exe")

                    if "zoom" in query.lower():  # NEW
                        speak("opening Zoom")

                        os.startfile(
                            r"C:\Users\HP\AppData\Roaming\Zoom\bin\zoom.exe")

                elif "you are chaman" in query:
                    speak("How do you know about it sir that i am chhaman")

                elif 'time' in query:
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(time)
                    speak(f"it's {time}")

                elif 'are you single' in query:  # NEW
                    speak('I am in a relationship with wifi')

                elif 'open code' in query:
                    os.startfile("C:\\Users\\sahil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                    speak("here it is, sir")

                elif 'play some music' in query:
                    songs = os.listdir("F:\\Songs")
                    print(songs)
                    os.startfile(os.path.join("F:\\Songs", songs[random.randint(0, len(songs) - 1)]))

                elif 'stop music' in query:
                    speak("ok sir")
                    os.system('taskkill /f /im Music.UI.exe')
                # elif 'joke' in query:
                    # speak(pyjokes.get_joke())

                elif "send email" in query:
                    query = query.replace("send email to ", "")
                    try:
                        speak("what message you want to send sir")
                        content = takeCommand()
                        print(query)
                        to = DictOfEmails[query]
                        sendEmail(to, content)
                        speak("your email has sent sir!!")
                    except Exception as e:
                        print(e)
                        speak("sorry sir i am not able send your email, you please try again...!!")

                elif 'exit' in query:
                    print("Ok Thank you, sir")
                    speak("Ok Thank you sir")
                    break

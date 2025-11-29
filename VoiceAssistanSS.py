# from typing import _SpecialForm
import pyttsx3
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os
import random
import smtplib 
import speech_recognition as sr
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
# from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

DictOfEmails = {'sahil' : "sahilshubhsoni13@gmail.com"} #This should in be database

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour <12:
        speak('Good Morning sir')
        print('Good Morning sir')
    elif hour >= 12 and hour <17:
        speak('Good Afternoon sir')
        print('Good Afternoon sir')
    else:
        speak('Good Evening sir')

    speak("How may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        r.energy_threshold = 3000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'hindi')
        print("user said: ", query)
    except Exception as e:
        print("say that again please...")
        return "None"
    return query  

def startCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.energy_threshold = 3000
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = 'en-in')

    except Exception as e:
        print("say that again please...")
        return "None"
        
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    with open("D:\\myData\\myEmail\\email.txt") as f1:
        Econtents = f1.readlines()
    with open("D:\\myData\\myEmail\\pass.txt") as f2:
        Pcontents = f2.readlines()
    server.login(Econtents[0], Pcontents[0])
    server.sendmail(Econtents[0], to, content)
    f1.close()
    f2.close()
    server.close()

def notes(content):
    f = open("D:\\myData\\Notes.txt", "a")
    f.write(content)
    f.close()
    speak("your notes have successfully completed!!")
    print("your Notes have successfully completed!!")

def readNotes():
    with open("D:\\myData\\Notes.txt") as f:
        return f.read()

if __name__ == "__main__":
    flag = True
    while True:
        query = startCommand().lower()
        if 'hey david' in query and flag or 'hello zara' in query and flag==False :
            wishMe()
            while True:
                query = takeCommand().lower()
                if 'exit' in query:
                    print("Ok Thank you, sir")
                    speak("Ok Thank you sir")
                    break

                elif "thank you" in query or "thanks" in query:
                    print('Any thing for you, Sir!')
                    speak("any thing for you sir")

                elif 'switch assistant' in query:
                    if flag == True:
                        flag = False
                        engine.setProperty('voice', voices[1].id)
                        speak("hello sir i am zara your new virtual assistent...")
                        print("hello sir i am zara your new virtual assistent...")
                        break
                    elif flag == False:
                        flag = True
                        engine.setProperty('voice', voices[0].id)
                        speak("hello sir i am david your new virtual assistent...")
                        print("hello sir i am david your new virtual assistent...")
                        break
                    else:
                        speak('sorry sir could you please say that again')
                        print('sorry sir could you please say that again')

                elif 'wikipedia' in query:
                    speak("Searching wikipedia...")
                    query = query.replace("wikipedia", "")
                    try:
                        results = wikipedia.summary(query, sentences = 2)
                        speak('According to wikipedia')
                        print(results)
                        speak(results)
                    except Exception as e:
                        print("Sorry, i didn't get the information from wikipedia...")
                        speak("Sorry, i didn't get the information from wikipedia...")

                elif 'tell me' in query:
                    try:
                        query = query.replace("tell me", "")
                        appID = 'XL9JR4-XW55ETXTE3'
                        client = wolframalpha.Client(appID)
                        res = client.query(query)
                        answer = next(res.results).text
                        print(answer)
                        speak(answer)
                    except Exception as e:
                        speak("sorry sir, could you please say that again...!!")
                        print("sorry sir, could you please say that again...!!")

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'the time' in query:
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(time)
                    speak(f"it's {time}")

                elif 'open code' in query:
                    os.startfile("C:\\Users\\sahil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                    speak("here it is, sir")

                elif 'play music' in query:
                    songs = os.listdir("D:\\Songs")
                    print(songs)
                    os.startfile(os.path.join("D:\\Songs", songs[random. randint(0,len(songs)-1)]))

                elif 'stop music' in query:
                    speak("ok sir")
                    os.system('taskkill /f /im Music.UI.exe')

                elif "send email" in query:
                    query = query.replace("send email to ", "")
                    try:
                        speak("what message you want to send sir")
                        content =takeCommand()
                        print(query)
                        print('Content : ', content)
                        speak('do you want send this...')
                        confirmation = takeCommand()
                        if 'yes' in confirmation:
                            to = DictOfEmails[query]
                            sendEmail(to, content)
                            speak("your email has sent sir!!")
                            print("your email has sent sir!!")
                        else:
                            speak("ok sir")
                            print('Ok sir!')
                    except Exception as e:
                        print(e)
                        speak("sorry sir i am not able to send your email, you please try again...!!")

                elif "temperature" in query:
                    print("In which city sir")
                    speak("In which city sir")
                    search = takeCommand()
                    search = "temperature in " + search
                    url= f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup (r.text,"html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")

                elif 'read notes' in query or 'read note' in query:
                    speak(readNotes())
                    print(readNotes())

                elif "notes" in query or 'note' in query:
                    speak('what do you want to write in notes sir')
                    content = takeCommand()
                    speak("do you want to write this sir")
                    print(content)
                    speak(content)
                    query = takeCommand()
                    if 'yes' in query:
                        notes(content)

                elif 'news' in query:

                    try:
                        jsonObj = urlopen(
                            "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=ea1b8a7f27ef496d90cc64a6f18ea505")
                        # jsonObj = urlopen("https://www.covid19india.org")
                        data = json.load(jsonObj)
                        i = 1

                        speak('here are some top news from the times of india')
                        print('''=============== TIMES OF INDIA ============''' + '\n')

                        for item in data['articles']:
                            if i > 3:
                                break
                            print(str(i) + '. ' + item['title'] + '\n')
                            print(item['description'] + '\n')
                            speak(str(i) + '. ' + item['title'] + '\n')
                            i += 1
                    except Exception as e:
                        print(str(e))

                elif 'covid updates' in query:
                    speak("here you go sir")
                    webbrowser.open("covid19india.org")

                # elif "camera" in query or "take a photo" in query:
                #     ec.capture(0,"robo camera","img.jpg")





from tkinter import *
from tkinter import ttk
import VoiceAssistant
import threading
import datetime
from tkinter import messagebox



def send():
    send = "You : " + e.get()
    txt.configure(state="normal")
    txt.insert(END, "\n" + send)
    txt.configure(state="disabled")

    if (e.get().lower() == "hello"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Good Afternoon Sir ! How May i Help You")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.wishMe, name="mythread1")
        mythread1.start()

    elif (e.get().lower() == "hello how are you"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Fine Sir")
        txt.configure(state="disabled")

    elif (e.get().lower() == "hi"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Good Afternoon Sir ! How May i Help You")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.wishMe, name="mythread1")
        mythread1.start()

    elif (e.get().lower() == "what can you do"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> I Am Your Personal Assistant !! I Can Search Web For You ,Open App For You , Send Email ,Play Music For You")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.Abt_me, name="mythread1")
        mythread1.start()

    elif (e.get().lower() == "tell me a joke"):
        joke=VoiceAssistant.pyjokes.get_joke()
        txt.configure(state="normal")
        txt.insert(END, "\n" +"--> "+joke )
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.speak(joke), name="mythread1")
        mythread1.start()

    elif (e.get().lower() == "open youtube"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Opened Youtube !!")
        txt.configure(state="disabled")
        VoiceAssistant.youtube()

    elif (e.get().lower() == "open Google"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Opened Google !!")
        txt.configure(state="disabled")
        VoiceAssistant.google()

    elif (e.get().lower() == "play music"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Playing Music...")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.play_music, name="mythread1")
        mythread1.start()

    elif (e.get().lower() == "stop music"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Music Stopped !!")
        txt.configure(state="disabled")
        VoiceAssistant.stop_music()

    elif (e.get().lower() == "show time"):
        time = datetime.datetime.now().strftime("%H:%M:%S")
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> " + time)
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.time, name="mythread1")
        mythread1.start()

    elif (e.get().lower() == "send email"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> What message you want to send sir")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.send_email_ui, name="mythread1")
        mythread1.start()

    elif (e.get().lower() == "are you single"):
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> I am in a relationship with wifi")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.speak("I am in a relationship with wifi"), name="mythread1")
        mythread1.start()

    else:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Sorry ! coudnt get")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.not_got, name="mythread1")
        mythread1.start()


    e.delete(0, END)


def voice():

    query = VoiceAssistant.takeCommand().lower()

    send = "You : " + query
    txt.configure(state="normal")
    txt.insert(END, "\n" + send)
    txt.configure(state="disabled")

    if 'joke' in query:
        joke = VoiceAssistant.pyjokes.get_joke()
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> " + joke)
        txt.configure(state="disabled")
        VoiceAssistant.speak(joke)

    elif 'hello' in query:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Good Afternoon Sir ! How May i Help You")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.wishMe, name="mythread1")
        mythread1.start()





    elif 'wikipedia' in query:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Searching Wikipedia")
        txt.configure(state="disabled")

        ans=VoiceAssistant.wikipedia_01(query)
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> "+ans)
        txt.configure(state="disabled")

    elif 'play music' in query:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Playing Music ...")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.play_music, name="mythread1")
        mythread1.start()


    elif 'stop music' in query:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Music Stopped !!")
        txt.configure(state="disabled")
        VoiceAssistant.stop_music()

    elif 'youtube' in query:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Opening Youtube !!")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.youtube(), name="mythread1")
        mythread1.start()

    elif 'google' in query:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Opening Google !!")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.google, name="mythread1")
        mythread1.start()


    elif 'time' in query:

        time = datetime.datetime.now().strftime("%H:%M:%S")
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> " + time)
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.time, name="mythread1")
        mythread1.start()

    elif 'send email' in query:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Sending Email...")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.send_email_ui, name="mythread1")
        mythread1.start()

    elif 'are you single' in query:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> I am in a relationship with wifi")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.single, name="mythread1")
        mythread1.start()

    elif 'what can you do' in query:
        txt.configure(state="normal")
        txt.insert(END,"\n" + "--> I Am Your Personal Assistant !! I Can Search Web For You ,Open App For You , Send Email ,Play Music For You")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.Abt_me, name="mythread1")
        mythread1.start()

    elif 'tell me' in query:

        ans=VoiceAssistant.answer(query)
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> " +ans )
        txt.configure(state="disabled")

    elif 'auto run' in query:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Now On Always on Mode ,Say Ok David to wake me up and stop listening to Stop")
        txt.configure(state="disabled")
        VoiceAssistant.speak("Now on autorun mode , say ok david to wake me up and stop listening to Stop")
        while True:

            query = VoiceAssistant.startCommand().lower()
            print("listening started")
            if 'ok david' in query:
                txt.configure(state="normal")
                txt.insert(END,"\n" + "Listening in Background...")
                txt.configure(state="disabled")
                VoiceAssistant.speak("Listening in Background")
                while True:
                    ans=voice()
                    query=ans
                    print("while 2")
                    print(query)
                    if 'stop listening' in query:
                        txt.configure(state="normal")
                        txt.insert(END, "\n" + "Listening Stopped,Say OK DAVID to Start Again...")
                        txt.configure(state="disabled")
                        VoiceAssistant.speak("Listening Stopped , Say OK DAVID to Start Again")
                        print("Ok Thank you, sir")

                        break

            elif 'exit listening' in query:
                VoiceAssistant.speak("Background listening stopped , click on mic button to wake me up")
                txt.configure(state="normal")
                txt.insert(END, "\n" + "Background Listening Stopped...")
                txt.configure(state="disabled")
                print("exit")
                break


    elif 'stop listening' in query:
        pass

    else:
        txt.configure(state="normal")
        txt.insert(END, "\n" + "--> Sorry ! Coudn't Get")
        txt.configure(state="disabled")
        mythread1 = threading.Thread(target=VoiceAssistant.not_got, name="mythread1")
        mythread1.start()

    return query


def mic():
    txt.configure(state="normal")
    txt.insert(END, "\n" + "Listening...")
    txt.configure(state="disabled")

    print("Mic on")

    mythread1 = threading.Thread(target=voice, name="mythread1")
    mythread1.start()

def change_theme():
    theme_name = theme_choice.get()
    fg_color, bg_color = color_dict[theme_name]
    txt.config(foreground=fg_color, background=bg_color)



# main part
root = Tk()
txt = Text(root,state="disabled")
root.title("Assistant")
#  txt.configure(state="normal")
# set_menu_bar
main_menu = Menu()
Language = Menu(main_menu, tearoff=False)
Voice = Menu(main_menu, tearoff=False)

color_theme = Menu(main_menu, tearoff=False)

theme_choice = StringVar()
# color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon, monokai_icon,night_blue_icon)
color_dict = {
    'Light Default ': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}
main_menu.add_cascade(label='Language', menu=Language)
main_menu.add_cascade(label='Voice', menu=Voice)

main_menu.add_cascade(label='Color Theme', menu=color_theme)

Language.add_radiobutton(label="Eng")

Voice.add_radiobutton(label="Male")  # var dena baki hai
Voice.add_radiobutton(label="Female")

for i in color_dict:
    color_theme.add_radiobutton(label=i, variable=theme_choice, compound=LEFT,
                                command=change_theme)

root.config(menu=main_menu)
large_font=('Verdana',15)
e = Entry(root, width=52,font=large_font)
send_btn = PhotoImage(file='icons/send.png')
send = ttk.Button(root, image=send_btn, command=send)
txt.grid(row=0, column=0, columnspan=6, sticky=W + E)
e.grid(row=1, column=0, padx=5, pady=2,ipady=10)
mike_icon = PhotoImage(file='icons/MIC-BUTTON.png')
mike_btn = ttk.Button(root, image=mike_icon, command=mic)
mike_btn.grid(row=1, column=1, padx=5, pady=5)
send.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
#
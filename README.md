# 🎙️ Voice-Enabled Personal Assistant  
A Python-based conversational desktop assistant with voice recognition, speech synthesis, automation features, and a Tkinter-powered GUI.

---

## 🚀 Overview  
**Voice-Enabled Personal Assistant** is a smart desktop assistant built using **Python**, **SpeechRecognition**, **pyttsx3**, **WolframAlpha API**, and **Tkinter**.  
It can understand voice commands, talk back using text-to-speech, search the web, play music, send emails, fetch Wikipedia summaries, answer general queries, automate tasks, and more.

This project also contains a **graphical chat UI** with theme switching, a mic button for voice input, and real-time assistant responses.

---

## 🎯 Features

### 🔊 **Voice Commands**
- Activate assistant with trigger words (`Hey David`, `Hello Zara`, `Ok Jarvis`, etc.)
- Recognizes speech using Google Speech Recognition (SpeechRecognition library)
- Responds using pyttsx3 TTS engine

### 💬 **Conversation & Responses**
- Greets user based on time of day  
- Can tell jokes  
- Answers factual questions using **WolframAlpha API**  
- Fetches Wikipedia summaries  

### 📨 **Email Automation**
- Sends emails using `smtplib`  
- Reads sender credentials from secure text files  
- Supports confirmations before sending

### 🎵 **Media Control**
- Plays random music from user directory  
- Stops music on command

### 🌐 **Web Automation**
- Opens YouTube  
- Opens Google  
- Opens applications like **Chrome**, **VS Code**, **Zoom**

### 🕒 **Time Weather & News**
- Speaks current system time  
- Fetches temperature via Google scraping  
- Reads top news headlines (NewsAPI)

### 📝 **Notes**
- Creates notes  
- Reads previously saved notes from a file

### 🧠 **Multi-Voice Assistant**
- Supports two personalities:
  - **David** – male voice  
  - **Zara** – female voice  
- Toggle assistant personality with “switch assistant”

### 🖥️ **Tkinter GUI**
- Chat-style window  
- Mic button to speak  
- Text input to type commands  
- Theme options (Light, Dark, Red, Night Blue, Monokai)  
- Background listening mode ("always-on" mode)

👨‍💻 Author

Sahil Soni

Python Developer | Voice Automation | Desktop Apps

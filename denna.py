import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
def wishMe ():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak('Good Morning')
    elif hour >= 12 and hour < 18 :
        speak('Good Afternoon')
    else :
        speak('Good Evening')
    speak('I am Denna sir. Please tell me how may i help you')
    #
def takeCommand () :
    r= sr.Recognizer()
    with sr.Microphone() as source :
        print('Listening...')
        r.pause_threshold = 1
        audio=r.listen(source)
    try :
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f'You said :- {query} \n')
    except Exception as e :
        #print(e)
        print('Say that again please...')
        return 'None'
    return query 


if __name__ == '__main__' :
    wishMe()
   # while True :
    a=1
    if a==1 :
        query=takeCommand().lower()
        if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        # elif 'open youtube' in query :
        #     webbrowser.open('youtube.com')
        # elif 'open google' in query :
        #     webbrowser.open('google.com')
        # elif 'open stack overflow' in query :
        #     webbrowser.open('stackoverflow.com')
        # #elif 'play music' in query :
        # elif 'open instagram' in query:
        #     webbrowser.open('instagram.com')
        # elif 'open facebook' in query :
        #     webbrowser.open('facebook.com')
        # elif 'open whatsapp' in query :
        #     webbrowser.open('https://web.whatsapp.com/')

            

        elif 'the time' in query :
            str_Time =datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {str_Time}')
        elif 'open code' in query or 'open vscode' in query :
            code_path="C:\\Users\\sakin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif query=='who are you' :
            speak('I am denna your personal assistant')
        elif 'open' in query :

            webbrowser.open(f'{query[::-1]}.com')
        






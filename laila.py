import pyttsx3    # module
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')               #  sapi5-it is api used to get voice input
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)   #used to set voice   ..there are
                                           # 2 types of voive male and female 1 ,2 for female and 0 for male
def speak(audio):
    ''' this function is used to take input and it display as audio'''    # docstring
    engine.say(audio)
    engine.runAndWait()
def wishme():
    ''' this function is used for greeting purpose'''
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning !")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am lila. please tell me how may i help you ")



def takeCommand():
    '''it takes microphone input from the user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening...")
        r.pause_threshold=1 # it will not complete command if i rest 1 sec during command
        r.energy_threshold=500 #it used to increse intensity of listening
        audio=r.listen(source)

    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n" )
    except Exception as e :
        print("say that again please...")
        return "None"
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('manaliindulkar36@gmail.com','15_@SeptemBer')
    server.sendmail('manaliindulkar36@gmail.com',to,content)


if __name__=="__main__":
    wishme()
    while True:
     query=takeCommand().lower()
     if 'wikipedia' in query :
         speak("searching wikipedia...")
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query , sentences=2)   #sentences used to read line of info from wikipedia
         speak("acording to wikipedia")
         print(results)
         speak(results)
     elif 'open youtube' in query:
         webbrowser.open("youtube.com")

     elif 'open google' in query:
         webbrowser.open("google.com")


     elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")

     elif 'play music' in query:
         music_dir='D:\\my music'
         songs=os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir,songs[0]))
     elif 'the time' in query:
         strTime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"the time is {strTime}")
     elif 'open pycharm' in query:
         codepath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.3\\bin"
         os.startfile(codepath)

     elif 'send email' in query:       #it will activated after activation of less secure app on in gmail setting
         try:
             speak("what should i say ?")
             content=takeCommand()
             to="manaliindulkar36@gmail.com"
             sendemail(to,content)
             speak("email has been send")
         except Exception as e:
             speak("soory im not able to send")
     elif 'exit' in query :

         break

     speak("thank you ")










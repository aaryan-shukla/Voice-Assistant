import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING ")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON ")
    else:
        speak("GOOD EVENING")

    speak("ASSISTANT THIS SIDE , TELL ME HOW MAY I HELP YOU")

def takecom():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            print("RECONGIZING....")
            query=r.recognize_google(audio, language="en-in")
            print(f"USER SAID :{query}")
        except Exception as e:
            print("SAY THAT AGAIN PLEASE... ")
            return  "NONE"
    return query
if __name__ == '__main__':
    wish()
    i=1
    while i:
        query=takecom().lower()

        if 'wikipedia' in query:
            speak('LOOKING IN THE WIKIPEDIA')
            query=query.replace("wikipedia", " ")
            results=wikipedia.summary(query,sentences=2)
            speak("ACCORDING TO THE WIKIPEDIA ")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open hotstar' in query:
            webbrowser.open("https://www.hotstar.com/in")
        elif 'open geeks for geeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open news' in query:
            webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
        elif 'open covid tracker' in query:
            webbrowser.open("https://www.worldometers.info/coronavirus/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open sap portal' in query:
            webbrowser.open("https://kiit.ac.in/sap/")
        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458712209&hvpos=&hvnetw=g&hvrand=3710325760244832719&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9040183&hvtargid=kwd-10573980&hydadcr=14453_2154373&gclid=Cj0KCQjwkbuKBhDRARIsAALysV5A1fm3eyMsfNe7RYBTJ7r3j9xz_z7LOyOB2GT3C40AHxW24zqTwssaAu4NEALw_wcB")
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com/")
        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/0/h")
        elif 'open sony liv' in query:
            webbrowser.open("https://www.sonyliv.com/")
        elif 'play music' in query:
            music_dir='D:\\music'
            songs=os.listdir(music_dir)
            length=len(songs)
            rl=random.randint(0,length-1)
            os.startfile(os.path.join(music_dir,songs[rl]))
        elif 'the time' in query:
            today = datetime.datetime.now()
            today.strftime("%H %M %S")
            speak(f"THE TIME RIGHT NOW IS {today}")
        elif 'open code' in query:
            code="C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        elif 'send email' in query:
            email=smtplib.SMTP('smtp.gmail.com',587)
            email.starttls()
            email.login("aaryanshuklashukla@gmail.com","Neeraj@1969")
            speak("PLEASE SPEAK THE CONTENT OF THE EMAIL")
            cont=takecom()
            speak("enter the EMAIL ID OF RECIEVER")
            recv=input("")
            email.sendmail("aaryanshuklashukla@gmail.com",recv,cont)
            email.quit()
        elif 'jokes' in query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)
        elif 'search' in query:
            speak("What do you want me to search for (please type) ? ")
            search_term = input()
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get(
                'C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(search_url)
            speak(f"here are the results for the search term: {search_term}")
            print(search_term)
        elif 'play movie' in query:
            movie_dir = 'C:\\Users\\KIIT\\Videos\\Captures'
            movies = os.listdir(movie_dir)
            length = len(movies)
            rl = random.randint(0, length - 1)
            os.startfile(os.path.join(movie_dir, movies[rl]))
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Aaryan Shukla.")
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecom()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            query = takecom()
            if 'yes' in query or 'sure' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        else :
            print("SPEAK AGAIN COULDN'T FIND What you asked ")



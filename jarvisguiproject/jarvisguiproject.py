from cgitb import text
import smtplib
import speech_recognition as f
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
from tkinter import *
from turtle import color
from PIL import ImageTk
# jarvis conde
def jarivsup():

    def speek(trxt):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(trxt)
        engine.runAndWait()

    def wichme():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speek("Good mornig sir plzz pactice python programing")
        elif hour>=12 and hour<18:
            speek("Good afternoon sir your tee time")    
        else:
            speek("good evning sir")    

        speek("hello sir i am jarvis plzz tell me how i can i help you")    

    # this takeCom funcation voice to text convert
    def takeCom():
        ma=f.Recognizer()  
        with f.Microphone() as mic:
            ma.pause_threshold=1
            w=ma.listen(mic)
        try:   
            print("Listing...........") 
            quey=ma.recognize_google(w,language="en-in")
            print(f"user said: {quey}")
        except:   
            speek("say tha try again Plzz..") 
        return  quey  

    def senfEmail(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("your-gmail",'password-your')
        server.sendmail('your-gmail',"senger-gmail","hello irfan khan how are you")
        server.quit()

    # wichme()
    if __name__=="__main__":
        wichme()
        while True:
            
            quey=takeCom().lower()
            if "wikipedia" in quey:
                speek("searching Wikipedia")
                quey1=quey.replace("wikipedia","")
                wiki=wikipedia.summary(quey1,sentences=2)
                speek("According to Reseult")
                speek(wiki)
            elif "open youtube" in quey:
                webbrowser.open("https://www.youtube.com/")   
            elif "open google" in quey:
                webbrowser.open("hackerone.com") 
            elif "open instagram" in quey:
                webbrowser.open("instagram.com")
            elif "open facebook" in quey:
                webbrowser.open("facebook.com")  
            elif "play music" in quey:  
                so="C:\\Users\\STAR\\XSS-LOADER\\Music\\fav"
                lis=os.listdir(so)
                w=random.choice(lis)
                my_computer = os.startfile(os.path.join(so,w))  
            elif "the time" in quey:
                time1=datetime.datetime.now().strftime("%H:%M:S")
                speek(f"Hello sir the time is {time1}")
            elif "how are you" in quey:
                speek(" i am fine sir")
                #   speek("sir i can help you ")
            elif "open code" in quey:
                speek("visual stodio code open now plzz wait")
                os.startfile("C:\\Users\\STAR\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")
            elif "open google" in quey:
                speek("google is open")
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")
            elif "open files" in quey:
                speek("file in open")
                os.startfile("C:\\Users\\STAR\\XSS-LOADER\\Downloads")    
            elif "exit" in quey:
                speek("Exit jarvis programer")
                break    

# Tknter code

jarvis = Tk()
jarvis.title("jarvis")
jarvis.geometry("1000x625")
jarvis.minsize(1000,612)
jarvis.maxsize(1000,612)
label=Label(jarvis,font=('Helvetica', 15, 'bold') ,text="Hello sir")
label.pack()
bg1=PhotoImage(file="projects/jarvis2.png")
bg2=Label(jarvis,image=bg1)
bg2.place(x = 0, y = 0)
btn=Button(jarvis,text="Start jarvis",bg="red",height=2,width=10,command=jarivsup)
btn.place(x=492,y=565)

jarvis.mainloop()


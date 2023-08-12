
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import openai

api="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"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "hi" in command:
                command = command.replace("hi","")
                
    except:
        pass
    return command

def run_assistant():
    command = get_command()
    print(command)
    if 'play' in command:
        song = command.replace("play",' ')
        talk("playing"+ song)
        pywhatkit.playonyt(song)
        print("Playing songs")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H : %M %p")
        talk("Now time is "+ time)

    elif "tell me about" in command:
        about = command.replace("tell me about","")
        info = wikipedia.summary(about,2)
        print(info)
        talk(info)
    elif "what is your name " in command:
        aa=command.replace("what is your name")
        say=("hi how can i help"+aa)
        
        print(say)
        talk(say)
        
    

    else:
        talk("soory i can't understand tell me again")

    
while True:
    run_assistant()

import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime
import pyjokes
import pywhatkit
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speeck_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert to text
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening.......")
        audio = recognizer.listen(source)
        try:

            #Recognizer speech using Google speech recognition
            command =recognizer.recognize_google(audio)
            print(f" You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speeck_text("Sorry,I did not understand that.")
            return ""
        except sr.RequestError:
            speeck_text("Sorry, the service is unavailable.")
            return ""
        
# Functionto search the web or get info form wikipedia
def search_info(command):
    try:
        # Function to search the web or command and get a summary
        speeck_text(f" Searching for {command} on Wikipedia")
        result = wikipedia.summary(command,sentences=2)
        print(result)
        speeck_text(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speeck_text("There are multiple option ,please be more specific.")
    except wikipedia.exceptions.PageError:
        speeck_text("I cound not find anything on wikipedia, let me search Google.")
        webbrowser.open(f"http://www.google.com/search?q={command}")    

# Function to search the web or open social media
def handle_command(command):
    #Open Specific websites based on the command
    if "google" in command:
        speeck_text("Opening Google")
        webbrowser.open("http://www.google.com")
    elif "youtube" in command:
        speeck_text("opening youtube")
        webbrowser.open("http://www.youtube.com")  
    elif "facebook" in command:
        speeck_text("Opening Facebook")
        webbrowser.open("http://www.facebook.com") 
    elif "Instagram" in command:
        speeck_text("Opening Instagram")
        webbrowser.open("http://www.instagram.com") 
    elif "gmail" in command:
        speeck_text("Opening Gmail")
        webbrowser.open("http://mail.google.com")  
    elif "github" in command:
        speeck_text("Opening Github") 
        webbrowser.open("http://github.com")     
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M:%p")
        print(time_now)
        speeck_text(f"Today time is {time_now}")
    elif "date" in command:
        t_date = datetime.datetime.now().strftime("%B %d,%Y")    
        print(t_date)
        speeck_text(f"Today date is {t_date}")
    elif "play" in command:
        song = command.replace('play','').strip()
        speeck_text(f"playing {song} on youtube")
        pywhatkit.playonyt(song)    
    elif "joke" in command:
        jokes = pyjokes.get_joke(language="en",category="neutral")
        print(jokes)
        speeck_text(f"Goood Jokes {jokes}.")    

    else:
        speeck_text(f"Searching for {command} on Google")
        search_info(command)

# Main assistant function
def voice_assistant():
    speeck_text("How can i help you today")
    while True:
        command = listen()
        if command:
            if "exit" in command or "bye" in command:
                speeck_text("Goodbye for today")
                break
            else:
                handle_command(command)

if __name__ == "__main__":
    voice_assistant()                              
       

          
        
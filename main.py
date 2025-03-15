import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import openai

# Initialize text-to-speech engine
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Capture voice command
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {command}\n")
        return command.lower()
    except Exception as e:
        print("Sorry, I couldn't understand. Please try again.")
        return ""

# Open common applications
def open_application(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "command prompt": "cmd.exe",
        "task manager": "taskmgr.exe"
    }
    if app_name in apps:
        os.system(apps[app_name])
        speak(f"Opening {app_name}")
    else:
        speak("Sorry, I don't know that application.")

# Open websites
def open_website(site_name):
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "wikipedia": "https://www.wikipedia.org",
        "github": "https://www.github.com"
    }
    if site_name in websites:
        webbrowser.open(websites[site_name])
        speak(f"Opening {site_name}")
    else:
        speak("Sorry, I don't have that website stored.")

# Get current time
def get_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {now}")

# ChatGPT API call
def ask_chatgpt(question):
    openai.api_key = getapikey
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": question}
            ],
            temperature=0.7
        )
        answer = response["choices"][0]["message"]["content"].strip()
        speak(answer)
        return answer
    except Exception as e:
        speak("Sorry, I couldn't fetch a response from OpenAI.")
        return "Error fetching response."

# Main execution loop
def main():
    speak("Welcome to Next Level AI Assistant, made by Abhishek.")
    print("Welcome to Next Level AI Assistant, made by Abhishek.")
    
    while True:
        command = take_command()
        if "open" in command:
            words = command.split("open ")[-1]
            if words in ["youtube", "google", "wikipedia", "github"]:
                open_website(words)
            elif words in ["notepad", "calculator", "command prompt", "task manager"]:
                open_application(words)
            else:
                speak("I can't open that yet.")
        elif "time" in command:
            get_time()
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            response = ask_chatgpt(command)
            print("AI Assistant:", response)

if __name__ == "__main__":
    main()

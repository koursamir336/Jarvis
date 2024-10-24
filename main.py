10.24 9:37 PM
import os
import requests
from bs4 import BeautifulSoup
import wikipedia
import datetime

# Function to speak text using Termux TTS
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

# Function to take input from the user in Termux
def takeCommand():
    print("Waiting for your command...")
    try:
        # Using a simple prompt to avoid input issues in Termux
        command = input("You: ").lower()
        return command
    except Exception as e:
        speak("Sorry, I couldn't understand that.")
        return "None"

# Greeting function based on time
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, Samir.")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Samir.")
    else:
        speak("Good Evening, Samir.")
    speak("How can I help you and assist you today?")

# Wikipedia search function
def searchWikipedia(query):
    speak("Searching Wikipedia...")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)

# Google search function
def searchGoogle(query):
    speak("Opening Google search...")
    query = query.replace("google", "")
    os.system(f'termux-open-url "https://www.google.com/search?q={query}"')

# Function to get weather information using Google
def getWeather():
    speak("Fetching weather information...")
    search = "current temperature"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    temp = soup.find("div", class_="BNeawe").text
    speak(f"The current temperature is {temp}")

# Function to tell the current time
def tellTime():
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {strTime}")

# Main function to handle commands
if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            searchWikipedia(query)

        elif 'google' in query:
            query = query.replace("google", "")
            searchGoogle(query)

        elif 'weather' in query:
            getWeather()

        elif 'time' in query:
            tellTime()

        elif 'exit' in query or 'sleep' in query:
            speak("Goodbye, Samir.")
            break


import os
import requests
import speech_recognition as sr
import pyttsx3
import nltk
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Adjust speech speed
engine.setProperty('volume', 1.0)  # Max volume

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input and return text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        speak("I couldn't understand that. Could you repeat?")
    except sr.RequestError:
        speak("Sorry, there was a network error.")
    return None

def google_search(query):
    """Search Google using Programmable Search Engine."""
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)
        results = service.cse().list(q=query, cx=CSE_ID, num=3).execute()
        if 'items' in results:
            return results['items'][0]  # Return best result
        return None
    except Exception as e:
        return str(e)

def fetch_webpage(url):
    """Scrape text content from a webpage."""
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = '\n'.join([para.get_text() for para in paragraphs if para.get_text().strip()])
        return text if text else "No readable content found."
    except requests.exceptions.RequestException as e:
        return str(e)

def summarize_text(text, num_sentences=5):
    """Summarize text using NLTK's sentence tokenizer."""
    nltk.download('punkt')
    sentences = nltk.tokenize.sent_tokenize(text)
    return ' '.join(sentences[:num_sentences])

def assistant():
    """Main function to run the AI assistant."""
    speak("Hello! How can I assist you today?")
    while True:
        query = listen()
        if query:
            if "exit" in query or "stop" in query:
                speak("Goodbye! Have a great day.")
                break
            search_result = google_search(query)
            if search_result:
                title = search_result.get('title', 'No title')
                snippet = search_result.get('snippet', 'No preview available')
                url = search_result.get('link', '')
                full_text = fetch_webpage(url)
                summary = summarize_text(full_text)
                response = f"Here's what I found about {title}: {snippet}\nSummary: {summary}"
                speak(response)
            else:
                speak("I couldn't find anything relevant.")

if __name__ == "__main__":
    assistant()

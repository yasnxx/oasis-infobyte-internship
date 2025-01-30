import os
import datetime
import wikipedia
import webbrowser
import smtplib
from gtts import gTTS # Google Text-to-Speech
from IPython.display import Audio, display
import ipywidgets as widgets # For Colab input

# Dictionary for email recipients
email_dict = {"friend": "friend@example.com", "family": "family@example.com"}

def speak(text):
    """Convert text to speech using gTTS and play audio in Colab."""
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    display(Audio("speech.mp3", autoplay=True))

def wishMe():
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Hunterdii. How may I assist you?")

def sendEmail(to, content):
    """Send an email (requires enabling less secure apps or OAuth setup)."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your-email@gmail.com', 'your-password') # Use App Password for security
        server.sendmail('your-email@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        speak("Sorry, I am not able to send this email.")

# Create a user input box in Colab
query_box = widgets.Text(
    value='', 
    placeholder='Type your command here...',
    description='Command:',
    disabled=False
)
display(query_box)

def process_query(widget):
    """Process the user input and execute the corresponding command."""
    query = widget.value.lower() # FIXED: Extract text from widget

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("https://youtube.com")

    elif 'open google' in query:
        webbrowser.open("https://google.com")

    elif 'play music' in query:
        music_url = "https://music.youtube.com/playlist?list=PLIL965-SXjbVEiWwe1l6RApWYDnbhc_Oz"
        webbrowser.open(music_url)

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the current time is {strTime}")

    elif 'search google for' in query:
        search_query = query.replace('search google for', '')
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif 'search youtube for' in query:
        search_query = query.replace('search youtube for', '')
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

    elif 'send email to' in query:
        speak("What should I say?")
        content = input("Enter email content: ")
        speak("Who should I send it to?")
        recipient = input("Enter recipient name (e.g., friend): ").lower()
        to = email_dict.get(recipient, None)
        if to:
            sendEmail(to, content)
        else:
            speak("Recipient not found.")

    elif 'shutdown' in query or 'restart' in query:
        speak("Shutdown and restart commands are not available in Google Colab.")

# Run the assistant only once per execution
wishMe()

# Use the text box to get user input
query_box.on_submit(process_query) # FIXED: `widget.value.lower()`

import speech_recognition as sr
import os
import threading
from gtts import gTTS
from playsound import playsound  # To play the generated audio
from chatbotu import responsess

class TextToSpeech:
    def __init__(self):
        self.lock = threading.Lock()  # To prevent concurrent access to the audio play

    def convert(self, text: str):
        def tts():
            with self.lock:  # Ensure only one thread can access the audio playback at a time
                try:
                    tts = gTTS(text=text, lang='en')  # Create a gTTS object
                    audio_file = "response.mp3"
                    tts.save(audio_file)  # Save the audio to a file
                    
                    # Check if the file exists before playing
                    if os.path.exists(audio_file):
                        playsound(audio_file)  # Play the audio file
                        os.remove(audio_file)  # Remove the file after playing
                    else:
                        print("Audio file does not exist:", audio_file)
                except Exception as e:
                    print("Error while playing audio:", e)

        threading.Thread(target=tts).start()

def speak(text):
    tts = TextToSpeech()  # Create an instance of TextToSpeech
    tts.convert(text)  # Convert text to audio and play it

def listent():
    lop=None
    r = sr.Recognizer()
    user_response = None
    response_text = None

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        user_response = r.recognize_google(audio)
        print("YOU SAID:", user_response)

        # Get response based on user input
        response_text = response(user_response)
        print("Jarvis:", response_text)

        # Use speak function to say the response text
        speak(response_text)

        # Exit on goodbye
        if "finish" in user_response.lower():
            print("Goodbye!")
            speak("Goodbye!")  # Use the speak function here too

    except sr.UnknownValueError:
        print("Could not understand audio")

    return user_response, response_text, lop

# Call listen to start the conversation
if __name__ == "__main__":
    while True:
        listent()

import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import os

def speech_to_speech_translation():
    # Initialize recognizer and translator
    recognizer = sr.Recognizer()
    translator = Translator()

    # Capture audio input
    with sr.Microphone() as source:
        print("Say something in your language:")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Translate the text
            translated_text = translator.translate(text, src="en", dest="fr")  # Change "en" and "fr" to desired languages
            print(f"Translated: {translated_text.text}")

            # Convert translated text to speech
            tts = gTTS(translated_text.text, lang="fr")  # Use the language code of the target language
            tts.save("translated_speech.mp3")
            os.system("start translated_speech.mp3")  # For macOS/Linux, replace with "open" or "afplay"

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            print(f"Error with recognition service: {e}")

# Run the function
speech_to_speech_translation()

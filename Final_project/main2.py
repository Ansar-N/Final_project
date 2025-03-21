import googletrans
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from microphone
with sr.Microphone() as source:
    print("Speak now:")
    voice = recognizer.listen(source)
    try:
        # Convert speech to text
        listen = recognizer.recognize_google(voice, language="en")
        print(f"You said: {listen}")

        # Translate text to French
        translator = googletrans.Translator()
        translate = translator.translate(listen, dest="fr")
        print(f"Translated to French: {translate.text}")

        # Convert translated text to speech
        converted_audio = gTTS(translate.text, lang="fr")
        converted_audio.save("translated_audio.mp3")

        # Play the audio
        playsound("translated_audio.mp3")
    except Exception as e:
        print(f"Error: {e}")

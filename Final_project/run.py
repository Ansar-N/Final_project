import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import playsound

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def translate_and_speak(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language).text
    print(f"Translated: {translation}")
    
    tts = gTTS(text=translation, lang=target_language)
    tts.save("output.mp3")
    playsound.playsound("output.mp3")
    os.remove("output.mp3")

def main():
    target_language = input("Enter the target language code (e.g., 'en' for English, 'ta' for Tamil): ")
    
    while True:
        original_text = recognize_speech()
        if original_text:
            print(f"You said: {original_text}")
            translate_and_speak(original_text, target_language)

if __name__ == "__main__":
    main()
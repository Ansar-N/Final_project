from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import os
import playsound
import threading

app = Flask(__name__)

# Function for text translation
def translate_text(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

# Function for text to speech
def text_to_speech(text, language, filename):
    tts = gTTS(text=text, lang=language)
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the audio file
@app.route('/upload', methods=['POST'])
def upload():
    audio_file = request.files['audio']
    recognizer = sr.Recognizer()

    # Save the audio file temporarily
    filepath = 'audio.wav'
    audio_file.save(filepath)

    # Recognize speech from the audio file
    with sr.AudioFile(filepath) as source:
        audio = recognizer.record(source)
        try:
            # Transcribe audio to text
            transcription = recognizer.recognize_google(audio)
            translated_text = translate_text(transcription, dest_language='ta')  # Translate to Tamil

            # Generate speech
            filename = 'output.mp3'
            threading.Thread(target=text_to_speech, args=(translated_text, 'ta', filename)).start()
            return jsonify({'transcription': transcription, 'translated': translated_text})
        except sr.UnknownValueError:
            return jsonify({'error': "I couldn't understand the audio."})
        except sr.RequestError:
            return jsonify({'error': "Could not request results from Google Speech Recognition service."})
        finally:
            os.remove(filepath)

if __name__ == "__main__":
    app.run(debug=True)
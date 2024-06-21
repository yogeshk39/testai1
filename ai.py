from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Voice-to-Text API!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    recognizer = sr.Recognizer()
    audio_file = request.files['file']
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return jsonify({'transcription': text})
        except sr.UnknownValueError:
            return jsonify({'error': 'Could not understand audio'}), 400
        except sr.RequestError as e:
            return jsonify({'error': f"Could not request results; {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

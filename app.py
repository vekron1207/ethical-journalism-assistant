from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import speech_recognition as sr
import tempfile
import os
from PIL import Image

app = Flask(__name__)

# Use a smaller, free model for text generation
chatbot_pipeline = pipeline("text-generation", model="facebook/opt-1.3b")
recognizer = sr.Recognizer()

def chatbot_response(text):
    response = chatbot_pipeline(text, max_length=100, do_sample=True)
    return response[0]['generated_text']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze/text', methods=['POST'])
def analyze_text():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    text = data.get('text')
    response = chatbot_response(text)
    return jsonify({"user_input": text, "response": response})

@app.route('/analyze/audio', methods=['POST'])
def analyze_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
        file.save(tmp.name)
        try:
            with sr.AudioFile(tmp.name) as source:
                audio_data = recognizer.record(source)
                transcript = recognizer.recognize_google(audio_data)
                response = chatbot_response(transcript)
        except Exception as e:
            transcript = f"Error: {str(e)}"
            response = "I couldn't process the audio."
        os.unlink(tmp.name)
    
    return jsonify({'transcript': transcript, 'response': response})

@app.route('/analyze/video', methods=['POST'])
def analyze_video():
    return jsonify({"response": "Video analysis is not supported in this free version."})

@app.route('/analyze/image', methods=['POST'])
def analyze_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
        file.save(tmp.name)
        try:
            image = Image.open(tmp.name)
            response = "I see an image, but advanced analysis requires a more powerful model."
        except Exception as e:
            response = f"Error processing image: {str(e)}"
        os.unlink(tmp.name)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

# Ethical Journalism Assistant

A simple AI-powered chatbot that analyzes text, audio, video, and images for ethical journalism purposes. It provides natural language responses using open-source models without requiring login or authentication.

## Features
- **Conversational AI**: Uses `microsoft/DialoGPT-medium` for chatbot responses.
- **Speech-to-Text**: Uses OpenAI Whisper to transcribe audio and video.
- **Image Analysis**: Uses ResNet-50 to classify images.
- **No Authentication Required**: Open and free to use.

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/ethical-journalism-assistant.git
cd ethical-journalism-assistant
```

### 2. Set Up Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install flask transformers torch torchvision torchaudio openai-whisper pillow opencv-python ffmpeg-python
```

### 4. Download Necessary Models
```sh
python -c "from transformers import pipeline; pipeline('text-generation', model='microsoft/DialoGPT-medium')"
whisper.download_model('base')
```

### 5. Run the Application
```sh
python app.py
```
The app will be available at `http://127.0.0.1:5000/`.

## Additional Enhancements
To make the project more advanced, you can:
- Integrate **Fact-Checking APIs** (e.g., Google Fact Check API)
- Use **Fine-Tuned NLP Models** for more relevant conversations
- Implement **Database Support** to store previous chats
- Add **Front-end UI Improvements** with modern frameworks like React

## Contributing
Feel free to fork the repo, submit pull requests, and suggest improvements!

## License
This project is open-source and licensed under the MIT License.

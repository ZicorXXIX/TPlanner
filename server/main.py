
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv() #
# os.environ["OPENAI_API_KEY"] = "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"
import requests
from flask_cors import CORS
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from threading import Thread
import threading
from flask import Flask, request
import os
from openai import OpenAI
openai = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
import base64
import pygame
from pathlib import Path

import google.ai.generativelanguage as glm
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = "AIzaSyAbZHdUXe7MokOeBw4pxrnZ9LD3QpVV_5U"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro-vision')

app = Flask('')
CORS(app)
# socketio = SocketIO(app, cors_allowed_origins="*")
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['CORS_HEADERS'] = 'Content-Type'

from langchain import OpenAI, ConversationChain
llm= OpenAI(temperature=0.9)
conversation = ConversationChain(llm=llm, verbose=True)

conversation.predict(input="""Hi there,  You are a travel agent who helps users make exciting travel plans.

      Ask me a set of questions regarding my travel and plan an iternary for me. The iternary should have description of each day.
    limit to 200-250 words.""")

def synthesize_speech(texting):
    text = f"{texting}"
    print(text)

    # Specify the model, voice, and input text
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file("output.mp3")
    # Define the path where the audio file will be saved
    temp_file = "./output.mp3"
    # Save the audio to a temporary file

    # response.stream_to_file(temp_file)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play the audio file
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up
    pygame.mixer.quit()
    os.remove(temp_file)

@app.route('/')
def home():
  return "I'm alive"


@app.route('/perform', methods=['POST'])
def original():
  data = request.get_json()
  print(data)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_to_text(f"uploads/{filename}")
        return 'File uploaded successfully', 200

def image_to_text(image_path):
    response = model.generate_content(
    glm.Content(
        parts=[
            glm.Part(
                text="Identify the monument in this picture and give me just its co-ordinates and location in json format "),
            glm.Part(
                inline_data=glm.Blob(
                    mime_type='image/jpeg',
                    data=pathlib.Path(f'{image_path}').read_bytes()
                )
            ),
        ],
    ),
    stream=True)

    response.resolve()
    print(response)
    print(response.candidates[0].content.parts[0].text)
    return response.candidates[0].content.parts[0].text

@app.route('/chat', methods=['POST'])
def start_conversation(image_ctx):
    print("Starting conversation...")
    if(image_ctx):
        data= image_ctx
    else:
        data= request.get_json()
    user_input = data['input']
    if user_input.lower() == "quit":
        return "Goodbye!"
    response = conversation.predict(input=user_input)
    print("Bot: ", response)
    flask_thread = threading.Thread(target=synthesize_speech, args=(response,))
    flask_thread.start()
    return response

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
   
    print(request.get_data())
    audio_data = request.get_json()['audio']
    decoded_data = base64.b64decode(audio_data)
    
    # Save the audio data to a temporary file
    with open('audio.webm', 'wb') as f:
        f.write(decoded_data)
    
    # Open the audio file for reading
    audio_file = open('audio.webm', "rb")
    
    # Transcribe the audio using OpenAI
    transcript = openai.audio.transcriptions.create(model="whisper-1", 
  file=audio_file)
    print(transcript.text)
    
    # Return the transcription result
    return transcript.text



def run():
  app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
  t = Thread(target=run)
  t.start()
# Replace with your OpenAI API key




if __name__ == "__main__":
    start_conversation()

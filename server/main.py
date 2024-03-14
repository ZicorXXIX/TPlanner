
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv() #
# os.environ["OPENAI_API_KEY"] = "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"
import requests
from flask_cors import CORS
from flask import Flask
from threading import Thread
import threading
from flask import Flask, request
import os
from openai import OpenAI
openai = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
import base64
import pygame
from pathlib import Path
app = Flask('')
CORS(app)
# socketio = SocketIO(app, cors_allowed_origins="*")

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

@app.route('/chat', methods=['POST'])
def start_conversation():
    print("Starting conversation...")
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

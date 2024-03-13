
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
os.environ["OPENAI_API_KEY"] = "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"
import requests
from flask_cors import CORS
from flask import Flask
from threading import Thread
from flask import Flask, request
import os
from openai import OpenAI
openai = OpenAI(api_key="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")
import base64
app = Flask('')
CORS(app)
# socketio = SocketIO(app, cors_allowed_origins="*")

from langchain import OpenAI, ConversationChain
llm= OpenAI(temperature=0.9)
conversation = ConversationChain(llm=llm, verbose=True)

conversation.predict(input="""Hi there,  You are a travel agent who helps users make exciting travel plans.

      Ask me a set of questions regarding my travel and plan an iternary for me. The iternary should have description of each day.
    """)


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
    return response

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
   
    print(request)
    audio_data = request.json['audio']
    decoded_data = base64.b64decode(audio_data)
    
    # Save the audio data to a temporary file
    with open('/tmp/audio.webm', 'wb') as f:
        f.write(decoded_data)
    
    # Open the audio file for reading
    audio_file = open('/tmp/audio.webm', "rb")
    
    # Transcribe the audio using OpenAI
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    
    # Return the transcription result
    return transcript



def run():
  app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
  t = Thread(target=run)
  t.start()
# Replace with your OpenAI API key




if __name__ == "__main__":
    start_conversation()
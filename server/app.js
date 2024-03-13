// server.js
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const multer = require('multer');
const openai = require('openai');

const app = express();

import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI();


// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(multer().any());

app.post('/api/transcribe', async (req, res) => {
    const transcription = await openai.audio.transcriptions.create({
        file: fs.createReadStream("/path/to/file/speech.mp3"),
        model: "whisper-1",
        response_format: "text",
      });
    
      console.log(transcription.text);
});

app.listen(3000, () => console.log('Server listening on port 3000'));
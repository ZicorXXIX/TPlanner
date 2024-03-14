import React from "react";
import "../App.css"
import axios from 'axios';


function MicrophoneButton({sendMessage}) {
    const [recording, setRecording] = React.useState(false);
    const [mediaRecorder, setMediaRecorder] = React.useState(null);
    const [chunks, setChunks] = React.useState([]);

    const handleClick = () => {
        if (recording) {
            mediaRecorder.stop();
        } else {
            navigator.mediaDevices.getUserMedia({ audio: true })
                .then(stream => {
                    const newMediaRecorder = new MediaRecorder(stream);
                    newMediaRecorder.ondataavailable = e => {
                        setChunks(prev => [...prev, e.data]);
                    };
                    setMediaRecorder(newMediaRecorder);
                    newMediaRecorder.start();
                });
        }
        setRecording(prevState => !prevState);
    };

    React.useEffect(() => {
        if (!recording && chunks.length) {
            const blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
            blob.arrayBuffer().then(buffer => {
                const base64Audio = btoa(
                    new Uint8Array(buffer)
                      .reduce((data, byte) => data + String.fromCharCode(byte), '')
                );
                axios.post('http://localhost:8080/transcribe', { audio: base64Audio })
                    .then((response) => {
                        console.log(response.data);
                        sendMessage(response.data);                        
                    });
            });
            setChunks([]);
        }
    }, [recording, chunks]);

    return (
        <button
            type="button"
            className={`inline-flex items-center px-4 py-2 border rounded-full shadow-sm text-sm font-medium ${recording ? 'bg-red-500 text-white' : 'bg-gray-300 text-gray-700'} hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500`}
            onClick={handleClick}
        >
            {recording ? 'Stop Recording' : 'Start Recording'}
        </button>
    );
}
export default function ChatBox(){
    const [messages, setMessages] = React.useState([]);
    const [query, setQuery] = React.useState('');
    console.log(query);
    function handleChange(e){
      setQuery(e.target.value);
      console.log(e.target.value);
      console.log(query);
    }
    function sendMessage(input){
      let data = JSON.stringify({
        "input": "[INST] "+input+" [/INST] "
      });
      
      let config = {
        method: 'post',
        maxBodyLength: Infinity,
        url: 'http://localhost:8080/chat',
        headers: { 
          'Content-Type': 'application/json'
        },
        data : data
      };
      
      axios.request(config)
      .then((response) => {
        console.log(response.data);
          setMessages([...messages,{generated_text: input, user: true}, {generated_text: response.data, user: false}]);
          console.log(messages)
      })
      .catch((error) => {
        console.log(error);
      });
    }

    function handleSubmit(e){
        e.preventDefault();
        console.log("indubml:",query);
        // setMessages([...messages, {generated_text: query, user: true}]);
        sendMessage(query);
        setQuery('');
    }
    return(
        <>
          
    <div id="chat-content" class="overflow-x-hidden">
        <div className="chat-messages" id="chat-messages">

            {messages?.map((message) => {

                return(<>
                    <div className={`messsage ${!message.user ? "bot" : "user" }`}>
                        <div className="message-content">
                        {message.generated_text}
                        </div>
                </div>

                </>)
            })}
        </div>
        <div class="chat-input">
        <form onSubmit={handleSubmit}>


            <input onChange={handleChange} type="text" id="user-input" value={query} placeholder="Plan your next trip..."></input>
            <button id="send-button">Send<div className="hoverEffect"><div></div></div></button>
            <MicrophoneButton className="record" sendMessage={sendMessage}/>

        </form>
        </div>
    </div>
    

        </>
    )
}



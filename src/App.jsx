import React, { useState } from 'react';
import styled from 'styled-components';
import axios from 'axios';
import SearchBar from './components/SearchBar';
import Home from './components/Home';
import ChatBox from './components/ChatBox';
import VoiceWidget from './components/VoiceWidget';


// const App = () => {
//  const [input, setInput] = useState('');
//  const [messages, setMessages] = useState([]);
// //  const [response, setResponse] = useState([]);

//  const sendMessage = async (input) => {
//   let data = JSON.stringify({
//     "input": "[INST] "+input+" [/INST] "
//   });
  
//   let config = {
//     method: 'post',
//     maxBodyLength: Infinity,
//     url: 'https://api.deepinfra.com/v1/inference/mistralai/Mixtral-8x7B-Instruct-v0.1',
//     headers: { 
//       'Content-Type': 'application/json'
//     },
//     data : data
//   };
  
//   axios.request(config)
//   .then((response) => {
//     console.log(response.data.results[0])
//     setMessages(JSON.stringify(response.data.results[0]));
//   })
//   .catch((error) => {
//     console.log(error);
//   });
// };

//  const handleInputChange = (e) => {
//     setInput(e.target.value);
//  };

//  const handleSendMessage = (e) => {
//     e.preventDefault();
//     const newMessage = sendMessage(input);
//     setInput('');
//  };

//  return (
//     <>
    //   <div id="about-us">
    //     <h1>Travel Buddy</h1>
    //     <p>This travel chatbot is a cutting-edge digital assistant designed to enhance the travel experience 
    //         for users. This virtual companion is equipped with the ability to converse with travelers, 
    //         providing them with valuable information, recommendations, and assistance throughout their journey.</p>
    // </div>
    // <div class="chat-content">
    //     <div class="chat-messages" id="chat-messages">

    //     </div>
    //     <div class="chat-input">
    //         <input type="text" id="user-input" placeholder="Plan your next trip..."></input>
    //         <button id="send-button">Send<div class="hoverEffect"><div></div></div></button>
    //     </div>
    // </div>
  
    // <div class="content-center">
    //     <ul>
        
    //         <li><a href="https://www.linkedin.com/in/dharam-veer-726366245/" target="_blank"><i class="fa fa-twitter fa-2x"></i></a></li>
    //         <li><a href="https://www.linkedin.com/in/dharam-veer-726366245/" target="_blank"><i class="fa fa-linkedin fa-2x"></i></a></li>
    //         <li><a href="https://www.instagram.com/veer_9457/" target="_blank"><i class="fa fa-instagram fa-2x"></i></a></li>
    //     </ul>   
    // </div>

    //  <div id="image-dialog" class="hidden">
    //     <div id="image-container"></div>
    //     <button id="close-dialog">Close</button>
    // </div>
//     </>
//  );
// };

// export default App;


export default function App() {
  return (
    <>

    {/* <Home /> */}
    <ChatBox />
    {/* <VoiceWidget /> */}
    </>
  );
}
  


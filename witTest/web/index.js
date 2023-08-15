// script.js
document.addEventListener('DOMContentLoaded', function () {
  const chatMessages = document.getElementById('chat-messages');
  const userInput = document.getElementById('user-input');

  var myresponse = ""

  userInput.addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
      const userMessage = userInput.value;
      displayMessage(userMessage, 'user');

      // Send user message to chatbot API and get bot response
      const botResponse = getBotResponse(userMessage);

      botResponse.then((value) => {
      console.log(value);
        displayMessage(value, 'bot')
        });

      // Display bot response
      //displayMessage(botResponse, 'bot');

      userInput.value = ''; // Clear user input
    }
  });

  function displayMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
  }

  function getBotResponse(userMessage) {
    // Use your chosen chatbot API to send userMessage and receive bot response
    // Replace this with actual API call
     botResponse = 'Bot: This is a sample response.';


    let  apiUrl = 'http://127.0.0.1:8080/get-resp/?text=';
    let p = userMessage;
    apiUrl = apiUrl+p;
    try {
      const responseData = fetchDataSynchronously(apiUrl);
      return  responseData
    } catch (error) {
      console.error('An error occurred:', error);
      }

  }

  function  processInput(){
    const uri = 'http://127.0.0.1:8080/get-resp/?text=hi'
   fetch(uri)
  .then(res => res.text())
  .then(res => {
      console.log(res)
    return res
  }

  )
}


//-------
  async function fetchDataSynchronously(url) {
  try {
    const response = await fetch(url); // Make an asynchronous fetch request
    const data = await response.text(); // Parse the response
    console.log("*****",data)
    myresponse = data;
    return data;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

});
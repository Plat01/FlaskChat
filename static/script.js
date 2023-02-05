// Get the chat form and input field
const chatForm = document.querySelector('#chat-form');
const messageInput = document.querySelector('#message-input');

// Get the chat container
const chatContainer = document.querySelector('.chat-container');

// Add a new message to the chat container
function addMessage(username, message) {
  // Create a new chat message element
  const chatMessage = document.createElement('div');
  chatMessage.classList.add('chat-message');

  // Create the message text
  const messageText = document.createElement('p');
  messageText.innerHTML = `<strong>${username}:</strong> ${message}`;

  // Add the message text to the chat message element
  chatMessage.appendChild(messageText);

  // Add the chat message to the chat container
  chatContainer.appendChild(chatMessage);
}

// Submit the chat form
chatForm.addEventListener('submit', (event) => {
  event.preventDefault();

  // Get the message from the input field
  const message = messageInput.value;

  // Add the message to the chat container
  addMessage('User', message);

  // Clear the input field
  messageInput.value = '';
});


const chatButton = document.getElementById('chat-button');
const chatBox = document.getElementById('chat-box');
const closeChat = document.getElementById('close-chat');
const sendButton = document.getElementById('send-button');
const chatContent = document.getElementById('chat-content');
const chatInputText = document.getElementById('chat-input-text');

chatButton.addEventListener('click', function() {
    if (chatBox.style.display === 'flex') {
        chatBox.style.display = 'none';
    } else {
        chatBox.style.display = 'flex';
    }
});

closeChat.addEventListener('click', function() {
    chatBox.style.display = 'none';
});

sendButton.addEventListener('click', function() {
    const message = chatInputText.value.trim();
    if (message) {
        const messageElement = document.createElement('p');
        messageElement.textContent = message;
        chatContent.appendChild(messageElement);
        chatInputText.value = '';
        chatContent.scrollTop = chatContent.scrollHeight; // Scroll to the bottom
    }
});

//chatbot END
// CHATBOT API CALL
$(document).ready(function() {
    // On send button click
    $("#send-button").click(function() {
        var userInput = $("#chatinputtext").val(); // Get user input
        if (userInput.trim() !== "") {
            // Add user's message to chat content
            $("#chat-content").append('<div class="message user"> <i class="material-icons icon">account_circle</i>' + userInput + '</div>');

            // Clear the input field
            $("#chatinputtext").val('');

            // Send the message to the backend and get the response
            $.ajax({
                url: 'https://bpxai.pythonanywhere.com/message/' + encodeURIComponent(userInput), // Encode the user input for URL safety
                type: 'GET',
                contentType: 'application/json',
                success: function(response) {
                    var botResponse = response.response;

                    // Add bot's response to chat content
                    $("#chat-content").append('<div class="message bot"> <i class="material-icons">android</i>' + botResponse + '</div>');

                    // Scroll to the bottom of the chat content
                    $("#chat-content").scrollTop($("#chat-content")[0].scrollHeight);
                },
                error: function() {
                    // Handle errors
                    $("#chat-content").append('<div class="message bot"><i class="fas fa-robot text-large"></i>Sorry, something went wrong.</div>');
                }
            });
        }
    });
});

// Function to handle the Enter key press
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the default action (form submission, etc.)
        
        // Trigger the click event on the button with id 'sendbtn'
        document.getElementById('send-button').click();
    }
});
import streamlit as st
import requests

# Streamlit App Title
st.title('AI Chatbot')

# A placeholder for chat history
chat_history = st.empty()

# Session state for storing conversation history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to send the message to the Flask backend and get a response
def get_chatbot_response(user_input):
    try:
        # Send a POST request to the Flask backend
        response = requests.post('http://localhost:5000/chat', json={'message': user_input})
        # Return the response from the backend
        return response.json().get('response', 'No response from the chatbot')
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# User input field
user_input = st.text_input("You:", placeholder="Type your message here...")

# If the user submits a message
if user_input:
    # Add user message to the session state
    st.session_state['messages'].append(('user', user_input))
    
    # Get the chatbot's response from the Flask backend
    bot_response = get_chatbot_response(user_input)
    
    # Add chatbot's response to the session state
    st.session_state['messages'].append(('bot', bot_response))

# Display chat history
for role, message in st.session_state['messages']:
    # if role == 'user':
    #     st.write(f"**You**: {message}")
    # else:
    #     st.write(f"**AI**: {message}")
    if role == 'user':
        # Highlight user question in red
        st.markdown(f"<div style='background-color: #FA6B84; color: black; padding: 10px; border-radius: 5px; margin-top: 15px'>👦: {message}</div>", unsafe_allow_html=True)
    else:
        # Highlight AI response in green
        st.markdown(f"<div style='background-color: #DAFFD5; color: black; padding: 10px; border-radius: 5px; margin-top: 5px'>🤖: {message}</div>", unsafe_allow_html=True)

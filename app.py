# app.py
import streamlit as st
from listen import listen
from aut import authenticate_google_calendar
from calendar_utils import create_appointment
import datetime
import nltk
from chatbot import initialize_textblob

# Call the initialization function to ensure TextBlob is ready
initialize_textblob()




# Set up Google Calendar API credentials
creds = authenticate_google_calendar()

# Streamlit UI
st.title("Dental Clinic Virtual Assistant")
st.write("Hi! I'm here to help you with appointment scheduling and any questions you have.")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Start listening for voice input on button click
if st.button("Start Listening"):
    user_response, response_text = listen()
    # Append both user and bot messages to chat history
    st.session_state.chat_history.append(("user", user_response))
    st.session_state.chat_history.append(("bot", response_text))

# Display chat messages
if st.session_state.chat_history:
    st.subheader("Chat History")
    for role, message in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"**You:** {message}")
        elif role == "bot":
            st.markdown(f"**Bot:** {message}")

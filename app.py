# app.py
# This is the main file you run. It builds the Streamlit UI and wires
# together extractor.py + vector_store.py + chatbot.py

import streamlit as st
from dotenv import load_dotenv

from extractor import get_video_id, get_transcript
from vector_store import build_vector_store
from chatbot import ask_question

# Load GROQ_API_KEY from the .env file into the environment variables
load_dotenv()


st.set_page_config(page_title="YouTube Video Chatbot")
st.title("YouTube Video Chatbot")
st.write("Paste a YouTube link, then ask questions about the video's content.")

# session_state keeps the vector store alive between Streamlit reruns
# (Streamlit reruns the whole script top-to-bottom on every interaction)
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# --- Step 1: video input ---
youtube_url = st.text_input("YouTube video URL")

if st.button("Load Video"):
    video_id = get_video_id(youtube_url)
    transcript_text = get_transcript(video_id)

    if transcript_text is None:
        # This is the warning the task asked for: no subtitles available
        st.warning("This video doesn't contain subtitles, so its content can't be extracted.")
    else:
        with st.spinner("Reading the video and building the vector database..."):
            st.session_state.vector_store = build_vector_store(transcript_text)
        st.success("Video loaded. You can ask questions below.")

# --- Step 2: question input (only shown once a video is loaded) ---
if st.session_state.vector_store is not None:
    st.divider()
    user_question = st.text_input("Ask a question about the video")

    if st.button("Get Answer"):
        with st.spinner("Thinking..."):
            answer = ask_question(st.session_state.vector_store, user_question)
        st.write(answer)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# YouTube Video Chatbot (LangChain + Groq + FAISS + Streamlit)

A RAG chatbot that answers questions about a YouTube video using its subtitles.

## How it works (the 4 files)
- `extractor.py` — pulls the video id from the URL and fetches subtitles
- `vector_store.py` — splits the transcript into chunks and stores them in FAISS
- `chatbot.py` — retrieves relevant chunks and asks Groq's LLM to answer
- `app.py` — the Streamlit page that ties all three together

## Step-by-step setup

### 1. Create the project folder
Create a new empty folder anywhere on your computer, e.g. `youtube_chatbot`,
and open it in VS Code (`File > Open Folder`).

### 2. Add the 6 files
Put `app.py`, `extractor.py`, `vector_store.py`, `chatbot.py`,
`requirements.txt`, and `.env.example` directly inside that folder.

### 3. Create a virtual environment
Open the VS Code terminal (`Terminal > New Terminal`) and run:
```
python -m venv venv
```
Activate it:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### 4. Install the dependencies
```
pip install -r requirements.txt
```

### 5. Get a free Groq API key
Go to https://console.groq.com/keys, sign up, and create a key.

### 6. Create your .env file
Copy `.env.example`, rename the copy to `.env`, and paste your key in:
```
GROQ_API_KEY=your_actual_key_here
```

### 7. Run the app
```
streamlit run app.py
```
This opens the app in your browser (usually `http://localhost:8501`).

### 8. Use it
1. Paste a YouTube video URL and click **Load Video**.
   - If the video has subtitles, it gets chunked and stored in FAISS.
   - If it has no subtitles, you'll see a warning instead of a crash.
2. Type a question about the video and click **Get Answer**.
3. The app retrieves the most relevant transcript chunks and Groq's
   LLM answers using only that content.
=======
# YouTube_ChatBot
>>>>>>> 0a76fcfc057b64a433b0afe96f52ed67db035bc2
=======
# YouTube_ChatBot
>>>>>>> 0a76fcfc057b64a433b0afe96f52ed67db035bc2
=======
# YouTube_ChatBot
>>>>>>> 0a76fcfc057b64a433b0afe96f52ed67db035bc2
=======
# YouTube_ChatBot
>>>>>>> 0a76fcfc057b64a433b0afe96f52ed67db035bc2
=======
# YouTube_Video-_Chatbot
>>>>>>> 1454944c6549e92bc346616ffc50562ae3063dd5

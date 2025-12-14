# Google File Search with Streamlit

A Streamlit application that uses Google's Generative AI File Search to answer questions about uploaded PDF documents.

## Features

- Upload PDF documents to Google's File Search store
- Ask questions about the document content
- Get AI-powered answers using Gemini 2.5 Flash

## Setup

1. Get a Google API key from [Google AI Studio](https://aistudio.google.com/apikey)

2. Set the API key as an environment variable:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

3. Install dependencies:
```bash
pip install google-genai streamlit
```

4. Run the application:
```bash
streamlit run gfs.py
```

## Usage

Place your PDF file (e.g., `Tesla_Model_Y_Owners_Manual.pdf`) in the project directory and run the application. The app will upload the document and allow you to ask questions about its content.

## Requirements

- Python 3.7+
- google-genai
- streamlit

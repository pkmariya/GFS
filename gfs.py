import time
import os
from google import genai
from google.genai import types
import streamlit as st

# Get API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please set it with your API key.")

client = genai.Client(api_key=api_key)
store = client.file_search_stores.create()

upload_op = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=store.name,
    file = "Tesla_Model_Y_Owners_Manual.pdf",
    config={
        'chunking_config':{
            'white_space_config':{
                'max_tokens_per_chunk': 200,
                'max_overlap_tokens': 20
            }
        }
    }
)

while not upload_op.done:
    time.sleep(1)
    print("Upload in progress...")
    upload_op = client.operations.get(upload_op)

print("Upload completed successfully.")

def get_answer(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
        config=types.GenerateContentConfig(
            tools=[types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[store.name]
                )
            )]
        )
    )
    return response.text

st.title("Tesla Model Y Owner's Manual Q&A")
question = st.text_input("Ask a question about the Tesla Model Y Owners Manual:")

if question:
    answer = get_answer(question)
    st.header("Answer:")
    st.write(answer)
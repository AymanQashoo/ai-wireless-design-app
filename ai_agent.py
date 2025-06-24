# ai_agent.py

import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def explain_results(results_dict: dict) -> str:
    prompt = (
        "Please explain the following wireless system output values in simple terms for a student:\n\n"
    )
    for key, value in results_dict.items():
        prompt += f"{key}: {value}\n"

    # Make the request to OpenAI
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who explains wireless communication system outputs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()

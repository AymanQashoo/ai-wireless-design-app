# ai_agent.py

import streamlit as st
from openai import OpenAI

# Load OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def explain_results(results_dict):
    prompt = (
        "You are an expert in wireless communication systems. "
        "Please explain the following results in clear and simple terms:\n\n"
        f"{results_dict}\n\n"
        "The explanation should be educational and easy to understand for students."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Failed to generate explanation: {e}"

import google.generativeai as genai
import streamlit as st

# Configure Gemini with the API key stored in Streamlit secrets
genai.configure(api_key=st.secrets["general"]["GEMINI_API_KEY"])


# Create a Gemini model instance
model = genai.GenerativeModel("gemini-pro")

def explain_results(topic, results):
    prompt = (
        f"You are an expert in wireless and mobile communication systems.\n"
        f"Explain the following {topic.replace('_', ' ')} calculation results in simple, clear terms:\n"
        f"{results}\n"
        f"Use bullet points if helpful and make it understandable for engineering students."
    )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error generating explanation: {str(e)}"

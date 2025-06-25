import streamlit as st
import openai

# Load API key from Streamlit secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def explain_results(topic, results):
    prompt = (
        f"You are an expert in wireless and mobile communication systems.\n"
        f"Explain the following {topic.replace('_', ' ')} calculation results in simple, clear terms:\n"
        f"{results}\n"
        f"Use bullet points if helpful and make it understandable for engineering students."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that explains telecom engineering calculations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Error generating explanation: {str(e)}"

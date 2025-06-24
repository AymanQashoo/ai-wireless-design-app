# ai_agent.py
import openai
import os

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_results(topic, results_dict):
    """
    Sends the scenario results to GPT and returns a natural language explanation.
    """
    prompt = f"""
    I am working on wireless network design. Please explain the following {topic.replace('_', ' ')} results in simple language:

    {results_dict}

    Make it clear and concise for a student with an engineering background.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in wireless and mobile network engineering."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        explanation = response['choices'][0]['message']['content']
        return explanation
    except Exception as e:
        return f"Error generating explanation: {e}"

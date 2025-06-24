import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_results(topic, results_dict):
    prompt = f"""
    I am working on wireless network design. Please explain the following {topic.replace('_', ' ')} results in simple language:\n\n
    {results_dict}\n\n
    Make it clear and concise for an engineering student.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a wireless network engineering assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating explanation: {e}"

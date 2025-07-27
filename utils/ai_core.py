import openai
import os

# Load your OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recommendation(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Error: {e}"

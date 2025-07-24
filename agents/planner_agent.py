from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def planner_agent(user_input: str) -> dict:
    print("[Planner Agent] Interpreting user input...")

    prompt = f"""
You are a travel planner AI. Extract structured data from the request below:

"{user_input}"

Return a JSON object with:
- origin
- destination
- departure_date (YYYY-MM-DD)
- return_date (YYYY-MM-DD)
- preferences (hotel stars, location, etc.)

Return only the JSON.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    try:
        output = response.choices[0].message.content.strip()
        data = eval(output)  # safer: use `json.loads()` if GPT is clean
        return data
    except Exception as e:
        print("Parsing error:", e)
        return {}

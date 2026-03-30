from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_reviews_with_llm(reviews):
    prompt = f"""
You are an AI that analyzes product reviews.

Reviews:
{reviews}

Return STRICTLY in this format:

Top Complaints:
- ...

Top Praises:
- ...

Key Insights:
- ...

Suggested Improvements:
- ...
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
from google import genai
import os
import json

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_reviews_with_llm(reviews):
    prompt = f"""
You are an AI that analyzes product reviews.

Reviews:
{reviews}

Return ONLY valid JSON in this format:

{{
  "complaints": ["..."],
  "praises": ["..."],
  "insights": ["..."],
  "improvements": ["..."]
}}

Rules:
- Only JSON
- No explanation
- No markdown
- Keep points short
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        raw_text = response.text.strip()

        # 🔥 Handle markdown issues (VERY IMPORTANT)
        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]

        parsed = json.loads(raw_text)

        return parsed

    except Exception as e:
        return {"error": str(e)}
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

GENAI_API_KEY = os.getenv("GENAI_API_KEY")

client = genai.Client(
    api_key=GENAI_API_KEY
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello, are you working?"
)

print(response.text)

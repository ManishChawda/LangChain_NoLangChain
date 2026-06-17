from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLEGENERATIVEAI_API_KEY = os.getenv("GOOGLEGENERATIVEAI_API_KEY")
print("KEY =", GOOGLEGENERATIVEAI_API_KEY)

# Get a free key at: https://aistudio.google.com
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLEGENERATIVEAI_API_KEY)

response = llm.invoke("Hello, are you working?")
print(response.content)

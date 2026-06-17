from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# 1. Initialize the Groq model
# Replace "YOUR_GROQ_API_KEY" with your actual key from console.groq.com
llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    groq_api_key=GROQ_API_KEY
)

print("--- Groq Chatbot Started (Type 'exit' or 'quit' to stop) ---")

# 2. Start the interactive loop
while True:
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    try:
        # 3. Get response from Groq
        response = llm.invoke(user_input)
        print(f"Bot: {response.content}\n")
    except Exception as e:
        print(f"Error: {e}")


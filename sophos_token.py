from dotenv import load_dotenv
import requests
import os

load_dotenv()

# 🔐 Replace with your values
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

url = "https://id.sophos.com/api/v2/oauth2/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "token"
}

response = requests.post(url, headers=headers, data=data)

print("Status Code:", response.status_code)
print("Response:", response.text)

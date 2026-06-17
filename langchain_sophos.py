from langchain_groq import ChatGroq
from dotenv import load_dotenv
import requests
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# 🔐 Groq API
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

# 🔐 Sophos credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# 🔹 Step 1: Get Access Token
def get_access_token():
    url = "https://id.sophos.com/api/v2/oauth2/token"
    
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "token"
    }

    response = requests.post(url, data=data)
    print("\n[DEBUG] Token Response:", response.text)  # 👈 debug
    return response.json()["access_token"]

# 🔹 Step 2: Get Tenant + Region
def get_tenant_and_region(token):
    url = "https://api.central.sophos.com/whoami/v1"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    print("\n[DEBUG] WhoAmI Response:", response.text)  # 👈 debug

    return response.json()

# 🔹 Step 3: Get Devices
def get_devices():
    token = get_access_token()

    info = get_tenant_and_region(token)

    tenant_id = info["id"]
    api_host = info["apiHosts"]["dataRegion"]

    print("\n[DEBUG] Tenant ID:", tenant_id)
    print("[DEBUG] API Host:", api_host)

    url = f"{api_host}/endpoint/v1/endpoints"

    headers = {
        "Authorization": f"Bearer {token}",
        "X-Tenant-ID": tenant_id
    }

    print("[DEBUG] Final URL:", url)

    response = requests.get(url, headers=headers)

    print("\n[DEBUG] Devices Response:", response.text)

    return response.text

# Step 4: Get Firewall
def get_firewalls():
    token = get_access_token()
    info = get_tenant_and_region(token)

    tenant_id = info["id"]
    api_host = info["apiHosts"]["dataRegion"]

    url = f"{api_host}/firewall/v1/firewalls"

    headers = {
        "Authorization": f"Bearer {token}",
        "X-Tenant-ID": tenant_id
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    result = []

    for fw in data.get("items", []):
        name = fw.get("hostname")
        model = fw.get("model")
        ip = fw.get("externalIpv4Addresses", [])
        status = fw.get("status", {}).get("connected")

        result.append(f"{name} | {model} | IP: {ip} | Online: {status}")

    return "\n".join(result)



# 🔹 Chat Loop
print("Chat started (type exit to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    elif "devices" in user_input.lower():
        result = get_devices()
        print("Bot:", result)
    
    elif "info" in user_input.lower():
        token = get_access_token()
        info = get_tenant_and_region(token)
        print("Bot:", info)
    
    elif "mcp" in user_input.lower():
        result = get_firewalls()
        print([line for line in result.split("\n") if "MCP" in line])

    elif "grkl" in user_input.lower():
        result = get_firewalls()
        print([line for line in result.split("\n") if "GRKL" in line])

    elif "firewall" in user_input.lower() or "sophos" in user_input.lower():
        result = get_firewalls()
        print("Bot:", result)
    
    else:
        response = llm.invoke(user_input)
        print("Bot:", response.content)

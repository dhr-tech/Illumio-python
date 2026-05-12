import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =========================
# Configuration
# =========================
ORG_ID = "3735772"
IP_LIST_ID = "16044073672512345"      # <-- CHANGE THIS
BASE_URL = f"https://uk-scp53.illum.io/api/v2/orgs/{ORG_ID}"

AUTH = HTTPBasicAuth(
    "api_1670c2de4c591c5b1",
    "6ea0f9e2dc858a1cc2ece7f7df259664e4c79c09f7dd2ce7e83ca77f635226cf"
)

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# =========================
# Updated IP list payload
# =========================
payload = {
    "name": "My_IP_List",                       # REQUIRED
    "description": "Updated via automation",    # Optional
    "ip_ranges": [
        {
            "from_ip": "10.10.10.0",
            "to_ip": "10.10.10.255",
            "description": "Internal subnet"
        },
        {
            "cidr_block": "192.168.50.0/24",
            "description": "Branch network"
        }
    ]
}

# =========================
# PUT request
# =========================
url = f"{BASE_URL}/sec_policy/active/ip_lists/{IP_LIST_ID}"

response = requests.put(
    url,
    auth=AUTH,
    headers=HEADERS,
    json=payload,
    verify=False
)

response.raise_for_status()

print("✅ IP list updated successfully")
print(json.dumps(response.json(), indent=2))
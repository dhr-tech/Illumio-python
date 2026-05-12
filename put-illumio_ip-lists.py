import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =========================
# Configuration
# =========================
ORG_ID = "vvvv"
IP_LIST_ID = "vvvv"
BASE_URL = f"https://uk-scp53.illum.io/api/v2/orgs/{ORG_ID}"

AUTH = HTTPBasicAuth(
    "api_xxxxxx",
    "yyyyyyyyyyyyyyyyyyyyyyyyy"
)

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# =========================
# PUT payload (FULL list)
# =========================
payload = {
    "name": "IPL-AZUREIP",   # ✅ REQUIRED
    "description": (
        "https://learn.microsoft.com/en-us/azure/virtual-network/"
        "what-is-ip-address-168-63-129-16?tabs=windows"
    ),
    "ip_ranges": [
        {
            "from_ip": "y.y.y.y",
            "to_ip": "x.x.x.x",
            "description": "Azure platform internal IP"
        }

        # ✅ Add more entries here if needed
        # {
        #     "cidr_block": "20.190.128.0/18",
        #     "description": "Azure public endpoints"
        # }
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

print("✅ IP list updated successfully:")
print(json.dumps(response.json(), indent=2))

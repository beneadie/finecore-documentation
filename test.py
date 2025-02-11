import requests
import json

url = " https://stagingapi.finecore.co/v1/wallets"
api_key = "flk_6f1025328641a6b2b3b309cee58a27aa_1784140885"  # Replace with your actual API key

payload = {
    "bvn": "11317307123",
    "first_name": "Ben",
    "last_name": "Testing",
    "date_of_birth": "12-11-2003",
    "phone_number": "08023094123",
    "email": "bentesting2024@finecore.co",
    "address": "No 10, Adewale Ajasin University"
}

headers = {
    "Content-Type": "application/json",
    "X-API-Key": api_key
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    print("Success!")
    print(json.dumps(response.json(), indent=2))
else:
    print("Failed with status code:", response.status_code)
    print(response.text)

import requests
import json

def get_public_ip():
    response = requests.get("https://api.ipify.org/?format=json")
    return response.json()["ip"] 

message = get_public_ip()
WEBHOOK_URL = "https://discord.com/api/webhooks/1477078144342294528/61j1vgbKugt7-DoUsp55bj1SW96U2YW4JOw4WX7mEQQGZAKB3QZ54IGw-9npd8j1nvty"
def send_discord_message(message):
    payload = {
        "content": message
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)

send_discord_message()

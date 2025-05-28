import requests
from config import WEBHOOK_URL

class Web:
    def __init__(self):
        self.session = requests.Session()
        self.pomelo_url = "https://discord.com/api/v9/users/@me/pomelo-attempt"

    def send_webhook(self, message):
        try:
            r = self.session.post(
                WEBHOOK_URL,
                json={"content": message},
                timeout=10
            )
            if r.status_code in [200, 204]:
                print("[+] Webhook sent")
            else:
                print(f"Failed to send webhook: {r.status_code} - {r.text}")
        except requests.exceptions.RequestException as e:
            print(f"Webhook request error: {e}")

    def check_user(self, token:str, username:str):
        try:
            r = self.session.post(
                self.pomelo_url,
                headers = {"Authorization": token,"content-type": "application/json"},
                json={"username": username},
                timeout = 10
            )
            if r.status_code == 401:
                print(f"[!] Unauthorized Token | {token}")
            else:
                data = r.json()
                if data.get("taken") is True:
                    print(f"[-] @{username} is taken")
                else:
                    print(f"[+] @{username} is available")
                    self.send_webhook(message=f"> **`@{username}` is available!**")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {username} - {e}")
        except Exception as e:
            print(f"Error: {username} - {e}")
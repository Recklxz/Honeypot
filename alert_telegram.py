import time, requests
LOG_PATH = "/home/pablo/Desktop/Honeypot/cowrie/var/log/cowrie/cowrie.log"

TOKEN = "7654314138:AAH9a1QR7RmTCheEnBm3Ag0SrZzOoL--HsQ"
CHAT_ID = "5842861982"

def send(msg):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})

def monitor():
    with open(LOG_PATH, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if "New connection" in line:
                send(f"[Cowrie Alert] {line.strip()}")
monitor()

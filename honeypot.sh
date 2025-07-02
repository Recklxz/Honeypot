#!/bin/bash
echo "[+] Activating virtual environment..."
source cowrie/cowrie-env/bin/activate || { echo "❌ Failed to activate env"; exit 1; }

echo "[+] Starting Cowrie honeypot..."
cd cowrie
bin/cowrie start >> ../cowrie_start.log 2>&1 &
cd ..

echo "[+] Starting Telegram alert script..."
python3 alert_telegram.py >> telegram.log 2>&1 &

echo "[+] Starting Logstash..."
logstash -f cowrie.conf >> logstash.log 2>&1 &

echo "[+] Starting Flask dashboard..."
python3 app.py >> flask.log 2>&1 &

echo "[✓] All services started successfully!"


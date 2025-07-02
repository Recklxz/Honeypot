#!/bin/bash

echo "[×] Stopping Cowrie..."
cd cowrie && bin/cowrie stop
cd ..

echo "[×] Stopping Telegram alert script..."
pkill -f alert_telegram.py

echo "[×] Stopping Logstash..."
sudo pkill -f logstash

echo "[×] Stopping Flask app..."
pkill -f app.py

echo "[✓] All services stopped!"

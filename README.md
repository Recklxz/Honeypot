# 🕵️ Honeypot Logging & Monitoring System

A secure and scalable honeypot project using **Cowrie**, deployed with **Docker**, integrated with the **ELK stack** for real-time log visualization, and optional **Telegram/Email alerts** for suspicious activities.

---

## 🔧 Project Structure

```
.
├── cowrie/                 # Cowrie honeypot (Dockerized)
│   └── cowrie.env          # Python virtual environment
├── elasticsearch/          # Elasticsearch configuration
├── kibana/                 # Kibana dashboard service
├── logstash/               # Logstash pipeline config
│   └── cowrie.conf         # Custom Logstash config
├── alert_telegram.py       # Sends alerts on attack detection
├── flask_dashboard/        # Flask + Bootstrap dashboard
├── honeypot.sh             # Startup script
└── docker-compose.yml      # Container orchestration
```

---

## ⚙️ Features

- 🐍 **Cowrie Honeypot** – Logs SSH/Telnet intrusion attempts.
- 📊 **Logstash + Elasticsearch** – Parses & stores logs.
- 📈 **Kibana** – Visualize attacks (IPs, timestamps, commands).
- 📬 **Alerting System** – Sends alerts via Telegram or Email.
- 🌐 **Flask Dashboard** – Simple frontend to view logs live.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/honeypot-monitoring
cd honeypot-monitoring
```

### 2. Start Docker containers

```bash
sudo docker-compose up -d
```

This will start:
- Cowrie
- Logstash
- Elasticsearch
- Kibana

Make sure Docker is installed.

### 3. Set Telegram Bot Token or Email Credentials

Edit `alert_telegram.py`:

```python
BOT_TOKEN = 'your_bot_token'
CHAT_ID = 'your_chat_id'
```

Or configure SMTP if using email alerts.

### 4. Run the alert script

```bash
python3 alert_telegram.py
```

### 5. Launch the Flask Dashboard

```bash
cd flask_dashboard
python3 app.py
```

Access it at: `http://127.0.0.1:5000`

---

## 📦 Logstash Configuration

Located in `logstash/cowrie.conf`:

```conf
input {
  file {
    path => "/home/pablo/Desktop/Honeypot/cowrie/var/log/cowrie/cowrie.json"
    start_position => "beginning"
    sincedb_path => "/dev/null"
    codec => json
  }
}

filter {
  grok {
    match => { "message" => "%{TIMESTAMP_ISO8601:timestamp}.*New connection.*" }
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "cowrie-attacks"
  }
}
```

---

## 🛡️ Security Tips

- Never run Cowrie as root (`cowrie` will warn you).
- Restrict access to Kibana (it’s unauthenticated by default).
- Use `fail2ban` or IPTables to block repeated attackers if needed.

---

## 🖥️ Screenshots

> _Add screenshots of Kibana dashboards, logs, and the Flask UI here._

---

## 📜 License

MIT License. See `LICENSE` file.

---

## 🤝 Contributions

Contributions, issues and suggestions are welcome! Feel free to submit pull requests.

---

## 👨‍💻 Author

**Anmol Kool**  
🔗 [LinkedIn](https://www.linkedin.com/in/anmol-kool)  
📁 [GitHub](https://github.com/Recklxz)
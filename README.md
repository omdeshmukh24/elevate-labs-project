# 🔧 Self-Healing Infrastructure using Prometheus, Alertmanager & Ansible

This project demonstrates how to build a self-healing infrastructure using **Prometheus** for monitoring, **Alertmanager** for alerting, and **Ansible** to automatically recover from failures (e.g., restart services like NGINX).

---

## 📁 Project Structure

```
self-healing/
├── alertmanager/
│   └── alertmanager.yml        
├── ansible/
│   └── restart_service.yml     
├── prometheus/
│   ├── prometheus.yml
    └── alert.rules.yml         
├── webhook/
│   └── webhook.py              
├── restart_nginx.yml           
└── venv/                       
```

---

## ⚙️ Prerequisites

- Docker & Docker Compose
- Python 3
- Ansible
- Node Exporter (for system metrics)
- `nginx` installed and running
- SMTP service (for email alerts - optional)

---

## 🔌 Step-by-Step Setup

### 1. Clone the Project

```bash
git clone https://github.com/your-username/self-healing.git
cd self-healing
```

---

### 2. Start Prometheus

```bash
sudo docker run -d --name prometheus -p 9090:9090 \
  -v ~/self-healing/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
  -v ~/self-healing/prometheus/alert.rules.yml:/etc/prometheus/alert.rules.yml \
  prom/prometheus
```

---

### 3. Start Alertmanager

```bash
sudo docker run -d --name alertmanager -p 9093:9093 \
  -v ~/self-healing/alertmanager/alertmanager.yml:/etc/alertmanager/alertmanager.yml \
  prom/alertmanager
```

---

### 4. Start Node Exporter (System Metrics)

```bash
sudo docker run -d --name node_exporter -p 9100:9100 prom/node-exporter
```

---

### 5. Run Flask Webhook Listener

#### Create and activate virtual environment:

```bash
cd webhook/
python3 -m venv venv
source venv/bin/activate
pip install flask
```

#### Run the Flask App:

```bash
nohup python3 webhook.py &
```

---

### 6. Setup Ansible Playbook

Edit the playbook to restart nginx:

```yaml
# ansible/restart_service.yml
---
- hosts: localhost
  become: true
  tasks:
    - name: Restart NGINX
      service:
        name: nginx
        state: restarted
```
---

## 📊 Dashboards

- **Prometheus**: [http://localhost:9090](http://localhost:9090)
- **Alertmanager**: [http://localhost:9093](http://localhost:9093)
- **Node Exporter**: [http://localhost:9100/metrics](http://localhost:9100/metrics)

---



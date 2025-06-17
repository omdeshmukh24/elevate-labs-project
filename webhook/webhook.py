from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", data)

    # Optional: Add filtering logic to trigger only specific alerts

    # Run the Ansible playbook
    subprocess.run(["ansible-playbook", "/home/ubuntu/self-healing/ansible/restart_service.yml"])

    return "Ansible playbook triggered!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

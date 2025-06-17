from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert: ", data)
    os.system("ansible-playbook restart_nginx.yml")
    return "OK", 200

app.run(port=5001)

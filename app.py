from flask import Flask, request
import requests, os
app = Flask(__name__)
WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")
PHONE_ID = os.environ.get("PHONE_ID")
OWNER = "94740370707"

@app.route('/')
def home():
    return "FashionBee Bot LIVE 0740370707"

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == 'fashionbee123':
            return request.args.get('hub.challenge')
        return "error"
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

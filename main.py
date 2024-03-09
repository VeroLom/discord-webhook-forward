from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/webhook', methods=['GET'])
def webhook():
    #data = request.json

    webhook_id = request.args.get('webhook_id')
    token = request.args.get('token')

    response_data = {
        "content": f"New transaction catched:\n```json\n{data}\n```"
    }

    webhook_url = f"https://discordapp.com/api/webhooks/{webhook_id}/{token}"
    response = requests.post(webhook_url, json=response_data)

    if response.status_code == 200:
        return jsonify({'result': True}), 200
    else:
        return jsonify({'error': f'Failed to send webhook: {response.text}'}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
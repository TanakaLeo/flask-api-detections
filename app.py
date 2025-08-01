from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "API de detecção YOLO está ativa."

@app.route('/detections', methods=['POST'])
def receber_dados():
    data = request.get_json()
    objetos = data.get('objetos')
    tempo = data.get('tempo_ms')
    timestamp = datetime.now().isoformat()

    print(f"[{timestamp}] Objetos: {objetos} ({tempo}ms)")
    return jsonify({"status": "recebido"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

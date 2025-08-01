from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "API de detecção YOLO está ativa."

@app.route('/detections', methods=['POST'])
def receber_dados():
    data = request.get_json()
    frame = data.get('frame')
    objetos = data.get('objetos')
    tempo = data.get('tempo_ms')
    timestamp = datetime.now().isoformat()

    print(f"[{timestamp}] Frame {frame}: {objetos} ({tempo}ms)")
    return jsonify({"status": "recebido", "frame": frame}), 200

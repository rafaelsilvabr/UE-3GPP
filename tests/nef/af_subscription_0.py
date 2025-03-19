from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para receber notificações da NEF
@app.route('/notifications', methods=['POST'])
def handle_notification():
    notification_data = request.json  # Dados da notificação
    print("Recebida notificação da NEF:")
    print(notification_data)
    return jsonify({"status": "Notificação recebida"}), 200

if __name__ == '__main__':
    # Inicia o servidor na porta 8080
    app.run(host='0.0.0.0', port=8081)
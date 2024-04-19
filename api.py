from flask import Flask, request, jsonify
import base64
from datetime import datetime, timedelta

app = Flask(__name__)

# Dados de exemplo para autenticação (usuários)
users = {
    'example@example.com': {'password': 'password123'}
}

# Endpoint para autenticação
@app.route('/auth', methods=['POST'])
def authenticate():
    data = request.json
    if 'email' in data and 'password' in data:
        email = data['email']
        password = data['password']
        if email in users and users[email]['password'] == password:
            # Criando token com validade de 7 dias
            expiration_date = datetime.utcnow() + timedelta(days=7)
            token = base64.b64encode(f"{email}:{expiration_date}".encode()).decode()
            return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid email or password"}), 401

# Endpoint para upload de foto
@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    # Verifica se o token está presente nos cabeçalhos
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Token is missing"}), 401

    # Verifica se o token é válido (implementação de validação do token necessário aqui)

    # Recebe o user_id e a foto
    user_id = request.form.get('user_id')
    photo_file = request.files.get('photo')
    if not user_id or not photo_file:
        return jsonify({"error": "Missing user_id or photo"}), 400

    # Converte a foto para base64 e obtém o tamanho em bytes
    photo_data = photo_file.read()
    photo_base64 = base64.b64encode(photo_data).decode()
    photo_size_bytes = len(photo_data)

    return jsonify({"photo_base64": photo_base64, "photo_size_bytes": photo_size_bytes}), 200

# Endpoint para consulta de contagem de fotos
@app.route('/photo_count', methods=['GET'])
def photo_count():
    # Verifica se o token está presente nos cabeçalhos
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Token is missing"}), 401

    # Verifica se o token é válido (implementação de validação do token necessário aqui)

    # Simula a contagem de fotos (substitua por sua lógica real)
    photo_count = 100  # Exemplo: contagem fictícia de fotos

    return jsonify({"photo_count": photo_count}), 200

if __name__ == '__main__':
    app.run(debug=True)
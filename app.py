from flask import Flask, request, jsonify

app = Flask(__name__)

# Estrutura de dados simulando um banco (em memória)
usuarios = []
current_id = 1  # ID inicial

# Rota para criar um novo usuário
@app.route('/users', methods=['POST'])
def criar_usuario():
    global current_id
    dados = request.json

    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({'erro': 'Dados inválidos. É necessário nome e email.'}), 400

    novo_usuario = {
        'id': current_id,
        'nome': dados['nome'],
        'email': dados['email']
    }
    usuarios.append(novo_usuario)
    current_id += 1

    return jsonify(novo_usuario), 201


# Rota para listar todos os usuários
@app.route('/users', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200


# Rota para obter um usuário pelo ID
@app.route('/users/<int:user_id>', methods=['GET'])
def obter_usuario(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404


# Rota para atualizar um usuário
@app.route('/users/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    dados = request.json
    for usuario in usuarios:
        if usuario['id'] == user_id:
            if 'nome' in dados:
                usuario['nome'] = dados['nome']
            if 'email' in dados:
                usuario['email'] = dados['email']
            return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404


# Rota para deletar um usuário
@app.route('/users/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuarios.remove(usuario)
            return jsonify({'mensagem': 'Usuário excluído com sucesso'}), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404


if __name__ == '__main__':
    app.run(debug=True)
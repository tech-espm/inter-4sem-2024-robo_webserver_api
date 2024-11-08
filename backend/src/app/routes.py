from flask import Blueprint, request, jsonify
from .db import get_db_connection
import datetime 


main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"message": "User created"}), 201

@main.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    
    return jsonify(users), 200

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    
    if user is None:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user), 200

@main.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    name = data.get('name')
    password = data.get('password')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = %s, password = %s WHERE id = %s", (name, password, user_id))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"message": "User updated"}), 200

@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"message": "User deleted"}), 200

@main.route('/grava_ip', methods=['POST'])
def grava_ip():
    data = request.json
    ip = data.get('ip')
 
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO arduino (ip) VALUES (%s)", (ip))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"message": "ip saved"}), 200

@main.route('/grava_leituras', methods=['POST'])
def grava_leituras():
    data = request.json
    umidade = data.get('umidade')
    data_atual = datetime.now()
    data_hora_medição = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    quadrante = data.get('quadrante')
 
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO leituras (umidade_solo, data_e_hora, quadrante) VALUES (%s)", (umidade, data_hora_medição, quadrante ))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"message": "data saved"}), 200
    
# @main.route('/create_tables', methods=['POST'])
# def create_tables():
#     try:
#         conn = get_db_connection()
#         cur = conn.cursor()
        
#         # Comando SQL para criar a tabela de usuários
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS users (
#                 id SERIAL PRIMARY KEY,
#                 name VARCHAR(100) NOT NULL,
#                 password VARCHAR(100) NOT NULL
#             );
#         """)
        
#         conn.commit()
#         cur.close()
#         conn.close()
        
#         return jsonify({"message": "Tabela de usuários criada com sucesso."}), 201
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
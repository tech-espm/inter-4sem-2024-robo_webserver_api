from flask import Blueprint, request, jsonify
from .db import get_db_connection

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

@main.route('/create_tables', methods=['POST'])
def create_tables():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Comando SQL para criar a tabela de usuários
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL
            );
        """)
        
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({"message": "Tabela de usuários criada com sucesso."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
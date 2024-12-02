from flask import Blueprint, request, jsonify
from app.db import get_db_connection
import datetime 
from psycopg2.extras import RealDictCursor 

main = Blueprint('main', __name__)

# Função auxiliar para executar consultas e obter resultados
def fetch_query_results(query):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)
    columns = [desc[0] for desc in cur.description]
    results = [dict(zip(columns, row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return results


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
    
@main.route('/clima', methods=['GET'])
def get_clima():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)  
    cur.execute('SELECT * FROM clima;')
    rows = cur.fetchall()  
    cur.close()
    conn.close()

    return jsonify(rows)  

@main.route('/solo/semanal', methods=['GET'])
def get_solo_semanal():
    conn = get_db_connection()
    query = """
        SELECT
            DATE_TRUNC('week', date) AS period,
            AVG(COALESCE(nitrogenio,0)) AS avg_nitrogenio,
            AVG(COALESCE(fosforo,0)) AS avg_fosforo,
            AVG(COALESCE(potassio,0)) AS avg_potassio
        FROM solo
        WHERE date >= CURRENT_DATE - INTERVAL '7 days'
        GROUP BY DATE_TRUNC('week', date)
        ORDER BY period DESC;
    """
    results = fetch_query_results(query)
    conn.close()
    return jsonify(results)

@main.route('/solo/mensal', methods=['GET'])
def get_solo_mensal():
    conn = get_db_connection()
    query = """
        SELECT
            DATE_TRUNC('month', date) AS period,
            AVG(COALESCE(nitrogenio,0)) AS avg_nitrogenio,
            AVG(COALESCE(fosforo,0)) AS avg_fosforo,
            AVG(COALESCE(potassio,0)) AS avg_potassio
        FROM solo
        WHERE date >= CURRENT_DATE - INTERVAL '1 month'
        GROUP BY DATE_TRUNC('month', date)
        ORDER BY period DESC;
    """
    results = fetch_query_results(query)
    conn.close()
    return jsonify(results)

@main.route('/solo/trimestral', methods=['GET'])
def get_solo_trimestral():
    conn = get_db_connection()
    query = """
        SELECT
            DATE_TRUNC('quarter', date) AS period,
            AVG(COALESCE(nitrogenio,0)) AS avg_nitrogenio,
            AVG(COALESCE(fosforo,0)) AS avg_fosforo,
            AVG(COALESCE(potassio,0)) AS avg_potassio
        FROM solo
        WHERE date >= CURRENT_DATE - INTERVAL '3 months'
        GROUP BY DATE_TRUNC('quarter', date)
        ORDER BY period DESC;
    """
    results = fetch_query_results(query)
    conn.close()
    return jsonify(results)

@main.route('/solo/media/1', methods=['GET'])
def get_solo_diario():
    conn = get_db_connection()
    query = """
        SELECT
            DATE(date) AS period,
            AVG(COALESCE(nitrogenio,0)) AS avg_nitrogenio,
            AVG(COALESCE(fosforo,0)) AS avg_fosforo,
            AVG(COALESCE(potassio,0)) AS avg_potassio
        FROM solo
        WHERE date = CURRENT_DATE 
        GROUP BY DATE(date)  
        ORDER BY period DESC;
    """
    results = fetch_query_results(query)
    conn.close()
    return jsonify(results)


@main.route('/solo/media/15', methods=['GET'])
def get_solo_media_ultimos_15_dias():
    conn = get_db_connection()
    query = """
        SELECT
            AVG(COALESCE(nitrogenio, 0)) AS avg_nitrogenio,
            AVG(COALESCE(fosforo, 0)) AS avg_fosforo,
            AVG(COALESCE(potassio, 0)) AS avg_potassio
        FROM solo
        WHERE date >= CURRENT_DATE - INTERVAL '15 days';  -- Filtra para os últimos 15 dias
    """
    results = fetch_query_results(query)
    conn.close()
    return jsonify(results)



@main.route('/solo/media/45', methods=['GET'])
def get_solo_media_ultimos_45_dias():
    conn = get_db_connection()
    query = """
        SELECT
            AVG(COALESCE(nitrogenio, 0)) AS avg_nitrogenio,
            AVG(COALESCE(fosforo, 0)) AS avg_fosforo,
            AVG(COALESCE(potassio, 0)) AS avg_potassio
        FROM solo
        WHERE date >= CURRENT_DATE - INTERVAL '45 days';
    """
    results = fetch_query_results(query)
    conn.close()
    return jsonify(results)

@main.route('/solo/media/30', methods=['GET'])
def get_solo_media_ultimos_30_dias():
    conn = get_db_connection()
    query = """
        SELECT
            AVG(COALESCE(nitrogenio, 0)) AS avg_nitrogenio,
            AVG(COALESCE(fosforo, 0)) AS avg_fosforo,
            AVG(COALESCE(potassio, 0)) AS avg_potassio
        FROM solo
        WHERE date >= CURRENT_DATE - INTERVAL '30 days';
    """
    results = fetch_query_results(query)
    conn.close()
    return jsonify(results)


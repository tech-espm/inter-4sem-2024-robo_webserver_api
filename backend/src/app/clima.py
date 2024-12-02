import pandas as pd
import psycopg2
from backend.src.config import Config

# Caminho para o arquivo CSV
file_path = 'C:/Users/andrezza.freire/Downloads/clima.csv'

# Lê o CSV para um DataFrame
df = pd.read_csv(file_path)

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        port=Config.DB_PORT
)

# Criação do cursor
cur = conn.cursor()

# Defina o nome da tabela no PostgreSQL
table_name = 'clima'

# Insere os dados na tabela
for i, row in df.iterrows():
    # Ajuste os nomes das colunas conforme necessário
    insert_query = f"""
    INSERT INTO {table_name} (time, temperature_2m_mean, rain_sum, wind_speed_10m_max)
    VALUES (%s, %s, %s, %s);
    """
    
    # Insira os dados na tabela
    cur.execute(insert_query, (row['time'], row['temperature'], row['rain_sun'], row['wind_speed_10m_max']))

# Commit para salvar as alterações no banco de dados
conn.commit()

# Fechar o cursor e a conexão
cur.close()
conn.close()

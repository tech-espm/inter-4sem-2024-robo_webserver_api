import psycopg2 
from config import Config
# docker run --name postgres2 -p 800:5432 -e POSTGRES_PASSWORD=root -d postgresdocker run --name postgres2 -p 800:5432 -e POSTGRES_PASSWORD=root -d postgres

conn = psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        port=Config.DB_PORT
)


tabela_users="""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
)
"""

tabela_leituras="""
CREATE TABLE IF NOT EXISTS leituras (
	umidade_solo FLOAT NOT NULL,
	data_e_hora timestamp NOT NULL,
	quadrante INT NOT NULL
)
"""

tabela_arduino="""
CREATE TABLE IF NOT EXISTS arduino (
	ip VARCHAR(20) NOT NULL
)
"""

cursor = conn.cursor()
cursor.execute(tabela_users)
cursor.execute(tabela_leituras)
cursor.execute(tabela_arduino)

print('deu certo')

cursor.execute("""
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_type = 'BASE TABLE'
      AND table_schema NOT IN ('pg_catalog', 'information_schema');
    """
    )

tables = cursor.fetchall()
for table in tables:
    print(f"Schema: {table[0]}, Table: {table[1]}")
        
conn.commit()
conn.close()

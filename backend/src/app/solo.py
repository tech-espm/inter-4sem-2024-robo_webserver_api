import pandas as pd
import psycopg2
from config import Config

file_path = 'C:/Users/andrezza.freire/Downloads/dados_solo_atual.csv'  

df = pd.read_csv(file_path)

conn = psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        port=Config.DB_PORT
)

cur = conn.cursor()

table_name = 'solo'

for i, row in df.iterrows():
    
    insert_query = f"""
    INSERT INTO {table_name} (date, nitrogenio, fosforo, potassio)
    VALUES (%s, %s, %s, %s);
    """
    
    cur.execute(insert_query, (row['Data'], row['Nitrogenio'], row['fosforo'], row['potassio']))

conn.commit()

cur.close()
conn.close()

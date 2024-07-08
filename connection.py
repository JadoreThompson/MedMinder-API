import os

import psycopg2
from dotenv import load_dotenv

load_dotenv('.env')

conn_params = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'dbname': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT')
}

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        print("Conn:", conn)
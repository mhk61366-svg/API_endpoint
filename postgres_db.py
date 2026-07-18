from psycopg import connect
from psycopg.rows import dict_row

HOST = "localhost"
PORT = 5432
DB_NAME = "backend_ai_internship"
USER = "postgres"
PASSWORD = "hamadDB"
TABLE_NAME = "users"


def get_connection():
    return connect(
        host=HOST,
        port=PORT,
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        row_factory=dict_row,
    )


def get_table_name():
    return TABLE_NAME

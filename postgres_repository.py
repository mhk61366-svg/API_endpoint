from repository import User_Repository
from postgres_db import get_connection, get_table_name


class PostgresUserRepository(User_Repository):
    def __init__(self):
        self.conn = get_connection()
        self.table_name = get_table_name()

    def get_all_users(self):
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {self.table_name}")
            user_details = cur.fetchall()
            return user_details
    
    def get_user_by_id(self, user_id: int):
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {self.table_name} WHERE id = %s", (user_id,))
            user_details = cur.fetchone()
            return user_details
    
    def create_user(self, user_data: dict):
        with self.conn.cursor() as cur:
            cur.execute(
                f"INSERT INTO {self.table_name} (name, age, email) VALUES (%s, %s, %s) RETURNING id, name, age, email",
                (user_data["name"], user_data["age"], user_data["email"]),
            )
            self.conn.commit()
            return cur.fetchone()

    def update_user(self, user_id: int, user_data: dict):
        if not user_data:
            return None

        set_clauses = []
        values = []
        for column in ("name", "age", "email"):
            if column in user_data:
                set_clauses.append(f"{column} = %s")
                values.append(user_data[column])

        if not set_clauses:
            return None

        values.append(user_id)
        sql = f"UPDATE {self.table_name} SET {', '.join(set_clauses)} WHERE id = %s RETURNING id, name, age, email"

        with self.conn.cursor() as cur:
            cur.execute(sql, tuple(values))
            self.conn.commit()
            return cur.fetchone()
        
    def delete_user(self, user_id: int):
        with self.conn.cursor() as cur:
            cur.execute(f"DELETE FROM {self.table_name} WHERE id = %s RETURNING *", (user_id,))
            self.conn.commit()
            deleted_user = cur.fetchone()
            return {"message": f"User deleted successfully"} if deleted_user else None
        
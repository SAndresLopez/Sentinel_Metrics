#encargado de poblar la base de datos.
# Como no tenemos una empresa real con miles de clientes usando una app
# este script "siembra" información ficticia.

import mysql.connector
from faker import Faker
import random


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="sentinel_metrics_db"
)
cursor = db.cursor()
fake = Faker()


def seed_project():
    print("Generando usuarios...")
    plans = ['Basic', 'Professional', 'Enterprise']
    user_ids = []

    for _ in range(100):
        query = "INSERT INTO users (full_name, email, plan_type) VALUES (%s, %s, %s)"
        values = (fake.name(), fake.email(), random.choice(plans))
        cursor.execute(query, values)
        user_ids.append(cursor.lastrowid)

    print("Generando logs de actividad...")
    actions = ['login', 'view_dashboard', 'export_csv', 'open_ticket', 'change_settings']

    for _ in range(5000):
        u_id = random.choice(user_ids)
        query = "INSERT INTO activity_logs (user_id, action_type, session_id) VALUES (%s, %s, %s)"
        values = (u_id, random.choice(actions), fake.uuid4())
        cursor.execute(query, values)

    db.commit()
    print(f"¡Éxito! Insertados {len(user_ids)} usuarios y 5000 logs.")


if __name__ == "__main__":
    seed_project()
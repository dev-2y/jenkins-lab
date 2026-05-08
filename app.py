import os
import psycopg
from flask import Flask

app = Flask(__name__)

def get_conn():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "app_db"),
        user=os.getenv("DB_USER", "app_user"),
        password=os.getenv("DB_PASSWORD", "app_password"),
    )

@app.get("/")
def home():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            value = cur.fetchone()[0]
    return {"status": "ok", "db": value}

if __name__ == "__main__":
    print("Iniciando aplicação Flask na porta 5000...", flush=True)
    app.run(host="0.0.0.0", port=5000)


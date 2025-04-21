import psycopg2
from database import get_connection

def get_connection():
    return psycopg2.connect(
        dbname="phone_book_db",
        user="postgres",
        password="2007",
        host="localhost",
        port="5432"
    )

def insert_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO phone_book (first_name, last_name, phone)
    VALUES
    ('Тогжан', 'Ivanova', '8123456789'),
    ('Аружан', 'Petrova', '8734567890'),
    ('Камила', 'Sidorova', '8998765432')
    """)

    conn.commit()
    cur.close()
    conn.close()

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS phone_book (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        phone VARCHAR(20) UNIQUE
    );
    ''')

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    init_db()
    insert_data()

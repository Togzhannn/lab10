import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="phone_book_db",
        user="postgres",
        password="2007",  
        host="localhost",
        port="5432"
    )

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

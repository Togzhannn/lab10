import psycopg2


conn = psycopg2.connect(
    dbname="phone_book_db",
    user="postgres",
    password="2007",  
    host="localhost",
    port="5432"
)

cur = conn.cursor()


cur.execute("""
    INSERT INTO phone_book (first_name, last_name, phone) 
    VALUES
    ('Тогжан', 'Ivanova', '8123456789'),
    ('Аружан', 'Petrova', '8734567890'),
    ('Камила', 'Sidorova', '8998765432')
""")


conn.commit()

cur.execute("SELECT * FROM phone_book")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()


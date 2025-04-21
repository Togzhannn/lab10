import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",  
        user="postgres",          
        password="2007"   
    )

# Insert 
def insert_data(first_name, phone):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (first_name, phone))
        conn.commit()
        print(f"Inserted: {first_name}, {phone}")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# 1.
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    insert_data(name, phone)

# 2.
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                insert_data(row[0], row[1])

# 3. 
def update_data(identifier, new_value, field):
    conn = connect()
    cur = conn.cursor()
    if field == "first_name":
        cur.execute("UPDATE PhoneBook SET first_name = %s WHERE phone = %s", (new_value, identifier))
    elif field == "phone":
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE first_name = %s", (new_value, identifier))
    conn.commit()
    print("Updated.")
    cur.close()
    conn.close()

# 4. 
def query_data(filter_by=None, value=None):
    conn = connect()
    cur = conn.cursor()
    if filter_by and value:
        cur.execute(f"SELECT * FROM PhoneBook WHERE {filter_by} = %s", (value,))
    else:
        cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# 5.
def delete_data(identifier, by_field="first_name"):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM PhoneBook WHERE {by_field} = %s", (identifier,))
    conn.commit()
    print("Deleted.")
    cur.close()
    conn.close()

if __name__ == '__main__':
     insert_from_csv('a.csv')

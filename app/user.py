from app.database import get_connection

def add_user(name, email):
    db = get_connection()
    cursor = db.cursor()

    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))

    db.commit()
    cursor.close()
    db.close()

def view_users():
    db = get_connection()
    cursor = db.cursor()

    query = "SELECT * FROM users"
    cursor.execute(query)

    for user in cursor.fetchall():
        print(user)

    cursor.close()
    db.close()

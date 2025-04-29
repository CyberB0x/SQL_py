import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="kali",
        database="user_db"
    )
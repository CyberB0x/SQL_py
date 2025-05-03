import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="",
        password="",
        database="user_db"
    )

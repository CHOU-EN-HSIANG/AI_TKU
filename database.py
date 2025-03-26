import mysql.connector
from mysql.connector import Error

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,      # host port號
            user="root",      # 請替換成你的 MySQL 帳號
            password="laman",  # 請替換成你的 MySQL 密碼
            database="laman_db"   # 請替換成你要連接的資料庫名稱
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("MySQL 連接失敗:", e)
        return None

# подключаем SQLite
import sqlite3 as sl

# открываем файл с базой данных
con = sl.connect('thecode.db')

# создаём таблицу для товаров
with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS goods (
            product VARCHAR(20) PRIMARY KEY,
            count INTEGER,
            price INTEGER

);
    """)


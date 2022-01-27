import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "messages_tg_bot.sqlite")


conn = sqlite3.connect(db_path)

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Messages')
cur.execute('CREATE TABLE Messages (id INTEGER PRIMARY KEY AUTOINCREMENT, messageText TEXT, appendingTime TEXT)')

cur.close()
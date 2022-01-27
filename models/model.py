import sqlite3
import os.path
import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "messages_tg_bot.sqlite")

conn = sqlite3.connect(db_path, check_same_thread=False)


def retrieve_messages() -> list:
	cur = conn.cursor()

	messages = []
	db_messages = cur.execute('''SELECT messageText FROM Messages''')
	
	for message in db_messages:
		messages.append(message[0])

	return messages
	cur.close()


def is_unique(message_text):
	return message_text not in retrieve_messages()


def save_data_if_unique(message_text) -> None:
	datetime_now = str(datetime.datetime.now())

	if is_unique(message_text):
		cur = conn.cursor()
		cur.execute('INSERT INTO Messages (messageText, appendingTime) VALUES (?, ?)',\
		(message_text, datetime_now))
		conn.commit()
		cur.close()
		return "success"
	else:
		return "duplicate"


def retrieve_data() -> None:
	cur = conn.cursor()
	cur.execute('''SELECT * FROM Messages''')
	for row in cur:
		print(row)
	cur.close()
# retrieve_data()


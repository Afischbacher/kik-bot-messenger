import sqlite3
from flask import g

global conn, cursor, answer


def route_response_logic(recieved_message):
    PATH = 'ReverseIndex.db'
    db = getattr(g, '__database', None)

    if db is None:
        conn = g.__database = sqlite3.connect(PATH)
        cursor = conn.cursor()
    msg_array = recieved_message.split()

    for msg in msg_array:
        sql = "SELECT `Answers` FROM Answers, Keywords WHERE Answers.ID = Keywords.ID AND" \
              " `Keywords` LIKE LOWER('%?%') ORDER BY RANDOM() LIMIT 1;"
        cursor.execute(sql, msg)
        if cursor.fetchone():
            answer = cursor.fetchone()
        break
    return answer

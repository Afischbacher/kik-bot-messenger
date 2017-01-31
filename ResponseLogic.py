import sqlite3
from flask import g




def sql_conn():
    PATH = 'ReverseIndex.db'
    db = getattr(g, '__database', None)

    if db is None:
        global conn, cursor
        conn = g.__database = sqlite3.connect(PATH)
        cursor = conn.cursor()
        sql = "SELECT `Answers` FROM Answers, Keywords WHERE Answers.ID = Keywords.ID AND `Keywords` LIKE LOWER('%' || ? || '%') ORDER BY RANDOM() LIMIT 1;"



def route_response_logic(recieved_message):
    msg_array = recieved_message.split()
    for msg in msg_array:
        sql = "SELECT `Answers` FROM Answers, Keywords WHERE Answers.ID = Keywords.ID AND `Keywords` LIKE LOWER('%' || ? || '%') ORDER BY RANDOM() LIMIT 1;"
        cursor.execute(sql,msg_array.index(msg))

    return cursor.fetchone()
import sqlite3
from flask import g

global conn, cursor, answer


def route_response_logic(recieved_message):
    db = getattr(g, '__database', None)

    if db is None:
        conn = g.__database = sqlite3.connect('ReverseIndex')
        cursor = conn.cursor()

    msg_list = recieved_message.split()

    for msg in msg_list:
        cursor.execute(
            "SELECT Answers FROM Answers, Keywords WHERE Answers.ID = Keywords.ID AND Keywords LIKE LOWER(?) ORDER BY RANDOM() LIMIT 1;",
            (msg,))
        row = cursor.fetchone()
        if row is not None:
            res = row[0]
            return res
        else:
            return "Sorry I am not sure about that question or response, I am going to have to get smarter for that one..."

import sqlite3
from flask import g

global conn, cursor, answer
user_inputs = []


def route_response_logic(recieved_message):
    db = getattr(g, '__database', None)

    if db is None:
        conn = g.__database = sqlite3.connect('ReverseIndex')
        cursor = conn.cursor()

    user_inputs.append(recieved_message)

    if recieved_message in user_inputs:
        return "Hey you already asked me that question, try another one"

    msg_list = recieved_message.split()

    for msg in msg_list:
        cursor.execute(
            "SELECT Answers FROM Answers, Keywords WHERE Answers.ID = Keywords.ID AND Keywords LIKE '% ' || LOWER(?) || ' %' ORDER BY RANDOM() LIMIT 1;",
            (msg,))
        row = cursor.fetchone()
        if row is not None:
            res = row[0]
            return res


    cursor.execute(
    "SELECT ConnectingResponse FROM `Unknown Answers` ORDER BY RANDOM() LIMIT 1;"
    )

    connecting_resp = cursor.fetchone()
    return connecting_resp[0]
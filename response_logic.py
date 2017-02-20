import sqlite3
from flask import g
from location_finder import get_location
import sqlite3

global conn, cursor, answer


def route_response_logic(recieved_message):
    db = getattr(g, '__database', None)

    if db is None:
        conn = g.__database = sqlite3.connect('ResponseDatabase')
        cursor = conn.cursor()

    msg_list = recieved_message.split()

    if "location" in recieved_message or "Location" in recieved_message:
        return get_location()

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

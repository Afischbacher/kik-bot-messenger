import sqlite3
from flask import g

rand_query = "SELECT `Answers` FROM Answers, Keywords WHERE Answers.Keyword_ID = Keywords.ID AND `Keywords` LIKE LOWER('%' || ? || '%') ORDER BY RANDOM() LIMIT 1;"


def sql_conn():
    PATH = 'ReverseIndex.db'
    db = getattr(g, '__database', None)

    if db is None:
        db = g.__database = sqlite3.connect(PATH)
    return db


def route_response_logic(recieved_message):
    return ""   
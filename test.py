import sqlite3


def logic():
    conn = sqlite3.connect('ReverseIndex')
    cursor = conn.cursor()
    msg_list = "asdfasd".split()

    for msg in msg_list:
        cursor.execute(
            "SELECT Answers FROM Answers, Keywords WHERE Answers.ID = Keywords.ID AND Keywords LIKE LOWER('%' || ? || '%') ORDER BY RANDOM() LIMIT 1;",
            (msg,))
        row = cursor.fetchone()
        if row is not None:
            return row[0]
        else:
            return "Sorry I can not answer that question right, now I am still getting smarter"


print(logic())

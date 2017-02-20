import sqlite3
from location_finder import get_location


def logic():
    conn = sqlite3.connect('ResponseDatabase')
    cursor = conn.cursor()

    resp = "Hey"
    msg_list = resp.split()

    if "location" in resp or "Location" in resp:
        print(get_location())
        return

    for msg in msg_list:
        cursor.execute(
            "SELECT Answers FROM Answers, Keywords WHERE Answers.ID = Keywords.ID AND Keywords LIKE '% ' || LOWER(?) || ' %' ORDER BY RANDOM() LIMIT 1;",
            (msg,))
        row = cursor.fetchone()
        if row is not None:
            return row[0]

    cursor.execute(
        "SELECT ConnectingResponse FROM `Unknown Answers` ORDER BY RANDOM() LIMIT 1;"
    )

    connecting_resp = cursor.fetchone()
    return connecting_resp[0]



print(logic())

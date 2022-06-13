import sqlite3
def GetTelephoneBook(db):
    con  = sqlite3.Connection(db)
    cur = con.cursor()
    cur.execute("""select pFname, pLname, tbNumber, ttName from peoples
    join TelephoneBook on (peoples.pID = TelephoneBook.pID)
    join TelTypes on (TelTypes.ttID = TelephoneBook.ttID)
    """)
    result = cur.fetchall()
    con.close()
    return result
import sqlite3
import Logging
def AddUser(db, fName, lName):
    con = sqlite3.Connection(db)
    cur = con.cursor()
    cur.execute(f"""Insert into Peoples(pFname, pLname) values ("{fName}", "{lName}");""")
    con.commit()
    cur.execute(f"""select max(pID) FROM Peoples""")
    pid = cur.fetchall()
    Logging.WriteEvent('add contact', f'Add {fName} {lName}')
    return pid[0][0]
def AddPhone(db, pID, tbNumber, ttID):
    con = sqlite3.Connection(db)
    cur = con.cursor()
    commandStr = f"""insert into TelephoneBook(pID, tbNumber, ttID) values({pID}, "{tbNumber}", {ttID});"""
    cur.execute(commandStr)
    con.commit()
    selectStr = f"""SELECT pFname, pLname FROM Peoples where pID = {pID}"""
    cur.execute(selectStr)
    people = cur.fetchall()
    Logging.WriteEvent('add telephone', f'Add {people[0][0]} {people[0][1]} - {tbNumber}')
def AddPhones(db, pID, tNumbers):
    for i in tNumbers:
        AddPhone(db, pID, i[0], i[1])
def AddCard(db, fName, lName, tNumbers):
    pID = AddUser(db,fName,lName)
    AddPhones(db, pID, tNumbers)
import sqlite3
import AddPhone
import Logging
def GetTTID(db,tName):
    con = sqlite3.Connection(db)
    cur = con.cursor()
    cur.execute(f'select ttID from TelTypes where ttName = "{tName}"')
    tID = cur.fetchall()
    if len(tID) == 0: return -1
    con.close()
    return tID[0][0]
def ImportData(db):
    con = sqlite3.Connection(db)
    file = open('import.csv', 'r', encoding='utf-8')
    lines = file.readlines()
    for i in lines:
        i = i.replace(f'\n','')
        line = i.split(';')
        pid = AddPhone.AddUser(db, line[0],line[1])
        for t in range(3, len(line), 2):
            ttID = GetTTID(db, line[t])
            if ttID != -1:
                AddPhone.AddPhone(db, pid, line[t-1], ttID)
    Logging.WriteEvent('Add import', 'import')
    con.close()
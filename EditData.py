import sqlite3
import Logging
def EditUser(db, pID, fName, lName):
    con = sqlite3.Connection(db)
    cur = con.cursor()
    cur.execute(f"""Update Peoples 
                set pFname = '{fName}',
                    pLName = '{lName}'
                where pID = {pID}""")
    con.commit()
    Logging.WriteEvent(f'Изменен пользователь с id = {pID}', 'edit user')
    print(f'Пользователь с id = {pID} изменен.')
import sqlite3
import Logging
def PrintPeoples(users):
    for i in users:
        print(f'{i}: {users[i]}')
def GetPeoples(db):
    con = sqlite3.Connection(db)
    cur = con.cursor()
    cur.execute("""select  pID, pFname || ' ' || pLname from peoples""")
    result = cur.fetchall()
    con.close()
    users = {i[0]: i[1] for i in result}
    PrintPeoples(users)
    return users
def DeleteUser(db, id):
    con = sqlite3.Connection(db)
    cur = con.cursor()
    cur.execute(f'delete from TelephoneBook where pID = {id}')
    Logging.WriteEvent(f'Удалены телефоны пользователя с id = {id}', 'delete phones')
    cur.execute(f'delete from Peoples where pID = {id}')
    Logging.WriteEvent(f'Удален пользователь с id = {id}', 'delete user')
    print(f'Пользователь с id = {id} удален.')
    print()
    con.commit()
    con.close()


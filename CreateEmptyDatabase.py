import sqlite3
import Logging
def CreateEmptyDB():
    con  = sqlite3.Connection('Empty.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Peoples(pID INTEGER PRIMARY KEY AUTOINCREMENT, pFname TEXT, pLname TEXT);
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS TelTypes(ttID INTEGER PRIMARY KEY AUTOINCREMENT, ttName);
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS TelephoneBook(pID INTEGER, tbNumber, ttID,
    FOREIGN KEY (pID) REFERENCES Peoples(pID),
    FOREIGN KEY (ttID) REFERENCES TelTypes(ttID)
    );
    """)
    cur.execute("""Insert into TelTypes(ttName) values ("Сотовый");""")
    cur.execute("""Insert into TelTypes(ttName) values ("Городской");""")
    cur.execute("""Insert into TelTypes(ttName) values ("Рабочий");""")
    cur.execute("""Insert into TelTypes(ttName) values ("Другой");""")
    con.commit()
    Logging.WriteEvent('Create Empty DB', 'CreateDB')
    con.close()
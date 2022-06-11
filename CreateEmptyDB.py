import sqlite3

con  = sqlite3.Connection('telephoneBook.db')
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
cur.execute("""Insert into Peoples(pFname, pLname) values ("Иван", "Иванов");""")
cur.execute("""Insert into Peoples(pFname, pLname) values ("Петр", "Петров");""")
cur.execute("""Insert into Peoples(pFname, pLname) values ("Сидор", "Сидоров");""")
cur.execute("""Insert into Peoples(pFname, pLname) values ("Андрей", "Андреев");""")
cur.execute("""Insert into Peoples(pFname, pLname) values ("Алексей", "Алексеев");""")
cur.execute("""Insert into Peoples(pFname, pLname) values ("Сергей", "Сергеев");""")
cur.execute("""Insert into TelTypes(ttName) values ("Сотовый");""")
cur.execute("""Insert into TelTypes(ttName) values ("Городской");""")
cur.execute("""Insert into TelTypes(ttName) values ("Рабочий");""")
cur.execute("""Insert into TelTypes(ttName) values ("Другой");""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (1, "111", 1);""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (1, "112", 2);""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (2, "211", 1);""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (2, "212", 2);""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (2, "213", 3);""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (3, "311", 4);""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (4, "412", 3);""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (5, "511", 1);""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (5, "512", 2);""")
cur.execute("""Insert into TelephoneBook(pID, tbNumber, ttID) values (6, "616", 1);""")
con.commit()
con.close()
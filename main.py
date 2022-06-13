import sqlite3
import ExportData
import Logging
import AddPhone
import UI
# con  = sqlite3.Connection('telephoneBook.db')
# cur = con.cursor()
# cur.execute("""select pFname, pLname, tbNumber, ttName from peoples
# join TelephoneBook on (peoples.pID = TelephoneBook.pID)
# join TelTypes on (TelTypes.ttID = TelephoneBook.ttID)
# """)
# result3 = cur.fetchall()
# con.close()
# ExportData.ExportDataFile(result3, 'file', 'qwe')
# AddPhone.AddCard('telephoneBook.db', 'Иван', 'Иванов', '7123', '3')
# AddPhone.AddCard('telephoneBook.db', 'Иван', 'Иванов', '7123', '3')
# AddPhone.AddCard('telephoneBook.db', 'Иван', 'Иванов', '7123', '3')
# AddPhone.AddCard('telephoneBook.db', 'Петр', 'Петров', '7123', '3')
# AddPhone.AddCard('telephoneBook.db', 'Петр', 'Петров', '7123', '3')
# AddPhone.AddCard('telephoneBook.db', 'Сидор', 'Сидоров', '7123', '3')
# AddPhone.AddCard('telephoneBook.db', 'Данила', 'Данилов', '7123', '3')
# AddPhone.AddCard('telephoneBook.db', 'Данила', 'Данилов', '7123', '3')
# AddPhone.AddCard('telephoneBook.db', 'Данила', 'Данилов', '7123', '3')
# AddPhone.AddCard('telephoneBook.db', 'Данила', 'Данилов', '7123', '3')
# t1 = []
# t1.append(['9999', 1])
# t1.append(['9998', 2])
# t1.append(['9997', 3])
# t1.append(['9996', 4])
# AddPhone.AddCard('telephoneBook.db', 'Сигезмунд', 'Сигезмундов', t1)

#UI.AddData('telephoneBook.db')
#UI.ViewTelephoneBook('telephoneBook.db')
UI.start('telephoneBook.db')
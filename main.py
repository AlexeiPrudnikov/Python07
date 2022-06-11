import sqlite3
import ExportData
import Logging
con  = sqlite3.Connection('telephoneBook.db')
cur = con.cursor()
cur.execute("""select pFname, pLname, tbNumber, ttName from peoples
join TelephoneBook on (peoples.pID = TelephoneBook.pID)
join TelTypes on (TelTypes.ttID = TelephoneBook.ttID)
""")
result3 = cur.fetchall()
con.close()
ExportData.ExportDataFile(result3, 'file', 'qwe')

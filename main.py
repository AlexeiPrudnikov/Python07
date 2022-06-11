import sqlite3
import Export
con  = sqlite3.Connection('telephoneBook.db')
cur = con.cursor()
cur.execute("""select pFname, pLname, tbNumber, ttName from peoples 
join TelephoneBook on (peoples.pID = TelephoneBook.pID)
join TelTypes on (TelTypes.ttID = TelephoneBook.ttID)
""")
result3 = cur.fetchall()
con.close()
Export.ExportFile(result3,'phones.txt')
Export.ExportCSV(result3,'phones.csv')
Export.ExportHtml(result3,'phones.html')
# for i in result3:
#     print(i)

import sqlite3
import AddPhone
import Logging
import Menu
import ExportData
import ViewBook
import DeletePhone
import ImportData
import CreateEmptyDatabase
import EditData
def IsValidType(id, telTypes):
    for i in telTypes:
        if i[0] == id: return True
    return False
def AddData(db):
    lName = input('Введите фамилию: ')
    fName = input('Введите имя: ')
    con = sqlite3.Connection(db)
    cur = con.cursor()
    cur.execute('select ttID, ttName from TelTypes')
    telTypes = cur.fetchall()
    result = 'y'
    telephones = []
    while (result == 'y'):
        print ('Типы телефонных номеров')
        for i in telTypes:
            print(f'{i[0]}: {i[1]}')
        valid = False
        while not valid:
            tt = int(input('Введите номер типа телефона:'))
            valid = IsValidType(tt, telTypes)
            if not valid:
                print('Ошибка, введенный номер некоректен.')
        tel = input('Введите номер телефона: ')
        telephones.append([tel, tt])
        result = input(f'Хотите добавить еще один телефон пользователю {fName} {lName} ("y" для продолжения)?')
    con.close()
    AddPhone.AddCard(db, fName, lName, telephones)
def ViewTelephoneBook(db):
    result = ViewBook.GetTelephoneBook(db)
    for i in result:
        print(f'{i[1]} {i[0]}: {i[2]} - {i[3]}')
    Logging.WriteEvent('print','db select')
def start(db):
    actions = Menu.InitMainMenu()
    index = -1
    while index != max(actions.keys()):
        Menu.PrintMenu(actions)
        index = Menu.ChooseMenu(actions)
        if index == 1:
            ViewTelephoneBook(db)
            print()
        elif index == 2:
            AddData(db)
        elif index == 3:
            DeletePhone.GetPeoples(db)
            delIndex = int(input('Введите номер пользователя, которого надо удалить: '))
            DeletePhone.DeleteUser(db, delIndex)
        elif index == 4:
            export = Menu.InitExportMenu()
            Menu.PrintMenu(export)
            expIndex = Menu.ChooseMenu(export)
            if expIndex == 1:
                ft = 'csv'
            elif expIndex == 2:
                ft = 'file'
            else:
                ft = 'html'
            ExportData.ExportDataFile(ViewBook.GetTelephoneBook(db), ft, 'export')
        elif index == 5:
            ImportData.ImportData(db)
        elif index == 6:
            CreateEmptyDatabase.CreateEmptyDB()
        elif index == 7:
            DeletePhone.GetPeoples(db)
            editIndex = int(input('Введите номер пользователя, которого надо изменить: '))
            lName = input('Введите новую фамилию: ')
            fName = input('Введите новое имя: ')
            EditData.EditUser(db, editIndex, fName, lName)


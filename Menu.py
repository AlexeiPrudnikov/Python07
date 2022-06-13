def PrintMenu(actions):
    for i in actions:
        print(f'{i}: {actions[i]}')
def InitMainMenu():
    actions = {}
    actions[1] = 'Просмотр книни'
    actions[2] = 'Добавить пользователя'
    actions[3] = 'Удалить пользователя'
    actions[4] = 'Экспорт телефонной книги'
    actions[5] = 'Выход'
    return actions
def ChooseMenu(actions):
    index = int(input('Выберите действие:'))
    while not index in actions.keys():
        index = int(input('Ошибка выбора. Выберите действие:'))
    return index
def InitExportMenu():
    export = {}
    export[1] = 'CSV'
    export[2] = 'File'
    export[3] = 'HTML'
    return export
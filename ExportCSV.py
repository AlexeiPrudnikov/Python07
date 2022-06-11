import Logging
def ExportCSVFile(data, fileName):
    file = open(f'{fileName}.csv', 'w', encoding="utf-16")
    for i in data:
        file.write(f"{';'.join(map(str, i))}\n")
    Logging.WriteEvent('Экспорт в csv-файл', 'Export')
    file.close()
import Logging
def ExportFileFile(data, fileName):
    file = open(f'{fileName}.file', 'w',encoding="utf-8")
    for i in data:
        for z in i:
            file.write(f"{z}\n")
    file.close()
    Logging.WriteEvent('Экспорт в file', 'Export')
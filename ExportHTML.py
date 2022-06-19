import Logging
def ExportHtmlFile(data, fileName):
    file = open(f'{fileName}.html', 'w', encoding="utf-8")
    htmlStr = f"""
    <!doctype html>
        <html lang="ru">
        <head>
          <meta charset="utf-8" />
          <title>{fileName}</title>
        </head>
        <body>
        <table border="1px">\n
        <caption>Телефонная книга</caption>
        <tr><th>Имя</th><th>Фамилия</th><th>Телефон</th><th>Тип телефона</th></tr>\n"""
    file.write(htmlStr)
    for i in data:
        file.write(f"<tr><td>{i[0]}</td><td>{i[1]}</td><td>{i[2]}</td><td>{i[3]}</td></tr>\n")
    htmlStr = """</table>
        </body>
        </html>
    """
    file.write(htmlStr)
    file.close()
    Logging.WriteEvent('Экспорт в html-файл', 'Export')
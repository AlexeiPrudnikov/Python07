def ExportFile(data, fileName):
    file = open(fileName, 'w',encoding="utf-8")
    for i in data:
        for z in i:
            file.write(f"{z}\n")
    file.close()
def ExportCSV(data, fileName):
    #file = open(fileName, 'w', encoding="utf-8")
    file = open(fileName, 'w', encoding="utf-16")
    for i in data:
        file.write(f"{';'.join(map(str, i))}\n")
    file.close()
def ExportHtml(data, fileName):
    file = open(fileName, 'w', encoding="utf-8")
    htmlStr = f"""
    <!doctype html>
        <html lang="ru">
        <head>
          <meta charset="utf-8" />
          <title>{fileName}</title>
        </head>
        <body>
        <table border="1px">\n"""
    file.write(htmlStr)
    for i in data:
        file.write(f"<tr><td>{i[0]}</td><td>{i[1]}</td><td>{i[2]}</td><td>{i[3]}</td></tr>\n")
    htmlStr = """</table>
        </body>
        </html>
    """
    file.write(htmlStr)
    file.close()

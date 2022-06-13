import datetime
def WriteEvent(data, dbEvent):
    logFile = open('logs.csv', 'a', encoding="utf-8")
    writeStr = f"""{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")};{dbEvent};{data}\n"""
    logFile.write(writeStr)
    logFile.close()
    return
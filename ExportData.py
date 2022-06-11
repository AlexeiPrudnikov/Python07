import ExportCSV
import ExportFile
import ExportHTML
def ExportDataFile(data, fileType, fileName):
    if fileType == 'html':
            ExportHTML.ExportHtmlFile(data, fileName)
    elif fileType == 'file':
            ExportFile.ExportFileFile(data, fileName)
    elif fileType == 'csv':
            ExportCSV.ExportCSVFile(data, fileName)
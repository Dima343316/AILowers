import datetime
import glob
from docx import Document
from python_docx_replace import docx_replace


class PasteValues:
    doc = Document("sweater/docs/sample/docx_sample.docx")

    def __init__(self, data):
        self.data = data

    def change_values(self):
        current_datetime = datetime.datetime.now().strftime(
            "%Y%m%d-%H%M%S")  # получение текущей даты и времени в формате "ГГГГММДД-ЧЧММСС"
        filename = f"sweater/docs/result/result_{current_datetime}.docx"  # формирование имени файла с датой и временем
        docx_replace(self.doc, **self.data)
        self.doc.save(filename)


def last_file(path):
    result = []
    for py in glob.glob(path):
        result.append(py)
    return sorted(result)[-1]


def file_count(path):
    result = []
    for py in glob.glob(path):
        result.append(py)
    return len(result)

import openpyxl
import itertools
import pandas



def LoadWorkBook(xlsx_path):
  return openpyxl.load_workbook(xlsx_path, read_only=True)
  
def GetWorkSheetIndexFromWorkBook(index, work_book):
  return work_book[work_book.sheetnames[index]]
  
def GetWorkSheetValues(work_sheet):
  return work_sheet.values
  
def CreatePandasDataFrameFromValues(values):
  column_names = next(values)
  
  rows = list(values)
  data = (itertools.islice(row, 0, None) for row in rows)
  
  data_frame = pandas.DataFrame(data, columns=column_names)
  return data_frame
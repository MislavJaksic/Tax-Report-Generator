import os

from tax_report_generator.pathfinding import pathfinder
from tax_report_generator.data_wrangling import excel_data
from tax_report_generator.settings import data_settings



def LoadDataFrame(file_name):
  name, extension = pathfinder.SplitFileNameIntoNameAndExtension(file_name)
  
  if extension == "xlsx":
    data_frame = LoadXLSXIntoDataFrame(file_name)
  else:
    raise Exception("Unknown extension!")
  
  return data_frame

  
  
def LoadXLSXIntoDataFrame(xlsx_name):
  xlsx_path_components = [GetDirectoryPath(),
                          data_settings.data_file_relative_path,
                          xlsx_name]
  xlsx_path = pathfinder.CreateAbsolutePath(xlsx_path_components)
  
  work_book = excel_data.LoadWorkBook(xlsx_path)
  work_sheet = excel_data.GetWorkSheetIndexFromWorkBook(0, work_book)
  
  values = excel_data.GetWorkSheetValues(work_sheet)
  
  data_frame = excel_data.CreatePandasDataFrameFromValues(values)
  return data_frame
  
  
  
def GetDirectoryPath():
  return os.path.dirname(__file__)
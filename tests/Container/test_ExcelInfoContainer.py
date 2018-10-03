from TaxReportGenerator.Containers.ExcelInfoContainer import ExcelInfoContainer

import pytest



def test_GetInfoAt():
  table_info = ExcelInfoContainer()
  table_info.AddExcelLetterColumnHeaderDataTypeTuple(("C", "Useful_Two", "float"))
  table_info.AddExcelLetterColumnHeaderDataTypeTuple(("B", "Useful_One", "float"))
  
  assert table_info.GetInfoAt(0) == ["B", "C"]
  
def test_GetDictByKeyValuePosition():
  table_info = ExcelInfoContainer()
  table_info.AddExcelLetterColumnHeaderDataTypeTuple(("C", "Useful_Two", "float"))
  table_info.AddExcelLetterColumnHeaderDataTypeTuple(("B", "Useful_One", "float"))
  
  assert table_info.GetDictByKeyValuePosition(1,2) == {"Useful_One" : "float", "Useful_Two" : "float"}

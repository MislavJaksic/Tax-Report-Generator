import datetime
from TaxReportGenerator.DataManipulation import Loading
from TaxReportGenerator.Containers.ExcelInfoContainer import ExcelInfoContainer
from TaxReportGenerator.Settings import DataSettings
from TaxReportGenerator.Settings import TestSettings
from TaxReportGenerator.BusinessRules import InvoiceRules

import pytest



def test_LoadExcel():
  table_info = ExcelInfoContainer()
  for column_info in TestSettings.sample_data_info:
    table_info.AddExcelLetterColumnHeaderDataTypeTuple(column_info)
  
  settings = Loading.GetExcelSettings(TestSettings.sample_data_file_path,
                                      table_info,
                                      TestSettings.sample_data_footer_rows)
  data = Loading.LoadExcel(settings)
  print(data.head())
  assert data.at[2,"strings"] == "world"
  
def test_LoadTestInvoices():
  table_info = ExcelInfoContainer()
  for column_data in TestSettings.invoices_info:
    table_info.AddExcelLetterColumnHeaderDataTypeTuple(column_data)
  
  settings = Loading.GetExcelSettings(TestSettings.invoices_file_path,
                                      table_info,
                                      TestSettings.sample_data_footer_rows)
  
  data = Loading.LoadExcel(settings)
  
  data = InvoiceRules.ApplyRules(data)
  
  assert data.at[2,DataSettings.due_date_invoices] == datetime.datetime(2018, 6, 22)

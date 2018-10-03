import datetime
import numpy as np
import pandas
from TaxReportGenerator.DataManipulation import Loading
from TaxReportGenerator.Containers.ExcelInfoContainer import ExcelInfoContainer
from TaxReportGenerator.Settings import TestSettings
from TaxReportGenerator.Settings import DataSettings
from TaxReportGenerator.BusinessRules import GeneralRules

import pytest



def test_ChangeValueToNaNInDataFrame():
  table_info = ExcelInfoContainer()
  for column_info in TestSettings.invoices_info:
    table_info.AddExcelLetterColumnHeaderDataTypeTuple(column_info)
  
  settings = Loading.GetExcelSettings(TestSettings.invoices_file_path,
                                      table_info,
                                      TestSettings.invoices_footer_rows)
  
  data = Loading.LoadExcel(settings)

  assert pandas.isnull(data.at[3,DataSettings.invoice_number_invoices]) == False
  
  data = GeneralRules.ChangeValueToNaNInDataFrame(TestSettings.invoices_empty_cell_value, data)

  assert pandas.isnull(data.at[3,DataSettings.invoice_number_invoices]) == True

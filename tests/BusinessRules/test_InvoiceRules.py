from TaxReportGenerator.Containers.ExcelInfoContainer import ExcelInfoContainer
from TaxReportGenerator.DataManipulation import Loading
from TaxReportGenerator.Settings import TestSettings
from TaxReportGenerator.Settings import DataSettings
from TaxReportGenerator.BusinessRules import GeneralRules
from TaxReportGenerator.BusinessRules import InvoiceRules

import pytest



def test_ApplyRules():
  table_info = ExcelInfoContainer()
  for column_info in TestSettings.invoices_info:
    table_info.AddExcelLetterColumnHeaderDataTypeTuple(column_info)
  
  settings = Loading.GetExcelSettings(TestSettings.invoices_file_path,
                                      table_info,
                                      TestSettings.invoices_footer_rows)
  data = Loading.LoadExcel(settings)
  
  data = GeneralRules.ChangeValueToNaNInDataFrame(TestSettings.invoices_empty_cell_value, data)
  data = InvoiceRules.ApplyRules(data)
  
  with pytest.raises(KeyError):
    assert data.at[0,DataSettings.customer_name_invoices]
  with pytest.raises(KeyError):
    assert data.at[1,DataSettings.customer_name_invoices]
  with pytest.raises(KeyError):
    assert data.at[3,DataSettings.customer_name_invoices]
   
  assert data.at[2,DataSettings.customer_name_invoices]

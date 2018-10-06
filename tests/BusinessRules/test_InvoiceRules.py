import pandas
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
  
  
  
@pytest.fixture(scope='function')
def TestExcel():
  table_info = ExcelInfoContainer()
  for column_info in TestSettings.invoices_info:
    table_info.AddExcelLetterColumnHeaderDataTypeTuple(column_info)
  
  settings = Loading.GetExcelSettings(TestSettings.invoices_file_path,
                                      table_info,
                                      TestSettings.invoices_footer_rows)
  data = Loading.LoadExcel(settings)
  data = GeneralRules.ChangeValueToNaNInDataFrame(TestSettings.invoices_empty_cell_value, data)
  
  return data
  
def test_DiscardRowsWithoutIdentifier(TestExcel):
  TestExcel = InvoiceRules.DiscardRowsWithoutIdentifier(TestExcel)
  
  assert pandas.isnull(TestExcel.at[0,DataSettings.invoice_number_invoices]) == False
  assert pandas.isnull(TestExcel.at[1,DataSettings.invoice_number_invoices]) == False
  assert pandas.isnull(TestExcel.at[2,DataSettings.invoice_number_invoices]) == False
  with pytest.raises(KeyError):
    assert TestExcel.at[3,DataSettings.invoice_number_invoices]
  
def test_DiscardRowsWithIncorrectCurrency(TestExcel):
  TestExcel = InvoiceRules.DiscardRowsWithIncorrectCurrency(TestExcel)
  
  assert TestExcel.at[0,DataSettings.customer_name_invoices]
  with pytest.raises(KeyError):
    assert TestExcel.at[1,DataSettings.customer_name_invoices]
  assert TestExcel.at[2,DataSettings.customer_name_invoices]
  assert TestExcel.at[3,DataSettings.customer_name_invoices]
  
def test_DeleteExtraColumns(TestExcel):
  InvoiceRules.DeleteExtraColumns(TestExcel)
  
  with pytest.raises(KeyError):
    assert TestExcel.at[0,DataSettings.posting_currency_invoices]
  
def test_DiscardRowsWithNegativeAmount(TestExcel):
  TestExcel = InvoiceRules.DiscardRowsWithNegativeAmount(TestExcel)
  
  assert TestExcel.at[0,DataSettings.invoice_amount_invoices]
  with pytest.raises(KeyError):
    assert TestExcel.at[1,DataSettings.invoice_amount_invoices]
  assert TestExcel.at[2,DataSettings.invoice_amount_invoices]
  assert TestExcel.at[3,DataSettings.invoice_amount_invoices]
  
def test_DiscardRowsAfterReportingDate(TestExcel):
  TestExcel = InvoiceRules.DiscardRowsAfterReportingDate(TestExcel)
  
  with pytest.raises(KeyError):
    assert TestExcel.at[0,DataSettings.customer_name_invoices]
  assert TestExcel.at[1,DataSettings.customer_name_invoices]
  assert TestExcel.at[2,DataSettings.customer_name_invoices]
  assert TestExcel.at[3,DataSettings.customer_name_invoices]

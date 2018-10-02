# -*- encoding: utf-8 -*-

import datetime
from TaxReportGenerator.DataManipulation import Loading
from TaxReportGenerator.Containers.TableInfoContainer import TableInfoContainer
from TaxReportGenerator.Settings import DataSettings
from TaxReportGenerator.Settings import TestSettings
from TaxReportGenerator.BusinessRules import InvoiceRules

import pytest



def test_LoadExcel():
  table_info = TableInfoContainer()
  table_info.AddColumnTuple(("B", "numbers", "U"))
  table_info.AddColumnTuple(("C", "dates", "U"))
  
  skip_last_few_rows = 1
  
  settings = Loading.GetExcelSettings(TestSettings.data_file_path,
                                      table_info,
                                      skip_last_few_rows)
  data = Loading.LoadExcel(settings)
  
  assert data.at[2,"numbers"] == "11.0"
  
def test_LoadTestInvoices():
  table_info = TableInfoContainer()
  table_info.AddColumnTuple(("F", DataSettings.posting_date_invoices, "M"))
  table_info.AddColumnTuple(("G", DataSettings.posting_currency_invoices, "U"))
  table_info.AddColumnTuple(("D", DataSettings.open_amount_invoices, "f"))
  table_info.AddColumnTuple(("B", DataSettings.invoice_number_invoices, "U"))
  table_info.AddColumnTuple(("E", DataSettings.due_date_invoices, "M"))
  table_info.AddColumnTuple(("C", DataSettings.invoice_amount_invoices, "f"))
  table_info.AddColumnTuple(("A", DataSettings.customer_name_invoices, "U"))
  
  skip_last_few_rows = 1
  
  settings = Loading.GetExcelSettings(TestSettings.invoices_file_path,
                                      table_info,
                                      skip_last_few_rows)
  
  data = Loading.LoadExcel(settings)
  
  data = InvoiceRules.ApplyRules(data)
  
  assert data.at[2,DataSettings.due_date_invoices] == datetime.datetime(2018, 6, 22)

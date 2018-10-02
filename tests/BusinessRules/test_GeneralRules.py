# -*- encoding: utf-8 -*-

import datetime
import numpy as np
import pandas
from TaxReportGenerator.DataManipulation import Loading
from TaxReportGenerator.Containers.TableInfoContainer import TableInfoContainer
from TaxReportGenerator.Settings import TestSettings
from TaxReportGenerator.Settings import DataSettings
from TaxReportGenerator.BusinessRules import GeneralRules

import pytest



def test_ChangeValueToNoneInDataFrame():
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

  assert pandas.isnull(data.at[3,DataSettings.invoice_number_invoices]) == False
  
  value = "nan"
  data = GeneralRules.ChangeValueToNoneInDataFrame(value, data)

  assert pandas.isnull(data.at[3,DataSettings.invoice_number_invoices]) == True

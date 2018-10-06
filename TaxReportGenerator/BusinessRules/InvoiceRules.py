# -*- encoding: utf-8 -*-

import os
import sys
import inspect
folder_list = os.path.abspath(inspect.getfile(inspect.currentframe())).split("\\")
folder = folder_list.pop()
while (folder_list[-1] != "TaxReportGenerator"):
  folder_list.pop()
sys.path.append(os.path.dirname("\\".join(folder_list)))

import numpy as np
from TaxReportGenerator.Settings import LegalSettings
from TaxReportGenerator.Settings import DataSettings



def ApplyRules(invoices):
  invoices = DiscardRowsWithoutIdentifier(invoices)
  
  invoices = DiscardRowsWithIncorrectCurrency(invoices)
  DeleteExtraColumns(invoices)
  
  invoices = DiscardRowsWithNegativeAmount(invoices)
  
  invoices = DiscardRowsAfterReportingDate(invoices)
  return invoices
  
def DiscardRowsWithoutIdentifier(invoices):
  #Delete rows without an invoice number
  return invoices[invoices[DataSettings.invoice_number_invoices].notnull()]
  
def DiscardRowsWithIncorrectCurrency(invoices):
  #Delete rows with non HRK currency
  return invoices[invoices[DataSettings.posting_currency_invoices] == LegalSettings.national_currency]
  
def DeleteExtraColumns(invoices):
  del invoices[DataSettings.posting_currency_invoices]
  
def DiscardRowsWithNegativeAmount(invoices):
  #Delete rows that have a negative invoice amount
  return invoices[invoices[DataSettings.invoice_amount_invoices] > 0]
  
def DiscardRowsAfterReportingDate(invoices):
  #Delete rows that are due after the report date
  return invoices[invoices[DataSettings.due_date_invoices] <= LegalSettings.DatumDo]

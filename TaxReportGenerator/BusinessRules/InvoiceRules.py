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
  #Delete rows without an invoice number
  invoices = invoices[invoices[DataSettings.invoice_number_invoices].notnull()]
  #Delete rows with non HRK currency
  invoices = invoices[invoices[DataSettings.posting_currency_invoices] == LegalSettings.national_currency]
  del invoices[DataSettings.posting_currency_invoices]
  #Delete rows that have a negative invoice amount
  invoices = invoices[invoices[DataSettings.invoice_amount_invoices] > 0]
  #Delete rows that are due after the report date
  invoices = invoices[invoices[DataSettings.due_date_invoices] <= LegalSettings.DatumDo]
  return invoices

from TaxReportGenerator.Containers.ReportDataContainer import ReportDataContainer
from TaxReportGenerator.Settings import DataSettings
from TaxReportGenerator.Settings import LegalSettings

import pytest



def test_ReportDataContainer():
  data = ReportDataContainer(set([DataSettings.customers,
                              DataSettings.vendors,
                              DataSettings.invoices,
                              DataSettings.IRA_EU,
                              DataSettings.URA_EU_DC,
                              DataSettings.URA_EU_DOM,
                              DataSettings.URA_EU_UVOZ]))
  
  assert data.customers.at[0,DataSettings.tax_number_customers] + "string"
  assert data.vendors.at[0,DataSettings.tax_number_vendors] + "string"
  assert data.invoices.at[0,DataSettings.invoice_amount_invoices] + 1.0
  assert data.IRA_EU.at[0,DataSettings.exports_IRA_EU] + 1.0
  assert data.URA_EU_DC.at[0,DataSettings.tax_base_URA_EU_DC] + 1.0
  assert data.URA_EU_DOM.at[0,DataSettings.refundable_URA_EU_DOM] + 1.0
  assert data.URA_EU_UVOZ.at[0,DataSettings.total_URA_EU_UVOZ] + 1.0

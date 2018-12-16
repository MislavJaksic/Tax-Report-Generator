from tax_report_generator.data_wrangling import pandas_functions
from tax_report_generator.settings import data_settings
from tax_report_generator.settings import report_settings



def FilterInvoices(data_frame):
  data_frame = DiscardPandasNullRows(data_frame)
  data_frame = DiscardNonNationalCurrencyCurrency(data_frame)
  data_frame = DiscardNegativeAmount(data_frame)
  data_frame = DiscardFutureDates(data_frame)
  
  return data_frame

def DiscardPandasNullRows(data_frame):
  customers_column = data_settings.invoices_customer_name
  filtered_data_frame = data_frame[data_frame[customers_column].notnull()]
  return filtered_data_frame
  
def DiscardNonNationalCurrencyCurrency(data_frame):
  posting_currency_column = data_settings.invoices_posting_currency
  filtered_data_frame = data_frame[data_frame[posting_currency_column] == data_settings.national_currency]
  return filtered_data_frame
  
def DiscardNegativeAmount(data_frame):
  amount_column = data_settings.invoices_amount
  filtered_data_frame = data_frame[data_frame[amount_column] > 0]
  return filtered_data_frame
  
def DiscardFutureDates(data_frame):
  due_date_column = data_settings.invoices_due_date
  filtered_data_frame = data_frame[data_frame[due_date_column] <= report_settings.DatumDo]
  return filtered_data_frame
  
  
  
def FilterCustomers(data_frame):
  data_frame = DiscardColumnsBeyondColumn(data_frame)
  
  return data_frame

def DiscardColumnsBeyondColumn(data_frame):
  useless_columns_after = data_settings.customers_useless_columns_after
  
  counter = 1
  for column in data_frame.columns:
    if counter > useless_columns_after:
      del data_frame[column]
    counter += 1
  
  return data_frame
  

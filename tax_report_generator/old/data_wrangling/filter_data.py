from tax_report_generator.data_wrangling import pandas_functions
from tax_report_generator.settings import data_settings
from tax_report_generator.settings import report_settings



def FilterInvoices(data_frame):
  data_frame = DiscardPandasNullRows(data_frame)
  data_frame = DiscardNonNationalCurrencyCurrency(data_frame)
  data_frame = DiscardNegativeAmount(data_frame)
  data_frame = DiscardFutureDates(data_frame)
  
  return data_frame
  
def FilterCustomers(data_frame):
  #last_usefull_column_index = data_settings.customers_useless_columns_after
  #data_frame = DiscardColumnsBeyondColumn(data_frame, last_usefull_column_index)
  data_frame = DiscardPandasNullRows(data_frame)
  
  return data_frame
  
def FilterVendors(data_frame):
  #last_usefull_column_index = data_settings.vendors_useless_columns_after
  #data_frame = DiscardColumnsBeyondColumn(data_frame, last_usefull_column_index)
  data_frame = DiscardPandasNullRows(data_frame)
  
  return data_frame
  
def FilterIRA_EU(data_frame):
  data_frame = DiscardPandasNullRows(data_frame)
  #data_frame = DiscardZeroInBothColumns(data_frame, data_settings.IRA_EU_goods_sold, data_settings.IRA_EU_services_sold)
  
  return data_frame
  
def FilterNullRows(data_frame):
  data_frame = DiscardPandasNullRows(data_frame)
  
  return data_frame


  
def DiscardPandasNullRows(data_frame):
  first_column = data_frame.columns[0]
  filtered_data_frame = data_frame[data_frame[first_column].notnull()]
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
  
def DiscardZeroInBothColumns(frame, column_one, column_two):
  return frame[(frame[column_one] != 0.0) | (frame[column_two] != 0.0)]

def DiscardColumnsBeyondColumn(data_frame, last_usefull_column_index):
  return data_frame #strange behaviour!
  
  
  

  

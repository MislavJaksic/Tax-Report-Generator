from tax_report_generator.data_wrangling import load_data
from tax_report_generator.pathfinding import pathfinder
from tax_report_generator.data_wrangling import filter_data
from tax_report_generator.settings import data_settings



class DataFrameWrapper(object):
  def __init__(self, file_names):
    self.data_frames = {}
    self.__LoadFiles(file_names)
    self.__FilterData()
    self.__SortData()
    
  def __LoadFiles(self, file_names):
    for file_name in file_names:
      name, extension = pathfinder.SplitFileNameIntoNameAndExtension(file_name)
      
      self.data_frames[name] = load_data.LoadDataFrame(file_name)
      
  def __FilterData(self):
    invoices_file = data_settings.invoices_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(invoices_file)
    
    if name in self.data_frames.keys():
      self.data_frames[name] = filter_data.FilterInvoices(self.data_frames[name])
      
    customers_file = data_settings.customers_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(customers_file)
    
    if name in self.data_frames.keys():
      self.data_frames[name] = filter_data.FilterCustomers(self.data_frames[name])
      
  def __SortData(self):
    invoices_file = data_settings.invoices_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(invoices_file)
    
    if name in self.data_frames.keys():
      self.data_frames[name].sort_values(by=[data_settings.invoices_customer_name])
      
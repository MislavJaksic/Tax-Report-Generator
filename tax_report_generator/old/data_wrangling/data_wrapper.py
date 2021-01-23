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
    customers_file = data_settings.customers_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(customers_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = filter_data.FilterCustomers(self.data_frames[name])
    
    invoices_file = data_settings.invoices_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(invoices_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = filter_data.FilterInvoices(self.data_frames[name])
    
    IRA_EU_file = data_settings.IRA_EU_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(IRA_EU_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = filter_data.FilterIRA_EU(self.data_frames[name])
    
    URA_EU_DC_file = data_settings.URA_EU_DC_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(URA_EU_DC_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = filter_data.FilterNullRows(self.data_frames[name])
      
    URA_EU_DOM_file = data_settings.URA_EU_DOM_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(URA_EU_DOM_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = filter_data.FilterNullRows(self.data_frames[name])
      
    URA_EU_UVOZ_file = data_settings.URA_EU_UVOZ_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(URA_EU_UVOZ_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = filter_data.FilterNullRows(self.data_frames[name])
      
    vendors_file = data_settings.vendors_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(vendors_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = filter_data.FilterVendors(self.data_frames[name])
      
  def __SortData(self):
    invoices_file = data_settings.invoices_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(invoices_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = self.data_frames[name].sort_values(by=[data_settings.invoices_customer_name])
      
    URA_EU_DC_file = data_settings.URA_EU_DC_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(URA_EU_DC_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = self.data_frames[name].sort_values(by=[data_settings.URA_EU_DC_vendor_id])
      
    IRA_EU_file = data_settings.IRA_EU_file
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(IRA_EU_file)
    if name in self.data_frames.keys():
      self.data_frames[name] = self.data_frames[name].sort_values(by=[data_settings.IRA_EU_customer_id])
      
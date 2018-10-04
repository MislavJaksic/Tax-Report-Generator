from TaxReportGenerator.DataManipulation import Loading
from TaxReportGenerator.Containers.ExcelInfoContainer import ExcelInfoContainer
from TaxReportGenerator.BusinessRules import InvoiceRules
from TaxReportGenerator.Settings import DataSettings
from TaxReportGenerator.Settings import LegalSettings



class TablesContainer(object):

  def __init__(self, required_data):
    self.tables = []
    self.LoadRequiredData(required_data)
    
  def LoadRequiredData(self, required_data):
    if DataSettings.customers in required_data:
      self.customers = self.LoadColumnsFromFileSkippingFooter(DataSettings.customers_columns,
                                                              DataSettings.customers_file_path,
                                                              DataSettings.customers_skip_footer)
      self.tables.append(self.customers)
    if DataSettings.invoices in required_data:
      self.invoices = self.LoadColumnsFromFileSkippingFooter(DataSettings.invoices_columns,
                                                             DataSettings.invoices_file_path,
                                                             DataSettings.invoices_skip_footer)
      self.invoices = InvoiceRules.ApplyRules(self.invoices)
      self.tables.append(self.invoices)
    if DataSettings.IRA_EU in required_data:
      self.IRA_EU = self.LoadColumnsFromFileSkippingFooter(DataSettings.IRA_EU_columns,
                                                           DataSettings.IRA_EU_file_path,
                                                           DataSettings.IRA_EU_skip_footer)
      self.tables.append(self.IRA_EU)
    if DataSettings.URA_EU_DC in required_data:
      self.URA_EU_DC = self.LoadColumnsFromFileSkippingFooter(DataSettings.URA_EU_DC_columns,
                                                              DataSettings.URA_EU_DC_file_path,
                                                              DataSettings.URA_EU_DC_skip_footer)
      self.tables.append(self.URA_EU_DC)
    if DataSettings.URA_EU_DOM in required_data:
      self.URA_EU_DOM = self.LoadColumnsFromFileSkippingFooter(DataSettings.URA_EU_DOM_columns,
                                                               DataSettings.URA_EU_DOM_file_path,
                                                               DataSettings.URA_EU_DOM_skip_footer)
      self.tables.append(self.URA_EU_DOM)
    if DataSettings.URA_EU_UVOZ in required_data:
      self.URA_EU_UVOZ = self.LoadColumnsFromFileSkippingFooter(DataSettings.URA_EU_UVOZ_columns,
                                                                DataSettings.URA_EU_UVOZ_file_path,
                                                                DataSettings.URA_EU_UVOZ_skip_footer)
      self.tables.append(self.URA_EU_UVOZ)
    if DataSettings.vendors in required_data:
      self.vendors = self.LoadColumnsFromFileSkippingFooter(DataSettings.vendors_columns,
                                                            DataSettings.vendors_file_path,
                                                            DataSettings.vendors_skip_footer)
      self.tables.append(self.vendors)
      
  def LoadColumnsFromFileSkippingFooter(self, columns, file_path, skip_footer):
    table_info = ExcelInfoContainer(columns)
    settings = Loading.GetExcelSettings(file_path,
                                        table_info,
                                        skip_footer)
    return Loading.LoadExcel(settings)
    
  def head(self):
    for data in self.tables:
      print(DataSettings.head())
      print()
      print()
  
  def tail(self):
    for data in self.tables:
      print(DataSettings.tail())
      print()
      print()
    
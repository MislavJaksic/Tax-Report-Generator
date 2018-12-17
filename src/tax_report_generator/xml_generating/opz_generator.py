import copy
from datetime import datetime

from tax_report_generator.pathfinding import pathfinder
from tax_report_generator.data_wrangling import transform_data
from tax_report_generator.data_wrangling import pandas_functions
from tax_report_generator.xml_generating import xml_generator
from tax_report_generator.xml_generating import lxml_functions
from tax_report_generator.settings import xml_settings
from tax_report_generator.settings import report_settings
from tax_report_generator.settings import data_settings



class OPZGenerator(xml_generator.XMLGenerator):
  def __init__(self, data_wrapper):
    self.__SetDataFrames(data_wrapper)
    
    report_name = xml_settings.opz_template
    self.SetAndLoadRootElements(report_name)
    
    self.ConstructReport()
    
    lxml_functions.WriteTreeToFile(self.wrapper_tree, xml_settings.opz_output_file)
    
  def __SetDataFrames(self, data_wrapper):
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.invoices_file)
    self.invoices = copy.deepcopy(data_wrapper.data_frames[name])
    
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.customers_file)
    self.customers = copy.deepcopy(data_wrapper.data_frames[name])
    
  
  
  def CreateAndFillOutBody(self):
    body_element = self.__ExtractBodyElement()
    children = lxml_functions.GetSubElements(body_element)
    
    customers_element = self.__FillOutCustomers()
    lxml_functions.InsertChildElementIntoElementAtIndex(customers_element, body_element, 0)
    
    for child_element in children:
      data = False
      child_tag = lxml_functions.GetTag(child_element)
    
      if child_tag == "UkupanIznosRacunaObrasca":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("K5", customers_element)
        
      elif child_tag == "UkupanIznosPdvObrasca":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("K6", customers_element)
        
      elif child_tag == "UkupanIznosRacunaSPdvObrasca":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("K7", customers_element)
        
      elif child_tag == "UkupniPlaceniIznosRacunaObrasca":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("K8", customers_element)
        
      elif child_tag == "NeplaceniIznosRacunaObrasca":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("K9", customers_element)
        
      elif child_tag == "OPZUkupanIznosRacunaSPdv":
        data = 0.0
        
      elif child_tag == "OPZUkupanIznosPdv":
        data = 0.0
        
      if (data != False):
        lxml_functions.SetElementText(child_element, data)
        
    return body_element
   

    
  def __FillOutCustomers(self):
    customers_element = lxml_functions.CreateElement("Kupci")
    
    customer_counter = 1
    while (pandas_functions.IsFrameNotEmpty(self.invoices)):
      customer_name = pandas_functions.GetFirstValueFromColumnFromFrame(data_settings.invoices_customer_name, self.invoices)
      
      invoice_batch, self.invoices = pandas_functions.SplitFrameAlongColumnWithValue(self.invoices, data_settings.invoices_customer_name, customer_name)
      
      customer_element = self.__FillOutCustomerNumber(invoice_batch, customer_counter)
      lxml_functions.AddChildElementToElement(customer_element, customers_element)
      
      customer_counter += 1
      
    return customers_element
     
  def __FillOutCustomerNumber(self, invoice_batch, number):
    customer_element = self.__ExtractCustomerElement()
    children = lxml_functions.GetSubElements(customer_element)
    
    invoices_element = self.__FillOutInvoices(invoice_batch)
    lxml_functions.AddChildElementToElement(invoices_element, customer_element)
    
    customer_name = pandas_functions.GetFirstValueFromColumnFromFrame(data_settings.invoices_customer_name, invoice_batch)
    
    for child_element in children:
      data = False
      child_tag = lxml_functions.GetTag(child_element)
    
      if child_tag == "K1":
        data = number
        
      elif child_tag == "K2":
        data = 1
        
      elif child_tag == "K3":
        number = pandas_functions.GetValueFromColumnFromFrameIfColumnHasValue(data_settings.customers_tax_number, self.customers, data_settings.customers_name, customer_name)
        data = transform_data.AddLeadingZerosToStringUntilLength(number, 11)
        
      elif child_tag == "K4":
        data = customer_name
        
      elif child_tag == "K5":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("R6", invoices_element)
        
      elif child_tag == "K6":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("R7", invoices_element)
        
      elif child_tag == "K7":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("R8", invoices_element)
        
      elif child_tag == "K8":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("R9", invoices_element)
        
      elif child_tag == "K9":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("R10", invoices_element)
      
      if (data != False):
        lxml_functions.SetElementText(child_element, data)
    
    return customer_element
  
  def __FillOutInvoices(self, invoice_batch):
    invoices_element = lxml_functions.CreateElement("Racuni")
    
    invoice_counter = 1
    for index, invoice in invoice_batch.iterrows():
      invoice_element = self.__FillOutInvoiceNumber(invoice, invoice_counter)
      
      lxml_functions.AddChildElementToElement(invoice_element, invoices_element)
      
      invoice_counter += 1
      
    return invoices_element
       
  def __FillOutInvoiceNumber(self, invoice, number):
      invoice_element = self.__ExtractInvoiceElement()
      all_children = lxml_functions.GetAllSubElements(invoice_element)
      
      for child_element in all_children:
        data = False
        child_tag = lxml_functions.GetTag(child_element)
      
        if child_tag == "R1":
          data = number
          
        elif child_tag == "R2":
          data = invoice[u'Invoice Nr']
          
        elif child_tag == "R3":
          data = invoice[u'Posting date']
          
        elif child_tag == "R4": 
          data = invoice[u'Due Date']
          
        elif child_tag == "R5":
          data = self.__GetPaymentDelay(invoice[u'Due Date'])
          
        elif child_tag == "R6":
          data = invoice[data_settings.invoices_amount] / (1.0 + report_settings.tax_rate)
          
        elif child_tag == "R7":
          data = invoice[data_settings.invoices_amount] - invoice[data_settings.invoices_amount] / (1.0 + report_settings.tax_rate)
          
        elif child_tag == "R8":
          data = invoice[data_settings.invoices_amount]
          
        elif child_tag == "R9":
          data = invoice[data_settings.invoices_amount] - invoice[data_settings.invoices_open_amount]
          
        elif child_tag == "R10":
          data = invoice[data_settings.invoices_open_amount]
          
        if (data != False):
          lxml_functions.SetElementText(child_element, data)
          
      return invoice_element
      
      
      
  def __GetPaymentDelay(self, payment_date):
    report_date = datetime.strptime(report_settings.NisuNaplaceniDo, "%Y-%m-%d")
    return report_date - payment_date
    
    
  
  def __ExtractBodyElement(self):
    body_element = copy.deepcopy(self.body_root)
    body_element.remove(body_element[0])
        
    return body_element
   
  def __ExtractCustomerElement(self):
    body_children = lxml_functions.GetAllSubElements(self.body_root)
    for element in body_children:
      if element.tag == "Kupac":
        customer_element = copy.deepcopy(element)
        customer_element.remove(customer_element[-1])
        
    return customer_element
    
  def __ExtractInvoiceElement(self):
    body_children = lxml_functions.GetAllSubElements(self.body_root)
    for element in body_children:
      if element.tag == "Racun":
        invoice_element = copy.deepcopy(element)
    
    return invoice_element
  
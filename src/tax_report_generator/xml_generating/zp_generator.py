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



class ZPGenerator(xml_generator.XMLGenerator):
  def __init__(self, data_wrapper):
    self.__SetDataFrames(data_wrapper)
    
    report_name = xml_settings.zp_template
    self.SetAndLoadRootElements(report_name)
    
    self.ConstructReport()
    
    lxml_functions.WriteTreeToFile(self.wrapper_tree, xml_settings.zp_output_file)
    
  def __SetDataFrames(self, data_wrapper):
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.IRA_EU_file)
    self.IRA_EU = copy.deepcopy(data_wrapper.data_frames[name])
    self.IRA_EU = self.IRA_EU[(self.IRA_EU[data_settings.IRA_EU_goods_sold] != 0.0) | (self.IRA_EU[data_settings.IRA_EU_services_sold] != 0.0)]
    
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.customers_file)
    self.customers = copy.deepcopy(data_wrapper.data_frames[name])
    
  

  def CreateAndFillOutBody(self):
    body_element = self.__ExtractBodyElement()
    all_children = lxml_functions.GetAllSubElements(body_element)
    
    deliveries_element = self.__FillOutDeliveries()
    lxml_functions.InsertChildElementIntoElementAtIndex(deliveries_element, body_element, 0)
    
    for child_element in all_children:
      data = False
      child_tag = lxml_functions.GetTag(child_element)
    
      if child_tag == "I1":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("I1", deliveries_element)
        
      if child_tag == "I4":
        data = lxml_functions.GetSumOfAllSubElementsWithTagPatternOfElement("I4", deliveries_element)
        
      if (data != False):
        lxml_functions.SetElementText(child_element, data)
        
    return body_element
   
  
  def __FillOutDeliveries(self):
    deliveries_element = lxml_functions.CreateElement("Isporuke")
    
    delivery_counter = 1
    while (not self.IRA_EU.empty):
      customer_id = pandas_functions.GetFirstValueFromColumnFromFrame(data_settings.IRA_EU_customer_id, self.IRA_EU)
      
      delivery_batch, self.IRA_EU = pandas_functions.SplitFrameAlongColumnWithValue(self.IRA_EU, data_settings.IRA_EU_customer_id, customer_id)
      
      delivery_element = self.__FillOutDeliveryNumber(delivery_batch, delivery_counter)
      lxml_functions.AddChildElementToElement(delivery_element, deliveries_element)
      
      delivery_counter += 1
      
    return deliveries_element
       
  def __FillOutDeliveryNumber(self, delivery_batch, number):
      delivery_element = self.__ExtractDeliveryElement()
      all_children = lxml_functions.GetAllSubElements(delivery_element)
      
      customer_id = pandas_functions.GetFirstValueFromColumnFromFrame(data_settings.IRA_EU_customer_id, delivery_batch)
      
      for child_element in all_children:
        data = False
        child_tag = lxml_functions.GetTag(child_element)
      
        if child_tag == "RedBr":
          data = number
          
        elif child_tag == "KodDrzave":
          data = pandas_functions.GetValueFromColumnFromFrameIfColumnHasValue(data_settings.customers_country, self.customers, data_settings.customers_tax_number, customer_id)
          
        elif child_tag == "PDVID":
          data = customer_id
          
        elif child_tag == "I1":
          data = pandas_functions.SumColumnInFrame(data_settings.IRA_EU_goods_sold, delivery_batch)
          
        elif child_tag == "I4":
          data = pandas_functions.SumColumnInFrame(data_settings.IRA_EU_services_sold, delivery_batch)
          
        if (data != False):
          lxml_functions.SetElementText(child_element, data)
          
      return delivery_element
        
        
        
  def __ExtractBodyElement(self):
    body_element = copy.deepcopy(self.body_root)
    body_element.remove(body_element[0])
        
    return body_element
   
  def __ExtractDeliveryElement(self):
    body_children = lxml_functions.GetAllSubElements(self.body_root)
    for element in body_children:
      if element.tag == "Isporuka":
        delivery_element = copy.deepcopy(element)
        
    return delivery_element
  
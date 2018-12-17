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



class PDVSGenerator(xml_generator.XMLGenerator):
  def __init__(self, data_wrapper):
    self.__SetDataFrames(data_wrapper)
    
    report_name = xml_settings.pdvs_template
    self.SetAndLoadRootElements(report_name)
    
    self.ConstructReport()
    
    lxml_functions.WriteTreeToFile(self.wrapper_tree, xml_settings.pdvs_output_file)
    
  def __SetDataFrames(self, data_wrapper):
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.URA_EU_DC_file)
    self.URA_EU_DC = copy.deepcopy(data_wrapper.data_frames[name])
    
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.vendors_file)
    self.vendors = copy.deepcopy(data_wrapper.data_frames[name])
    
  

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
        
      if (data != False):
        lxml_functions.SetElementText(child_element, data)
        
    return body_element
   
  
  def __FillOutDeliveries(self):
    deliveries_element = lxml_functions.CreateElement("Isporuke")
    
    delivery_counter = 1
    while (not self.URA_EU_DC.empty):
      vendor_id = pandas_functions.GetFirstValueFromColumnFromFrame(data_settings.URA_EU_DC_vendor_id, self.URA_EU_DC)
      
      delivery_batch, self.URA_EU_DC = pandas_functions.SplitFrameAlongColumnWithValue(self.URA_EU_DC, data_settings.URA_EU_DC_vendor_id, vendor_id)
      
      delivery_element = self.__FillOutDeliveryNumber(delivery_batch, delivery_counter)
      lxml_functions.AddChildElementToElement(delivery_element, deliveries_element)
      
      delivery_counter += 1
      
    return deliveries_element
       
  def __FillOutDeliveryNumber(self, delivery_batch, number):
      delivery_element = self.__ExtractDeliveryElement()
      all_children = lxml_functions.GetAllSubElements(delivery_element)
      
      vendor_id = pandas_functions.GetFirstValueFromColumnFromFrame(data_settings.URA_EU_DC_vendor_id, delivery_batch)
      
      for child_element in all_children:
        data = False
        child_tag = lxml_functions.GetTag(child_element)
      
        if child_tag == "RedBr":
          data = number
          
        elif child_tag == "KodDrzave":
          data = pandas_functions.GetValueFromColumnFromFrameIfColumnHasValue(data_settings.vendors_country, self.vendors, data_settings.vendors_tax_number, vendor_id)
          
        elif child_tag == "PDVID":
          data = vendor_id
          
        elif child_tag == "I1":
          data = pandas_functions.SumColumnInFrame(data_settings.URA_EU_DC_tax_base, delivery_batch)
          
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
  
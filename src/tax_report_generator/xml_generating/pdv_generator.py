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



class PDVGenerator(xml_generator.XMLGenerator):
  def __init__(self, data_wrapper):
    self.__SetDataFrames(data_wrapper)
    
    report_name = xml_settings.pdv_template
    self.SetAndLoadRootElements(report_name)
    
    self.ConstructReport()
    
    lxml_functions.WriteTreeToFile(self.wrapper_tree, xml_settings.pdv_output_file)
    
  def __SetDataFrames(self, data_wrapper):
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.IRA_EU_file)
    self.IRA_EU = copy.deepcopy(data_wrapper.data_frames[name])
    
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.URA_EU_DC_file)
    self.URA_EU_DC = copy.deepcopy(data_wrapper.data_frames[name])
    
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.URA_EU_DOM_file)
    self.URA_EU_DOM = copy.deepcopy(data_wrapper.data_frames[name])
    
    name, extension = pathfinder.SplitFileNameIntoNameAndExtension(data_settings.URA_EU_UVOZ_file)
    self.URA_EU_UVOZ = copy.deepcopy(data_wrapper.data_frames[name])
    
  

  def CreateAndFillOutBody(self):
    body_element = self.__ExtractBodyElement()
    self.__FillNonSums(body_element)
    self.__FillSums(body_element)
    self.__FillFinalSum(body_element)
    
    return body_element
   
   
   
  def __FillNonSums(self, body_element):    
    children = lxml_functions.GetSubElements(body_element)
    
    for child_element in children:
      grand_children = lxml_functions.GetSubElements(child_element)
      if (len(grand_children) > 0):
        self.__FillNonSumWithChildren(child_element)
      else:
        self.__FillNonSumChildless(child_element)
  
  def __FillNonSumChildless(self, child_element):
    data = False
    child_tag = lxml_functions.GetTag(child_element)
        
    if child_tag == "Podatak103":
      data = pandas_functions.SumColumnInFrame(data_settings.IRA_EU_goods_sold, self.IRA_EU)
        
    elif child_tag == "Podatak104":
      data = pandas_functions.SumColumnInFrame(data_settings.IRA_EU_services_sold, self.IRA_EU)
      
    elif child_tag == "Podatak109":
      data = pandas_functions.SumColumnInFrame(data_settings.IRA_EU_exports, self.IRA_EU)
    
    if (data != False):
      lxml_functions.SetElementText(child_element, data)
    
  def __FillNonSumWithChildren(self, child_element):
    child_tag = lxml_functions.GetTag(child_element)
    grandchildren = lxml_functions.GetSubElements(child_element)
    
    for grandchild_element in grandchildren:
      data = False
      grandchild_tag = lxml_functions.GetTag(grandchild_element)
    
      if child_tag == "Podatak203":
        if grandchild_tag == "Vrijednost":
          data = pandas_functions.SumColumnInFrame(data_settings.IRA_EU_taxable_base, self.IRA_EU)
        elif grandchild_tag == "Porez":
          data = pandas_functions.SumColumnInFrame(data_settings.IRA_EU_taxable_tax, self.IRA_EU)
        
      elif child_tag == "Podatak207":
        if grandchild_tag == "Vrijednost":
          data = pandas_functions.SumColumnInFrame(data_settings.URA_EU_DC_tax_base, self.URA_EU_DC)
        elif grandchild_tag == "Porez":
          data = pandas_functions.SumColumnInFrame(data_settings.URA_EU_DC_total, self.URA_EU_DC)
          
          
        
      elif child_tag == "Podatak303":          
        if grandchild_tag == "Vrijednost":
          data = 4 * pandas_functions.SumColumnInFrame(data_settings.URA_EU_DOM_refundable, self.URA_EU_DOM)
        elif grandchild_tag == "Porez":
          data = pandas_functions.SumColumnInFrame(data_settings.URA_EU_DOM_refundable, self.URA_EU_DOM)
        
      elif child_tag == "Podatak307":
        if grandchild_tag == "Vrijednost":
          data = pandas_functions.SumColumnInFrame(data_settings.URA_EU_DC_tax_base, self.URA_EU_DC)
        elif grandchild_tag == "Porez":
          data = pandas_functions.SumColumnInFrame(data_settings.URA_EU_DC_total, self.URA_EU_DC)
        
      elif child_tag == "Podatak314":          
        if grandchild_tag == "Vrijednost":
          data = 4 * pandas_functions.SumColumnInFrame(data_settings.URA_EU_UVOZ_total, self.URA_EU_UVOZ)
        elif grandchild_tag == "Porez":
          data = pandas_functions.SumColumnInFrame(data_settings.URA_EU_UVOZ_total, self.URA_EU_UVOZ)
        
      if (data != False):
        lxml_functions.SetElementText(grandchild_element, data)
  
  
  
  def __FillSums(self, body_element):
    children = lxml_functions.GetSubElements(body_element)
    
    for child_element in children:
      grand_children = lxml_functions.GetSubElements(child_element)
      if (len(grand_children) > 0):
        pass
        self.__FillSumWithChildren(body_element, child_element)
      else:
        self.__FillSumChildless(body_element, child_element)
        
  def __FillSumChildless(self, body_element, child_element):
    data = False
    child_tag = lxml_functions.GetTag(child_element)
        
    if child_tag == "Podatak100":
      data = lxml_functions.GetSumOfSubElementsWithTagPatternOfElement("Podatak1", body_element)
    
    if (data != False):
      lxml_functions.SetElementText(child_element, data)
      
  def __FillSumWithChildren(self, body_element, child_element):
    child_tag = lxml_functions.GetTag(child_element)
    grandchildren = lxml_functions.GetSubElements(child_element)
    
    for grandchild_element in grandchildren:
      data = False
      grandchild_tag = lxml_functions.GetTag(grandchild_element)
    
      if child_tag == "Podatak200":
        pattern_elements = lxml_functions.GetSubElementsWithTagPattern(body_element, "Podatak2")
        sum = 0.0
        
        if grandchild_tag == "Vrijednost":
          for pattern_element in pattern_elements:
            sum += lxml_functions.GetSumOfSubElementsWithTagPatternOfElement("Vrijednost", pattern_element)
          data = sum
        elif grandchild_tag == "Porez":
          for pattern_element in pattern_elements:
            sum += lxml_functions.GetSumOfSubElementsWithTagPatternOfElement("Porez", pattern_element)
          data = sum
        
      elif child_tag == "Podatak300":
        pattern_elements = lxml_functions.GetSubElementsWithTagPattern(body_element, "Podatak3")
        sum = 0.0
          
        if grandchild_tag == "Vrijednost":
          for pattern_element in pattern_elements:
            sum += lxml_functions.GetSumOfSubElementsWithTagPatternOfElement("Vrijednost", pattern_element)
          data = sum
        elif grandchild_tag == "Porez":
          for pattern_element in pattern_elements:
            sum += lxml_functions.GetSumOfSubElementsWithTagPatternOfElement("Porez", pattern_element)
          data = sum
        
      if (data != False):
        lxml_functions.SetElementText(grandchild_element, data)
  
  
  
  def __FillFinalSum(self, body_element):
    children = lxml_functions.GetSubElements(body_element)
    
    podatak_000 = lxml_functions.GetSubElementsWithTagPattern(body_element, "Podatak000")[0]
    podatak_100 = lxml_functions.GetSubElementsWithTagPattern(body_element, "Podatak100")[0]
    podatak_200 = lxml_functions.GetSubElementsWithTagPattern(body_element, "Podatak200")[0]
    vrijednost_podatak_200 = lxml_functions.GetSubElementsWithTagPattern(podatak_200, "Vrijednost")[0]
    
    data = float(podatak_100.text) + float(vrijednost_podatak_200.text)
    lxml_functions.SetElementText(podatak_000, data)
        
        
  
  def __ExtractBodyElement(self):
    body_element = copy.deepcopy(self.body_root)
    return body_element
  
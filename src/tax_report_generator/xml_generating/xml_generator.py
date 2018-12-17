import os
from datetime import datetime
import uuid

from tax_report_generator.pathfinding import pathfinder
from tax_report_generator.xml_generating import lxml_functions
from tax_report_generator.settings import xml_settings
from tax_report_generator.settings import report_settings



class XMLGenerator(object):
  def SetAndLoadRootElements(self, report_name):
    wrapper_path = self.__GetWrapperPath(report_name)
    metadata_path = self.__GetMetadataPath(report_name)
    header_path = self.__GetHeaderPath(report_name)
    body_path = self.__GetBodyPath(report_name)
    
    self.wrapper_tree = lxml_functions.LoadTree(wrapper_path)
    metadata_tree = lxml_functions.LoadTree(metadata_path)
    header_tree = lxml_functions.LoadTree(header_path)
    body_tree = lxml_functions.LoadTree(body_path)
    
    self.wrapper_root = lxml_functions.GetRootElement(self.wrapper_tree)
    self.metadata_root = lxml_functions.GetRootElement(metadata_tree)
    self.header_root = lxml_functions.GetRootElement(header_tree)
    self.body_root = lxml_functions.GetRootElement(body_tree)
  
  def __GetWrapperPath(self, file_name):
    xml_template_path_components = [GetDirectoryPath(),
                                    xml_settings.xml_template_relative_path,
                                    xml_settings.xml_wrapper_relative_path,
                                    file_name]
    file_path = pathfinder.CreateAbsolutePath(xml_template_path_components)
    return file_path
  
  def __GetMetadataPath(self, file_name):
    xml_template_path_components = [GetDirectoryPath(),
                                    xml_settings.xml_template_relative_path,
                                    xml_settings.xml_metadata_relative_path,
                                    file_name]
    file_path = pathfinder.CreateAbsolutePath(xml_template_path_components)
    return file_path
  
  def __GetHeaderPath(self, file_name):
    xml_template_path_components = [GetDirectoryPath(),
                                    xml_settings.xml_template_relative_path,
                                    xml_settings.xml_header_relative_path,
                                    file_name]
    file_path = pathfinder.CreateAbsolutePath(xml_template_path_components)
    return file_path
  
  def __GetBodyPath(self, file_name):
    xml_template_path_components = [GetDirectoryPath(),
                                    xml_settings.xml_template_relative_path,
                                    xml_settings.xml_body_relative_path,
                                    file_name]
    file_path = pathfinder.CreateAbsolutePath(xml_template_path_components)
    return file_path
  
  
  
  def ConstructReport(self):
    self.__FillOutMetadata()
    lxml_functions.AddChildElementToElement(self.metadata_root, self.wrapper_root)
    
    self.__FillOutHeader()
    lxml_functions.AddChildElementToElement(self.header_root, self.wrapper_root)
    
    body_element = self.CreateAndFillOutBody()
    lxml_functions.AddChildElementToElement(body_element, self.wrapper_root)
    
    
    
  def __FillOutMetadata(self):
    for child_element in self.metadata_root:
      data = False
      child_tag = lxml_functions.GetTag(child_element)
      
      if child_tag == "Autor":
        data = report_settings.Autor
        
      elif child_tag == "Datum":
        data = self.GetIsoFormatDateTimeNow()
        
      elif child_tag == "Identifikator":
        data = self.GetUUID4()
      
      if (data != False):
        lxml_functions.SetElementText(child_element, data)
    
    
    
  def __FillOutHeader(self):
    all_children = lxml_functions.GetAllSubElements(self.header_root)
    for child_element in all_children:
      data = False
      child_tag = lxml_functions.GetTag(child_element)
      
      if child_tag == "DatumOd":
        data = report_settings.DatumOd
        
      elif child_tag == "DatumDo":
        data = report_settings.DatumDo
        
      elif child_tag == "OIB":
        data = report_settings.OIB
        
      elif child_tag == "Naziv":
        data = report_settings.Naziv
        
      elif child_tag == "Mjesto":
        data = report_settings.Mjesto
        
      elif child_tag == "Ulica":
        data = report_settings.Ulica
        
      elif child_tag == "Broj":
        data = report_settings.Broj
        
      elif child_tag == "Ime":
        data = report_settings.Ime
        
      elif child_tag == "Prezime":
        data = report_settings.Prezime
        
      elif child_tag == "Ispostava":
        data = report_settings.Ispostava
        
      elif child_tag == "NaDan":
        data = report_settings.NaDan
        
      elif child_tag == "NisuNaplaceniDo":
        data = report_settings.NisuNaplaceniDo
      
      if (data != False):
        lxml_functions.SetElementText(child_element, data)
  
  

  def GetIsoFormatDateTimeNow(self):
    return datetime.now().isoformat(timespec="seconds")
    
  def GetUUID4(self):
    return uuid.uuid4()
    
 
       
def GetDirectoryPath():
  return os.path.dirname(__file__)
  
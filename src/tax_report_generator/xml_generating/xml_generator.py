import os
from datetime import datetime
import uuid

from tax_report_generator.pathfinding import pathfinder
from tax_report_generator.settings import xml_settings



class XMLGenerator(object):
  def GetWrapperPath(self, file_name):
    xml_template_path_components = [GetDirectoryPath(),
                                    xml_settings.xml_template_relative_path,
                                    xml_settings.xml_wrapper_relative_path,
                                    file_name]
    file_path = pathfinder.CreateAbsolutePath(xml_template_path_components)
    return file_path
  
  def GetMetadataPath(self, file_name):
    xml_template_path_components = [GetDirectoryPath(),
                                    xml_settings.xml_template_relative_path,
                                    xml_settings.xml_metadata_relative_path,
                                    file_name]
    file_path = pathfinder.CreateAbsolutePath(xml_template_path_components)
    return file_path
  
  def GetHeaderPath(self, file_name):
    xml_template_path_components = [GetDirectoryPath(),
                                    xml_settings.xml_template_relative_path,
                                    xml_settings.xml_header_relative_path,
                                    file_name]
    file_path = pathfinder.CreateAbsolutePath(xml_template_path_components)
    return file_path
  
  def GetBodyPath(self, file_name):
    xml_template_path_components = [GetDirectoryPath(),
                                    xml_settings.xml_template_relative_path,
                                    xml_settings.xml_body_relative_path,
                                    file_name]
    file_path = pathfinder.CreateAbsolutePath(xml_template_path_components)
    return file_path
  
  

  def GetIsoFormatDateTimeNow(self):
    return datetime.now().isoformat(timespec="seconds")
    
  def GetUUID4(self):
    return uuid.uuid4()
   
 
       
def GetDirectoryPath():
  return os.path.dirname(__file__)
  
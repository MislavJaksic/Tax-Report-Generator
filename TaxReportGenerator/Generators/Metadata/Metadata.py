from lxml import etree
from datetime import datetime
from uuid import uuid4

class Metadata(object):

  def __init__(self, metadata_child_tags, metadata_attributes, metadata_content):
    self.metadata_child_tags = metadata_child_tags
    self.metadata_attributes = metadata_attributes
    self.metadata_content = metadata_content
  
  def Construct(self):
    tag = "Metapodaci"
    metadata = self._CreateElements(tag)
    return metadata
    
  def _CreateElements(self, tag):
    element = etree.Element(tag, attrib=self.metadata_attributes[tag])
    
    if self._HasChildren(tag):
      for child_tag in self.metadata_child_tags[tag]:
        child_element = self._CreateElements(child_tag)
        element.append(child_element)
    else:
      element.text = self._ChooseContent(tag)
      
    return element
    
  def _HasChildren(self, tag):
    if tag in self.metadata_child_tags.keys():
      return True
    return False
    
  def _ChooseContent(self, tag):
    if tag == "Datum":
      content = self._FormatDateTime(self._GetNowDateTime())
    elif tag == "Identifikator":
      content = self._GetUUID4()
    elif tag == "Adresant":
      content = self.metadata_content[tag]
    else:
      content = self.metadata_content[tag]
      
    return content
	
  def _GetNowDateTime(self):
    time = datetime.now()
    return time
    
  def _FormatDateTime(self, time):
    formattedTime = time.strftime("%Y-%m-%dT%H:%M:%S")
    return formattedTime
    
  def _GetUUID4(self):
    return str(uuid4())
    
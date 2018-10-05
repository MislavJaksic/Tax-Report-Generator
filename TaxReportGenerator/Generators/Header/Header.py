from lxml import etree

class Header(object):
  
  def __init__(self, header_child_tags, header_content):
    self.header_child_tags = header_child_tags
    self.header_content = header_content
    
  def Construct(self):
    tag = "Zaglavlje"
    header = self._CreateElements(tag)
    return header
    
  def _CreateElements(self, tag):
    element = etree.Element(tag)
    
    if self._HasChildren(tag):
      for child_tag in self.header_child_tags[tag]:
        child_element = self._CreateElements(child_tag)
        element.append(child_element)
    else:
      element.text = self._ChooseContent(tag)
      
    return element
    
  def _HasChildren(self, tag):
    if tag in self.header_child_tags.keys():
      return True
    return False
    
  def _ChooseContent(self, tag):
    content = self.header_content[tag]
    return content
    
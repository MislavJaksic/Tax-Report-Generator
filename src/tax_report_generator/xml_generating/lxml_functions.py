import copy
import pandas
from lxml import etree

from tax_report_generator.data_wrangling import transform_data



def LoadTree(file_path):
    tree = etree.parse(file_path)
    return tree
    
def GetRootElement(tree):
  root = tree.getroot()
  return root

  
  
def CreateElement(tag):
  return etree.Element(tag)

def GetTag(element):
  tag_with_namespace_prefix = element.tag
  return GetTagWithoutNamespacePrefix(tag_with_namespace_prefix)
  
def GetTagWithoutNamespacePrefix(tag_with_namespace_prefix):
  return tag_with_namespace_prefix.split("}")[-1]
  
def SetElementText(element, data):
  if type(data) is float:
    data = transform_data.RoundHalfUp(data, 2)
    
  if type(data) is pandas._libs.tslibs.timedeltas.Timedelta:
    if (data.components.hours == 0):
      if (data.components.minutes == 0):
        if (data.components.seconds == 0):
          data = transform_data.GetDays(data)
          
  if type(data) is pandas._libs.tslibs.timestamps.Timestamp:
    data = transform_data.GetDate(data)
    
  element.text = str(data)  
  
  
  
def AddChildElementToElement(child_element, element):
  child_copy = copy.deepcopy(child_element)
  element.append(child_copy)
 
def InsertChildElementIntoElementAtIndex(child_element, element, index):
  child_copy = copy.deepcopy(child_element)
  element.insert(index, child_copy)
 
def GetAllSubElements(parent_element):
  child_elements = list(parent_element)
  
  for child_element in parent_element:
    child_elements.extend(GetAllSubElements(child_element))
  
  return child_elements

  
  
def GetSumOfNameElementsOfElement(name, element):
  all_children = GetAllSubElements(element)
  sum = 0.0
  for child_element in all_children:
    child_tag = GetTagWithoutNamespacePrefix(child_element.tag)
    if (child_tag == name):
      sum += float(child_element.text)
      
  return sum
  
  

def WriteTreeToFile(tree, file_name):
  tree.write(file_name)
  
def PrintTree(tree):
  root = GetTreeRoot(tree)
  PrintElement(root)
  
def PrintElement(element):
  print(etree.tostring(element, pretty_print=True))
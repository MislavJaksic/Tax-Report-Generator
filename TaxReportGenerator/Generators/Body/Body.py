# -*- encoding: utf-8 -*-
from lxml import etree

class Tijelo(object):
  
  def __init__(self, companies):
    self.companies = companies
    
    self.body_child_tags = False
    self.body = False
    
  def _CreateElements(self, parent_tag, current_tag):
    element = etree.Element(current_tag)
    
    if self._HasChildren(current_tag):
      for child_tag in self.body_child_tags[current_tag]:
        child_element = self._CreateElements(current_tag, child_tag)
        element.append(child_element)
    else:
      element.text = self._ChooseContent(parent_tag, current_tag)
      
    return element
    
  def _HasChildren(self, tag):
    if tag in self.body_child_tags.keys():
      return True
    return False
    
  def GetCountryCode(self, OIB):
    if (self.HasLeadingZero(OIB)):
      while (True):
        company = self.FindRowsInDataFrameWithValueInColumn(self.companies, OIB, u"Porezni broj")
        if not (self.HasLeadingZero(OIB)):
          break
        OIB = OIB[1:]
        
    else:
      company = self.FindRowsInDataFrameWithValueInColumn(self.companies, OIB, u"Porezni broj")
    
    if (company.empty):
      return u'ERROR_COUNTRY_CODE'
      
    countryCode = str(company[u"Država/regija"].iloc[0])
    return countryCode
    
  def HasLeadingZero(self, OIB):
    return (OIB[0] == "0")
    
  def FindRowsInDataFrameWithValueInColumn(self, dataframe, value, column):
    return (dataframe[dataframe[column] == value])
    
  def GroupAndSumDataFrameByColumn(self, dataframe, column):
    return dataframe.groupby(column).sum()
    
  def FloatToTwoDecimalString(self, number):
    string = "%.2f" % round(number, 2)
    return string
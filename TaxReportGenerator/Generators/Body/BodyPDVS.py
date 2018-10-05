# -*- encoding: utf-8 -*-
from TaxReportGenerator.Generators.Body.Body import Tijelo
from TaxReportGenerator.Generators.Body.BodyConstants import BodyConstantsPDVS
from lxml import etree

class TijeloPDVS(Tijelo):
  
  def __init__(self, URA_EU_DC, vendors):
    super(TijeloPDVS, self).__init__(vendors)
    
    self.URA_EU_DC_iter = self._CreateURA_EU_DCIter(URA_EU_DC)
    self.current_row = False
    
    self.body_child_tags = BodyConstantsPDVS.child_tags
    
    self.row_counter = 1
    self.total_sum = 0
    
  def _CreateURA_EU_DCIter(self, URA_EU_DC):
    grouped_by_URA = self.GroupAndSumDataFrameByColumn(URA_EU_DC, u"Dobavljač - OIB")
    return grouped_by_URA.iterrows()
    
  def Construct(self):
    self.body = etree.Element("Tijelo")
    isporuke = etree.Element("Isporuke")
    
    for URA_EU_DC_row in self.URA_EU_DC_iter:
      self.current_row = URA_EU_DC_row
      
      isporuka = self._CreateElements("Isporuke", "Isporuka")
      isporuke.append(isporuka)
      
    self.body.append(isporuke)
      
    self._ChooseSumContent()
    return self.body
       
  def _ChooseContent(self, parent_tags, tag):
    content = "ERROR_WRONG_ELE_NAME"
    
    if tag == "RedBr":
      content = str(self.row_counter)
      self.row_counter += 1
      
    elif tag == "KodDrzave":
      OIB = self.current_row[0]
      country_code = self.GetCountryCode(OIB)
      content = country_code
      
    elif tag == "PDVID":
      OIB = self.current_row[0]
      content = str(OIB)
      
    elif tag == "I1":
      sum = self.current_row[1].iloc[0]
      self.total_sum += sum
      content = self.FloatToTwoDecimalString(sum)
      
    elif tag == "I2":
      content = "0"
      
    return content
    
  def _ChooseSumContent(self):
    isporuke_ukupno = etree.Element("IsporukeUkupno")
    
    I1 = etree.Element("I1")
    I1.text = self.FloatToTwoDecimalString(self.total_sum)
    isporuke_ukupno.append(I1)
    
    I2 = etree.Element("I2")
    I2.text = "0"
    isporuke_ukupno.append(I2)
    
    self.body.append(isporuke_ukupno)
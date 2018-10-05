# -*- encoding: utf-8 -*-
from TaxReportGenerator.Generators.Body.Body import Tijelo
from TaxReportGenerator.Generators.Body.BodyConstants import BodyConstantsZP
from lxml import etree

class TijeloZP(Tijelo):
  
  def __init__(self, customers, IRA_EU):
    super(TijeloZP, self).__init__(customers)
    
    self.IRA_EU_iter = self.CreateIRA_EUIter(IRA_EU)
    self.current_row = False
    
    self.body_child_tags = BodyConstantsZP.child_tags
    
    self.row_counter = 1
    self.total_goods_sum = 0
    self.total_services_sum = 0
    
  def CreateIRA_EUIter(self, IRA_EU):
    grouped_by_IRA = self.GroupAndSumDataFrameByColumn(IRA_EU, u"Kupac - OIB/PDV ID")
    none_zeroes_IRA = grouped_by_IRA[(grouped_by_IRA[u"Isporuke dobara unutar EU"] != 0.0) | (grouped_by_IRA[u"Obavljene usluge unutar EU"] != 0.0)]
    return none_zeroes_IRA.iterrows()
    
  def Construct(self):
    self.body = etree.Element("Tijelo")
    isporuke = etree.Element("Isporuke")
    
    for IRA_EU_row in self.IRA_EU_iter:
      self.current_row = IRA_EU_row
      
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
      OIB = str(self.current_row[0])
      country_code = self.GetCountryCode(OIB)
      content = country_code
      
    elif tag == "PDVID":
      OIB = str(self.current_row[0])
      content = str(OIB)
      
    elif tag == "I1":
      sum = self.current_row[1].iloc[0]
      self.total_goods_sum += sum
      content = self.FloatToTwoDecimalString(sum)
      
    elif tag == "I2":
      content = "0"
      
    elif tag == "I3":
      content = "0"
      
    elif tag == "I4":
      sum = self.current_row[1].iloc[1]
      self.total_services_sum += sum
      content = self.FloatToTwoDecimalString(sum)
      
    return content
    
  def _ChooseSumContent(self):
    isporuke_ukupno = etree.Element("IsporukeUkupno")
    
    I1 = etree.Element("I1")
    I1.text = self.FloatToTwoDecimalString(self.total_goods_sum)
    isporuke_ukupno.append(I1)
    
    I2 = etree.Element("I2")
    I2.text = "0"
    isporuke_ukupno.append(I2)
    
    I3 = etree.Element("I3")
    I3.text = "0"
    isporuke_ukupno.append(I3)
    
    I4 = etree.Element("I4")
    I4.text = self.FloatToTwoDecimalString(self.total_services_sum)
    isporuke_ukupno.append(I4)
    
    self.body.append(isporuke_ukupno)
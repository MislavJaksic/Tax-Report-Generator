# -*- encoding: utf-8 -*-
from TaxReportGenerator.Generators.Body.Body import Tijelo
from TaxReportGenerator.Generators.Body.BodyConstants import BodyConstantsPDV
from lxml import etree

class TijeloPDV(Tijelo):
  
  def __init__(self, IRA_EU, URA_EU_DC, URA_EU_DOM, URA_EU_UVOZ):
    self.IRA_EU = IRA_EU
    self.URA_EU_DC = URA_EU_DC
    self.URA_EU_DOM = URA_EU_DOM
    self.URA_EU_UVOZ = URA_EU_UVOZ
    
    self.body_child_tags = BodyConstantsPDV.child_tags
    
    self.sum_100 = 0
    self.sum_200_vrijednost = 0
    self.sum_200_porez = 0
    self.sum_300_vrijednost = 0
    self.sum_300_porez = 0
  
  def Construct(self):
    tag = "Tijelo"
    self.body = self._CreateElements("None", tag)
    self._ChooseSumContent()
    return self.body
    
  def _ChooseContent(self, parent_tags, tag):
    if tag == "Podatak000":
      content = "ERROR_SUM"
      
    elif tag == "Podatak100":
      content = "ERROR_SUM"
      
    elif tag == "Podatak103":
      content = self.FloatToTwoDecimalString(self.IRA_EU[u"Isporuke dobara unutar EU"].sum())
      self.sum_100 += float(content)
      
    elif tag == "Podatak104":
      content = self.FloatToTwoDecimalString(self.IRA_EU[u"Obavljene usluge unutar EU"].sum())
      self.sum_100 += float(content)
      
    elif tag == "Podatak109":
      content = self.FloatToTwoDecimalString(self.IRA_EU[u"Izvozne isporuke"].sum())
      self.sum_100 += float(content)
      
      
    elif "Podatak200" in parent_tags:
      if tag == "Vrijednost":
        content = "ERROR_SUM"
      if tag == "Porez":
        content = "ERROR_SUM"
      
    elif "Podatak203" in parent_tags:
      if tag == "Vrijednost":
        content = self.FloatToTwoDecimalString(self.IRA_EU[u"Oporezivo 25% - osnovica"].sum())
        self.sum_200_vrijednost += float(content)
      if tag == "Porez":
        content = self.FloatToTwoDecimalString(self.IRA_EU[u"Oporezivo 25% - porez"].sum())
        self.sum_200_porez += float(content)
      
    elif "Podatak207" in parent_tags:
      if tag == "Vrijednost":
        content = self.FloatToTwoDecimalString(self.URA_EU_DC[u"Porezna osnovica 25%"].sum())
        self.sum_200_vrijednost += float(content)
      if tag == "Porez":
        content = self.FloatToTwoDecimalString(self.URA_EU_DC[u"Ukupno"].sum())
        self.sum_200_porez += float(content)
      
      
    elif "Podatak300" in parent_tags:
      if tag == "Vrijednost":
        content = "ERROR_SUM"
      if tag == "Porez":
        content = "ERROR_SUM"
      
    elif "Podatak303" in parent_tags:
      if tag == "Vrijednost":
        content = self.FloatToTwoDecimalString(self.URA_EU_DOM[u"Pretporez 25% - može se odbiti"].sum() * 4)
        self.sum_300_vrijednost += float(content)
      if tag == "Porez":
        content = self.FloatToTwoDecimalString(self.URA_EU_DOM[u"Pretporez 25% - može se odbiti"].sum())
        self.sum_300_porez += float(content)
      
    elif "Podatak307" in parent_tags:
      if tag == "Vrijednost":
        content = self.FloatToTwoDecimalString(self.URA_EU_DC[u"Porezna osnovica 25%"].sum())
        self.sum_300_vrijednost += float(content)
      if tag == "Porez":
        content = self.FloatToTwoDecimalString(self.URA_EU_DC[u"Ukupno"].sum())
        self.sum_300_porez += float(content)
      
    elif "Podatak314" in parent_tags:
      if tag == "Vrijednost":
        content = self.FloatToTwoDecimalString(self.URA_EU_UVOZ[u"Ukupno"].sum() * 4)
        self.sum_300_vrijednost += float(content)
      if tag == "Porez":
        content = self.FloatToTwoDecimalString(self.URA_EU_UVOZ[u"Ukupno"].sum())
        self.sum_300_porez += float(content)
        
      
    elif tag == "Podatak400":
      content = "ERROR_SUM"
      
    elif tag == "Podatak600":
      content = "ERROR_SUM"
      
    elif tag == "Podatak870":
      content = "false"
      
    else:
      content = "0"
      
    return content
  
  def _ChooseSumContent(self):
    podatak_100 = self.body.find("Podatak100")
    podatak_100.text = self.FloatToTwoDecimalString(self.sum_100)
    
    podatak_200_vrijednost = self.body.find("Podatak200").find("Vrijednost")
    podatak_200_vrijednost.text = self.FloatToTwoDecimalString(self.sum_200_vrijednost)
    
    podatak_200_porez = self.body.find("Podatak200").find("Porez")
    podatak_200_porez.text = self.FloatToTwoDecimalString(self.sum_200_porez)
    
    podatak_300_vrijednost = self.body.find("Podatak300").find("Vrijednost")
    podatak_300_vrijednost.text = self.FloatToTwoDecimalString(self.sum_300_vrijednost)
    
    podatak_300_porez = self.body.find("Podatak300").find("Porez")
    podatak_300_porez.text = self.FloatToTwoDecimalString(self.sum_300_porez)
    
    podatak_400 = self.body.find("Podatak400")
    podatak_600 = self.body.find("Podatak600")
    podatak_400.text = podatak_600.text = self.FloatToTwoDecimalString(self.sum_200_porez - self.sum_300_porez)
    
    podatak_000 = self.body.find("Podatak000")
    podatak_000.text = self.FloatToTwoDecimalString(float(podatak_100.text) + float(podatak_200_vrijednost.text))
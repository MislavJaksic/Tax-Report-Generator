from TaxReportGenerator.Settings import LegalSettings
from TaxReportGenerator.Generators.Body.BodyConstants import BodyConstantsOPZ
from TaxReportGenerator.Generators.Body.Body import Tijelo
from copy import copy
from lxml import etree
from datetime import datetime

class TijeloOPZ(Tijelo):
  
  def __init__(self, customers, invoices):
    super(TijeloOPZ, self).__init__(customers)

    self.CreateInvoiceIter(invoices)
    self.NextInvoice()
    
    self.kupacCounter = 1
    
    self.ResetKSums()
    
    self.UkupanIznosRacunaObrasca = 0
    self.UkupanIznosPdvObrasca = 0
    self.UkupanIznosRacunaSPdvObrasca = 0
    self.UkupniPlaceniIznosRacunaObrasca = 0
    self.NeplaceniIznosRacunaObrasca = 0
    
  def CreateInvoiceIter(self, invoices):
    self.invoiceIter = invoices.iterrows()
    
  def Construct(self):
    return self.CreateTijelo()
    
  def CreateTijelo(self):
    Tijelo = etree.Element("Tijelo")
    
    Tijelo.append(self.CreateKupci())
    
    for TijeloSumName in BodyConstantsOPZ.TijeloSumNames:
      TijeloSum = self.CreateTijeloSum(TijeloSumName)
      Tijelo.append(TijeloSum)
    
    return Tijelo
    
  def CreateKupci(self):
    Kupci = etree.Element("Kupci")
    
    while not (self.IsInvoiceEndOfFile()):
      self.AddToTijeloSums()
      self.ResetKSums()
      
      Kupci.append(self.CreateKupac())
    self.AddToTijeloSums()
          
    return Kupci
    
  def AddToTijeloSums(self):
    self.UkupanIznosRacunaObrasca += self.K5
    self.UkupanIznosPdvObrasca += self.K6
    self.UkupanIznosRacunaSPdvObrasca += self.K7
    self.UkupniPlaceniIznosRacunaObrasca += self.K8
    self.NeplaceniIznosRacunaObrasca += self.K9
  
  def ResetKSums(self):
    self.K5 = 0
    self.K6 = 0
    self.K7 = 0
    self.K8 = 0
    self.K9 = 0
  
  def CreateKupac(self):
    Kupac = etree.Element("Kupac")
    
    self.SetLastCustomerName()
    self.ResetRacunCounter()
    Racuni = self.CreateRacuni()
    
    for KName in BodyConstantsOPZ.KNames:
      K = self.CreateK(KName)
      Kupac.append(K)

    Kupac.append(Racuni)
    
    return Kupac
    
  def SetLastCustomerName(self):
    self.lastCustomerName = self.invoice[u'Customer Name']
    
  def ResetRacunCounter(self):
    self.racunCounter = 1
    
  def CreateRacuni(self):
    Racuni = etree.Element("Racuni")
    
    while (self.IsSameCustomer() and not self.IsInvoiceEndOfFile()):
      Racun = self.CreateRacun()
      Racuni.append(Racun)
      
      self.NextInvoice()
      
    return Racuni
    
  def IsSameCustomer(self):
    return (self.invoice[u'Customer Name'] == self.lastCustomerName)
  
  def IsInvoiceEndOfFile(self):
    return (self.index == -1)
      
  def CreateRacun(self):
    Racun = etree.Element("Racun")
    
    for RName in BodyConstantsOPZ.RNames:
      R = self.CreateR(RName)
      Racun.append(R)
    
    return Racun
    
  def CreateR(self, RName):
    R = etree.Element(RName)
    
    invoiceAmount = self.ToNumber(self.invoice[BodyConstantsOPZ.invoiceAmountString])
    openAmount = self.ToNumber(self.invoice[BodyConstantsOPZ.openAmountString])
    
    if RName == "R1":
      R.text = str(self.racunCounter)
      self.racunCounter += 1
      
    elif RName == "R2":
      R.text = self.invoice[u'Invoice Nr']
      
    elif RName == "R3":
      R.text = self.ToDateFormat(self.invoice[u'Posting date'])
      
    elif RName == "R4": 
      R.text = self.ToDateFormat(self.invoice[u'Due Date'])
      
    elif RName == "R5":
      daysLate = self.CalculateLatePaymentInDays(self.invoice[u'Due Date'])
      R.text = daysLate
      
    elif RName == "R6":
      amountDue = invoiceAmount / (1 + LegalSettings.tax_rate)
      R.text = self.FloatToTwoDecimalString(amountDue)
      self.K5 += amountDue
      
    elif RName == "R7":
      taxAmount = invoiceAmount - invoiceAmount / (1 + LegalSettings.tax_rate)
      R.text = self.FloatToTwoDecimalString(taxAmount)
      self.K6 += taxAmount
      
    elif RName == "R8":
      R.text = self.FloatToTwoDecimalString(invoiceAmount)
      self.K7 += invoiceAmount
      
    elif RName == "R9":
      R.text = self.FloatToTwoDecimalString(invoiceAmount - openAmount)
      self.K8 = self.K8 + invoiceAmount - openAmount
      
    elif RName == "R10":
      R.text = self.FloatToTwoDecimalString(openAmount)
      self.K9 += openAmount
      
    else:
      R.text = "ERROR_CREATE_R"
    return R
    
  def ToNumber(self, stringNumber):
    """Transform "123.456,78" to 123456.78"""
    return stringNumber
    
  def ToDateFormat(self, timestamp):
    """Transform timestamp(2017-05-30 00:00:00) to 2017-05-30"""
    string_date = str(timestamp)[0:10]
    return string_date
  
  def CalculateLatePaymentInDays(self, dueDateTimestamp):
    """Days that elapsed between DueDate and a fixed date"""
    fixedDate = datetime.strptime(LegalSettings.NisuNaplaceniDo, "%Y-%m-%d")
    paymentLate = fixedDate - dueDateTimestamp

    return str(paymentLate.days)
    
  def NextInvoice(self):
    try:
      self.index, self.invoice = next(self.invoiceIter)
    except StopIteration:
      self.index = -1
      
  def CreateK(self, KName):
    K = etree.Element(KName)
    
    if KName == "K1":
      K.text = str(self.kupacCounter)
      self.kupacCounter += 1
      
    elif KName == "K2":
      K.text = BodyConstantsOPZ.OznakaPoreznogBroja
      
    elif KName == "K3":
      taxNumber = self.GetTaxNumber(self.lastCustomerName)
      K.text = taxNumber
      
    elif KName == "K4":
      K.text = self.lastCustomerName
      
    elif KName == "K5":
      K.text = self.FloatToTwoDecimalString(self.K5)
      
    elif KName == "K6":
      K.text = self.FloatToTwoDecimalString(self.K6)
      
    elif KName == "K7":
      K.text = self.FloatToTwoDecimalString(self.K7)
      
    elif KName == "K8":
      K.text = self.FloatToTwoDecimalString(self.K8)
      
    elif KName == "K9":
      K.text = self.FloatToTwoDecimalString(self.K9)
      
    else:
      K.text = "ERROR_CREATE_K"
    return K
  
  def GetTaxNumber(self, customerName):
    customer = self.FindRowsInDataFrameWithValueInColumn(self.companies, customerName, u"Naziv")
    if (customer.empty):
      return u'ERROR_TAX_NUMBER'
      
    taxNumber = str(customer[u'Porezni broj'].iloc[0])
    taxNumber = self.AddLeadingZeros(taxNumber)
    return taxNumber
    
  def AddLeadingZeros(self, taxNumber):
    """OIB has to have eleven digits."""
    while (len(taxNumber) < 11):
      taxNumber = "0" + taxNumber
    return taxNumber
     
  def CreateTijeloSum(self, totalSumName):
    totalSum = etree.Element(totalSumName)
    
    if totalSumName == "UkupanIznosRacunaObrasca":
      totalSum.text = self.FloatToTwoDecimalString(self.UkupanIznosRacunaObrasca)
      
    if totalSumName == "UkupanIznosPdvObrasca":
      totalSum.text = self.FloatToTwoDecimalString(self.UkupanIznosPdvObrasca)
      
    if totalSumName == "UkupanIznosRacunaSPdvObrasca":
      totalSum.text = self.FloatToTwoDecimalString(self.UkupanIznosRacunaSPdvObrasca)
      
    if totalSumName == "UkupniPlaceniIznosRacunaObrasca":
      totalSum.text = self.FloatToTwoDecimalString(self.UkupniPlaceniIznosRacunaObrasca)
      
    if totalSumName == "NeplaceniIznosRacunaObrasca":
      totalSum.text = self.FloatToTwoDecimalString(self.NeplaceniIznosRacunaObrasca)
      
    if totalSumName == "OPZUkupanIznosRacunaSPdv":
      totalSum.text = BodyConstantsOPZ.OPZUkupanIznosRacunaSPdv
      
    if totalSumName == "OPZUkupanIznosPdv":
      totalSum.text = BodyConstantsOPZ.OPZUkupanIznosPdv
      
    return totalSum

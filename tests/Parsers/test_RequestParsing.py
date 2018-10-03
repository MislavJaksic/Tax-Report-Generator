from TaxReportGenerator.Parsers import RequestParsing

import pytest



def test_IdentifyRequiredDataExpected():
  reports = ["OPZ", "ZP"]
  assert RequestParsing.IdentifyRequiredData(reports) == set(["customers", "invoices", "IRA_EU"])
  
def test_IdentifyRequiredDataNoInput():
  reports = []
  assert RequestParsing.IdentifyRequiredData(reports) == set([])
  
def test_IdentifyRequiredDataBadInput():
  reports = ["nonsense"]
  assert RequestParsing.IdentifyRequiredData(reports) == set([])
  
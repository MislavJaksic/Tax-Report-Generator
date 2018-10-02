# -*- encoding: utf-8 -*-

from TaxReportGenerator.Parsers import RequestParsing

import pytest



def test_IdentifyRequiredData():
  reports = ["OPZ", "ZP"]
  assert RequestParsing.IdentifyRequiredData(reports) == set(["customers", "invoices", "IRA_EU"])
  
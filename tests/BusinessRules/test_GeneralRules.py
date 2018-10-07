import datetime
import numpy as np
import pandas
import math
from TaxReportGenerator.DataManipulation import Loading
from TaxReportGenerator.Containers.ExcelInfoContainer import ExcelInfoContainer
from TaxReportGenerator.Settings import TestSettings
from TaxReportGenerator.Settings import DataSettings
from TaxReportGenerator.BusinessRules import GeneralRules

import pytest



def test_ChangeValueToNull():
  column_name = "column"
  nan_value = "nan"
  data = pandas.DataFrame({column_name : ["1.0", "2", "3", nan_value]});
  
  assert pandas.isnull(data.at[3,column_name]) == False
  
  data = GeneralRules.ChangeValueToNaNInDataFrame(nan_value, data)

  assert pandas.isnull(data.at[3,column_name])
  
  
@pytest.fixture(scope='function')
def TestExcel():
  data_types = {"integers" : "int8",
                "float_integers" : "f",
                "integer_floats" : "int8",
                "floats" : "f",
                "strings" : "U",
                "dates" : "M"}
  data = pandas.read_excel(io=TestSettings.sample_data_file_path,
                           usecols=TestSettings.sample_data_excel_columns,
                           dtype=data_types,
                           skipfooter=1,
                          )
  return data
  
def test_FinancialRound(TestExcel):
  TestExcel = GeneralRules.FinancialRound(TestExcel)
  
  assert math.isclose(TestExcel.at[1,"floats"], 2.01, abs_tol=0.000001)
  assert math.isclose(TestExcel.at[2,"floats"], 3.00, abs_tol=0.000001)
  
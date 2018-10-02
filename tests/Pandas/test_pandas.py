# -*- encoding: utf-8 -*-

import pandas
import numpy
import datetime
from TaxReportGenerator.Settings import TestSettings

import pytest



def test_PandasReadStringAndDate():
  file_path = TestSettings.data_file_path
  rename_columns = ["name_one", "name_two"]
  excel_columns = "B,C"
  data_types = {"numbers" : "U", "dates" : "M"}
  data = pandas.read_excel(io=file_path,
                           names=rename_columns,
                           usecols=excel_columns,
                           dtype=data_types,
                           skipfooter=1,
                          )
                          
  assert data.at[2,rename_columns[0]] == "11.0"
  assert data.at[2,rename_columns[1]] == datetime.datetime(2013,3,3)
  
def test_PandasReadFloatAndDate():
  file_path = TestSettings.data_file_path
  rename_columns = ["name_one", "name_two"]
  excel_columns = "B,C"
  data_types = {"numbers" : "f", "dates" : "M"}
  data = pandas.read_excel(io=file_path,
                           names=rename_columns,
                           usecols=excel_columns,
                           dtype=data_types,
                           skipfooter=1,
                          )
                          
  assert data.at[2,rename_columns[0]] == 11.0
  assert data.at[2,rename_columns[1]] == datetime.datetime(2013,3,3)
  
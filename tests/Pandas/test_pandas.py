# -*- encoding: utf-8 -*-

import pandas
import numpy
import datetime
from TaxReportGenerator.Settings import TestSettings

import pytest



def test_PandasReadString():
  file_path = TestSettings.sample_data_file_path
  rename_columns = TestSettings.sample_data_renaming_labels
  excel_columns = TestSettings.sample_data_excel_columns
  data_types = {"numbers" : "U", "dates" : "M"}
  data = pandas.read_excel(io=file_path,
                           names=rename_columns,
                           usecols=excel_columns,
                           dtype=data_types,
                           skipfooter=1,
                          )
                          
  assert data.at[2,rename_columns[0]] == "11.0"
  
def test_PandasReadFloat():
  file_path = TestSettings.sample_data_file_path
  rename_columns = TestSettings.sample_data_renaming_labels
  excel_columns = TestSettings.sample_data_excel_columns
  data_types = {"numbers" : "f", "dates" : "M"}
  data = pandas.read_excel(io=file_path,
                           names=rename_columns,
                           usecols=excel_columns,
                           dtype=data_types,
                           skipfooter=1,
                          )
                          
  assert data.at[2,rename_columns[0]] == 11.0
  
def test_PandasReadDate():
  file_path = TestSettings.sample_data_file_path
  rename_columns = TestSettings.sample_data_renaming_labels
  excel_columns = TestSettings.sample_data_excel_columns
  data_types = {"numbers" : "f", "dates" : "M"}
  data = pandas.read_excel(io=file_path,
                           names=rename_columns,
                           usecols=excel_columns,
                           dtype=data_types,
                           skipfooter=1,
                          )
                          
  assert data.at[2,rename_columns[1]] == datetime.datetime(2013,3,3)
  
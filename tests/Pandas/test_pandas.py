# -*- encoding: utf-8 -*-

import pandas
import datetime
import math
from TaxReportGenerator.Settings import TestSettings

import pytest

@pytest.fixture(scope='module')
def TestExcel():
  data_types = {"integers" : "int8",
                "float_integers" : "f",
                "integer_floats" : "int8",
                "floats" : "f",
                "strings" : "U",
                "dates" : "M"}
  data = pandas.read_excel(io=TestSettings.sample_data_file_path,
                           names=TestSettings.sample_data_renaming_labels,
                           usecols=TestSettings.sample_data_excel_columns,
                           dtype=data_types,
                           skipfooter=1,
                          )
  return data
  
def test_PandasReadInteger(TestExcel):
  assert TestExcel.at[2,TestSettings.sample_data_renaming_labels[0]] == 3

def test_PandasReadFloatInteger(TestExcel):
  assert TestExcel.at[2,TestSettings.sample_data_renaming_labels[1]] == 3.0

def test_PandasReadIntegerFloat(TestExcel):
  assert TestExcel.at[2,TestSettings.sample_data_renaming_labels[2]] == 3
  
def test_PandasReadFloat(TestExcel):
  assert math.isclose(TestExcel.at[2,TestSettings.sample_data_renaming_labels[3]], 3.00001, abs_tol=0.001)

def test_PandasReadString(TestExcel):
  assert TestExcel.at[2,TestSettings.sample_data_renaming_labels[4]] == "world"

def test_PandasReadDates(TestExcel):
  assert TestExcel.at[2,TestSettings.sample_data_renaming_labels[5]] == datetime.datetime(2013,3,3)
  
def test_PandasReadEmptyCall(TestExcel):
  assert pandas.isnull(TestExcel.at[0,TestSettings.sample_data_renaming_labels[1]])
  
import datetime
import numpy as np
import pandas
from TaxReportGenerator.DataManipulation import Loading
from TaxReportGenerator.Containers.ExcelInfoContainer import ExcelInfoContainer
from TaxReportGenerator.Settings import TestSettings
from TaxReportGenerator.Settings import DataSettings
from TaxReportGenerator.BusinessRules import GeneralRules

import pytest



def test_ChangeValueToNull():
  column_name = "column"
  nan_value = "nan"
  data = pandas.DataFrame({column_name : [1.0, 2, 3, nan_value]});
  
  assert pandas.isnull(data.at[3,column_name]) == False
  
  data = GeneralRules.ChangeValueToNaNInDataFrame(nan_value, data)

  assert pandas.isnull(data.at[3,column_name])
  
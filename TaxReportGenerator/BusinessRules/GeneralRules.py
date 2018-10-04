import numpy as np



def ChangeValueToNaNInDataFrame(value, pandas_dataframe):
  pandas_dataframe = pandas_dataframe.replace(value, np.nan)
  return pandas_dataframe
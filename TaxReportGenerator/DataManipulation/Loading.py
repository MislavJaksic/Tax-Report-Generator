# -*- encoding: utf-8 -*-

import os
import sys
import inspect
folder_list = os.path.abspath(inspect.getfile(inspect.currentframe())).split("\\")
folder = folder_list.pop()
while (folder_list[-1] != "TaxReportGenerator"):
  folder_list.pop()
sys.path.append(os.path.dirname("\\".join(folder_list)))

import pandas



def LoadExcel(settings):
  """
  https://pandas.pyDataSettings.org/pandas-docs/stable/generated/pandas.read_excel.html
  """
  data = pandas.read_excel(io=settings["file_path"],
                           sheet_name=settings["sheet_name"],
                           header=settings["header"],
                           names=settings["names"],
                           index_col=settings["index_col"],
                           usecols=settings["usecols"],
                           squeeze=settings["squeeze"],
                           dtype=settings["dtype"],
                           engine=settings["engine"],
                           converters=settings["converters"],
                           true_values=settings["true_values"],
                           false_values=settings["false_values"],
                           skiprows=settings["skiprows"],
                           nrows=settings["nrows"],
                           na_values=settings["na_values"],
                           keep_default_na=settings["keep_default_na"],
                           verbose=settings["verbose"],
                           parse_dates=settings["parse_dates"],
                           date_parser=settings["date_parser"],
                           thousands=settings["thousands"],
                           comment=settings["comment"],
                           skipfooter=settings["skipfooter"],
                           convert_float=settings["convert_float"],
                          )
  return data

def GetExcelSettings(file_path, table_info, skip_footer):
  names = table_info.GetColumnNames()
  letters = table_info.GetColumnLetters()
  data_types = table_info.GetDataTypes()
  settings = {"file_path" : file_path,
              "sheet_name" : 0,
              "header" : 0,
              "names" : names,
              "index_col" : None,
              "usecols" : ",".join(letters),
              "squeeze" : False,
              "dtype" : data_types,
              "engine" : None,
              "converters" : None,
              "true_values" : None,
              "false_values" : None,
              "skiprows" : None,
              "nrows" : None,
              "na_values" : None,
              "keep_default_na" : True,
              "verbose" : True,
              "parse_dates" : False,
              "date_parser" : None,
              "thousands" : None,
              "comment" : None,
              "skipfooter" : skip_footer,
              "convert_float" : True,
             }
  return settings

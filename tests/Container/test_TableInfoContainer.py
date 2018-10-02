# -*- encoding: utf-8 -*-

from TaxReportGenerator.Containers.TableInfoContainer import TableInfoContainer

import pytest



def test_GetInfoAt():
  table_info = TableInfoContainer()
  table_info.AddColumnTuple(("C", "Useful_Two", "float"))
  table_info.AddColumnTuple(("B", "Useful_One", "float"))
  
  assert table_info.GetInfoAt(0) == ["B", "C"]
  
def test_GetDictByKeyValuePosition():
  table_info = TableInfoContainer()
  table_info.AddColumnTuple(("C", "Useful_Two", "float"))
  table_info.AddColumnTuple(("B", "Useful_One", "float"))
  
  assert table_info.GetDictByKeyValuePosition(1,2) == {"Useful_One" : "float", "Useful_Two" : "float"}

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

import context
from tax_report_generator.command_line_parsing import parser
from tax_report_generator.data_wrangling import data_wrapper
from tax_report_generator.xml_generating import opz_generator
from tax_report_generator.xml_generating import pdv_generator
from tax_report_generator.xml_generating import pdvs_generator
from tax_report_generator.xml_generating import zp_generator

from tax_report_generator.data_wrangling import pandas_functions



#Main will be run if you run this script directly
def Main():
  command_line_parser = parser.Parser()
  arguments = command_line_parser.GetArguments()
  file_names = command_line_parser.GetFileNames()
  
  data = data_wrapper.DataFrameWrapper(file_names)
    
  if arguments.OPZ:
    opz_generator.OPZGenerator(data)
  if arguments.PDV:
    pdv_generator.PDVGenerator(data)
  if arguments.PDVS:
    pdvs_generator.PDVSGenerator(data)
  if arguments.ZP:
    zp_generator.ZPGenerator(data)



#Entry point for the runnable script (defined in setup.py)
def Run():
  sys.exit(Main())

if __name__ == '__main__':
  Run()
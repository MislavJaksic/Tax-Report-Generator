import sys
import argparse

from tax_report_generator.settings import data_settings



class Parser(object):
  def __init__(self):
    self.parser = argparse.ArgumentParser()
    self.__AddArguments()
    
    if (self.__IsNoArguments()):
      self.__PrintHelpAndExit()
    
  def __AddArguments(self):
    self.__AddOptionalArgument("-pdv", "--PDV", "Generate PDV tax report.", True)
    self.__AddOptionalArgument("-pdvs", "--PDVS", "Generate PDVS tax report.", True)
    self.__AddOptionalArgument("-zp", "--ZP", "Generate ZP tax report.", True)
    self.__AddOptionalArgument("-opz", "--OPZ", "Generate OPZ tax report.", True)
    
  def __AddOptionalArgument(self, short_option, long_option, help_text, is_boolean):
    if (is_boolean):
      self.parser.add_argument(short_option,
                               long_option,
                               help=help_text,
                               action="store_true")
    else:
      self.parser.add_argument(short_option,
                               long_option,
                               help=help_text)
  
  

  def __IsNoArguments(self):
    args = self.GetArguments()
    args = vars(args)
    
    for arg in args.values():
      if arg:
        return False
    return True
    
  def __PrintHelpAndExit(self):
    self.parser.print_help(sys.stderr)
    sys.exit(1)
    
   

  def GetArguments(self):
    return self.parser.parse_args()
    
  def GetFileNames(self):
    args = self.GetArguments()
    file_names = []
    
    if (args.PDV):
      file_names.append(data_settings.IRA_EU_file)
      file_names.append(data_settings.URA_EU_DC_file)
      file_names.append(data_settings.URA_EU_DOM_file)
      file_names.append(data_settings.URA_EU_UVOZ_file)
    
    if (args.PDVS):
      file_names.append(data_settings.URA_EU_DC_file)
      file_names.append(data_settings.vendors_file)
      
    if (args.ZP):
      file_names.append(data_settings.customers_file)
      file_names.append(data_settings.IRA_EU_file)
      
    if (args.OPZ):
      file_names.append(data_settings.customers_file)
      file_names.append(data_settings.invoices_file)
    
    file_names_without_duplicates = set(file_names)
    
    return file_names_without_duplicates
    
import os
import sys
import inspect
folder_list = os.path.abspath(inspect.getfile(inspect.currentframe())).split("\\")
folder = folder_list.pop()
while (folder_list[-1] != "TaxReportGenerator"):
  folder_list.pop()
sys.path.append(os.path.dirname("\\".join(folder_list)))

import sys
from Parsers import RequestParsing
from Containers import TablesContainer
from Generators import Report



if __name__ == '__main__':
  command_line_arguments = sys.argv[1:]
  required_data = RequestParsing.IdentifyRequiredData(command_line_arguments)
  
  report_data = TablesContainer.TablesContainer(required_data)
  
  for report_name in command_line_arguments:
    report = Report.Report(report_name, report_data)
    
    report.Construct()
    report.ToFile(report_name + ".xml")
    print("Report called " + report_name + " has been generated.")
  
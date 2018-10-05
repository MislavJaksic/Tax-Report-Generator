# -*- encoding: utf-8 -*-

import os
import sys
import inspect
folder_list = os.path.abspath(inspect.getfile(inspect.currentframe())).split("\\")
folder = folder_list.pop()
while (folder_list[-1] != "TaxReportGenerator"):
  folder_list.pop()
sys.path.append(os.path.dirname("\\".join(folder_list)))



from TaxReportGenerator.Generators.Constants import ReportConstants, MetadataConstants, HeaderConstants

from TaxReportGenerator.Generators.Metadata.Metadata import Metadata

from TaxReportGenerator.Generators.Header.Header import Header

from TaxReportGenerator.Generators.Body.BodyOPZ import TijeloOPZ
from TaxReportGenerator.Generators.Body.BodyPDV import TijeloPDV
from TaxReportGenerator.Generators.Body.BodyPDVS import TijeloPDVS
from TaxReportGenerator.Generators.Body.BodyZP import TijeloZP

from lxml import etree

class Report(object):
    
  def __init__(self, report_name, report_data):
    self.report_name = report_name
    self.report_data = report_data
    
    self.report_root = self._GetReportRoot()
    self.metadata = self._GetMetadata()
    self.header = self._GetHeader()
    self.body = self._GetBody() 
    
  def _GetReportRoot(self):
    if self.report_name == "OPZ":
      report_root = etree.Element("ObrazacOPZ", attrib=ReportConstants.attributes["ObrazacOPZ"])
    elif self.report_name == "PDV":
      report_root = etree.Element("ObrazacPDV", attrib=ReportConstants.attributes["ObrazacPDV"])
    elif self.report_name == "PDVS":
      report_root = etree.Element("ObrazacPDVS", attrib=ReportConstants.attributes["ObrazacPDVS"])
    elif self.report_name == "ZP":
      report_root = etree.Element("ObrazacZP", attrib=ReportConstants.attributes["ObrazacZP"])
      
    return report_root
    
  def _GetMetadata(self):
    child_tags = MetadataConstants.child_tags
    attributes = MetadataConstants.attributes
    
    if self.report_name == "OPZ":
      content = MetadataConstants.OPZ_content
    elif self.report_name == "PDV":
      content = MetadataConstants.PDV_content
    elif self.report_name == "PDVS":
      content = MetadataConstants.PDVS_content
    elif self.report_name == "ZP":
      content = MetadataConstants.ZP_content
    
    metadata = Metadata(child_tags, attributes, content)
    return metadata
             
  def _GetHeader(self):
    content = HeaderConstants.content
    if self.report_name == "OPZ":
      child_tags = HeaderConstants.OPZ_child_tags
    else:
      child_tags = HeaderConstants.non_OPZ_child_tags
    
    header = Header(child_tags, content)
    return header
    
  def _GetBody(self):
    if self.report_name == "OPZ":
      body = TijeloOPZ(self.report_data.customers, self.report_data.invoices)
    elif self.report_name == "PDV":
      body = TijeloPDV(self.report_data.IRA_EU, self.report_data.URA_EU_DC, self.report_data.URA_EU_DOM, self.report_data.URA_EU_UVOZ)
    elif self.report_name == "PDVS":
      body = TijeloPDVS(self.report_data.URA_EU_DC, self.report_data.vendors)
    elif self.report_name == "ZP":
      body = TijeloZP(self.report_data.customers, self.report_data.IRA_EU)
    
    return body
    
  def ToFile(self, file_path):
    XML = etree.ElementTree(self.report_root)
    XML.write(file_path)
      

  def ToString(self):
    print(etree.tostring(self.report_root, pretty_print=True))
    
  def Construct(self):
    metadata_XML = self.metadata.Construct()
    self.report_root.append(metadata_XML)
    
    header_XML = self.header.Construct()
    self.report_root.append(header_XML)

    body_XML = self.body.Construct()
    self.report_root.append(body_XML)
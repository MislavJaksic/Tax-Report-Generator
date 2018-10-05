# -*- encoding: utf-8 -*-

import os
import sys
import inspect
folder_list = os.path.abspath(inspect.getfile(inspect.currentframe())).split("\\")
folder = folder_list.pop()
while (folder_list[-1] != "TaxReportGenerator"):
  folder_list.pop()
sys.path.append(os.path.dirname("\\".join(folder_list)))



from TaxReportGenerator.Settings import LegalSettings
from copy import copy

child_tags = {"Metapodaci" : ["Naslov", "Autor", "Datum", "Format", "Jezik", "Identifikator", "Uskladjenost", "Tip", "Adresant"],
              }

base_string = "http://purl.org/dc/elements/1.1/"
attributes = {"Metapodaci":   {"xmlns" : "http://e-porezna.porezna-uprava.hr/sheme/Metapodaci/v2-0"},
              "Naslov":       {"dc" : base_string + "title"},
			        "Autor":        {"dc" : base_string + "creator"},
			        "Datum":        {"dc" : base_string + "date"},
			        "Format":       {"dc" : base_string + "format"},
			        "Jezik":        {"dc" : base_string + "language"},
			        "Identifikator":{"dc" : base_string + "identifier"},
			        "Uskladjenost": {"dc" : "http://purl.org/dc/terms/conformsTo"},
			        "Tip":          {"dc" : base_string + "type"},
			        "Adresant":     {}
			        }
        
base_content = {"Metapodaci":   u"ERROR_METADATA",
                 "Autor":        LegalSettings.Autor,
                 "Naslov":       u"ERROR_TITLE",
                 "Datum":        u"ERROR_DATE", 
                 "Format":       u"text/xml", 
                 "Jezik":        u"hr-HR", 
                 "Identifikator":u"ERROR_UUID", 
                 "Uskladjenost": u"ERROR_COMPATIBILITY",
                 "Tip":          u"Elektronički obrazac", 
                 "Adresant":     u"Ministarstvo Financija, Porezna uprava, Zagreb"
                 }
                
ZP_content = copy(base_content)               
ZP_content["Naslov"]       = u"Zbirna prijavu za isporuke dobara i usluga u druge države članice Europske unije"
ZP_content["Uskladjenost"] = u"ObrazacZP-v1-0"

OPZ_content = copy(base_content)  
OPZ_content["Naslov"]       = u"Obrazac OPZ"
OPZ_content["Uskladjenost"] = u"ObrazacOPZ-v1-0"

PDV_content = copy(base_content)  
PDV_content["Naslov"]       = u"Prijava poreza na dodanu vrijednost"
PDV_content["Uskladjenost"] = u"ObrazacPDV-v9-0"

PDVS_content = copy(base_content)  
PDVS_content["Naslov"]       = u"Prijava za stjecanje dobara i primljene usluge iz drugih država članica Europske unije"
PDVS_content["Uskladjenost"] = u"ObrazacPDVS-v1-0"

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

non_OPZ_child_tags = {"Zaglavlje" : ["Razdoblje", "Obveznik", "ObracunSastavio", "Ispostava"],
                      "Razdoblje" : ["DatumOd", "DatumDo"],
                      "Obveznik" : ["Naziv", "OIB", "Adresa"],
                      "Adresa" : ["Mjesto", "Ulica", "Broj"],
                      "ObracunSastavio" : ["Ime", "Prezime"],
                      }
                      
OPZ_child_tags = {"Zaglavlje" : ["Razdoblje", "PorezniObveznik", "IzvjesceSastavio", "NaDan", "NisuNaplaceniDo"],
                  "Razdoblje" : ["DatumOd", "DatumDo"],
                  "PorezniObveznik" : ["OIB", "Naziv", "Adresa"],
                  "Adresa" : ["Mjesto", "Ulica", "Broj"],
                  "IzvjesceSastavio" : ["Ime", "Prezime"],
                  }

content = {"Zaglavlje" : u"ERROR_HEADER",
           "Razdoblje" : u"ERROR_RAZDOBLJE",
           "DatumOd" : LegalSettings.DatumOd,
           "DatumDo" : LegalSettings.DatumDo,
           "Obveznik" : u"ERROR_OBVEZNIK",
           "PorezniObveznik" : u"ERROR_OBVEZNIK",
           "Naziv" : LegalSettings.Naziv,
           "OIB" : LegalSettings.OIB,
           "Adresa" : u"ERROR_ADDRESS",
           "Mjesto" : LegalSettings.Mjesto,
           "Ulica" : LegalSettings.Ulica,
           "Broj" : LegalSettings.Broj,
           "ObracunSastavio" : u"ERROR_SASTAVIO",
           "IzvjesceSastavio": u"ERROR_SASTAVIO",
           "Ime" : LegalSettings.Ime,
           "Prezime" : LegalSettings.Prezime,
           "Ispostava" : LegalSettings.Ispostava,
           "NaDan" : LegalSettings.NaDan,
           "NisuNaplaceniDo" : LegalSettings.NisuNaplaceniDo,
           }

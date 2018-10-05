# -*- encoding: utf-8 -*-

import os
import sys
import inspect
folder_list = os.path.abspath(inspect.getfile(inspect.currentframe())).split("\\")
folder = folder_list.pop()
while (folder_list[-1] != "TaxReportGenerator"):
  folder_list.pop()
sys.path.append(os.path.dirname("\\".join(folder_list)))



from TaxReportGenerator.Settings import DataSettings

invoiceAmountString = DataSettings.invoice_amount_invoices
openAmountString = DataSettings.open_amount_invoices
#Total sum element names:
TijeloSumNames = ["UkupanIznosRacunaObrasca", "UkupanIznosPdvObrasca", "UkupanIznosRacunaSPdvObrasca", "UkupniPlaceniIznosRacunaObrasca", "NeplaceniIznosRacunaObrasca", "OPZUkupanIznosRacunaSPdv", "OPZUkupanIznosPdv"]
#Total sum data:
OPZUkupanIznosRacunaSPdv = OPZUkupanIznosPdv = "0"
#Kx element names:
KNames = ["K1","K2","K3","K4","K5","K6","K7","K8","K9"]
#Kx data:
K2 = OznakaPoreznogBroja = "1"
#Rx element names:
RNames = ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10"]
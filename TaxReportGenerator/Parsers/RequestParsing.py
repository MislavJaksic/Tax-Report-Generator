from TaxReportGenerator.Settings import DataSettings



def IdentifyRequiredData(reports):
  required_data = []
  
  if "PDV" in reports:
    required_data.append(DataSettings.IRA_EU)
    required_data.append(DataSettings.URA_EU_DC)
    required_data.append(DataSettings.URA_EU_DOM)
    required_data.append(DataSettings.URA_EU_UVOZ)
    
  if "PDVS" in reports:
    required_data.append(DataSettings.URA_EU_DC)
    required_data.append(DataSettings.vendors)
    
  if "ZP" in reports:
    required_data.append(DataSettings.customers)
    required_data.append(DataSettings.IRA_EU)
    
  if "OPZ" in reports:
    required_data.append(DataSettings.customers)
    required_data.append(DataSettings.invoices)
    
  return set(required_data)

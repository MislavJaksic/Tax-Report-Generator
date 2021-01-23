import math



def AddLeadingZerosToStringUntilLength( number, length):
    string = str(number)
    while (len(string) < length):
      string = "0" + string
    return string
    
    

def GetDate(time_date):
  return time_date.date()

def GetDays(time_delta):
  return time_delta.components.days


        
def ScientificRoundToDecimals(number, decimals):
  return RoundHalfUp(number, decimals)

def RoundHalfUp(n, decimals):
  multiplier = 10 ** decimals
  return math.floor(n*multiplier + 0.5) / multiplier
class ExcelInfoContainer(object):

  def __init__(self, initial_tuples=[]):
    self.array = []
    for tuple in initial_tuples:
      self.AddExcelLetterColumnHeaderDataTypeTuple(tuple)
    
  def __str__(self):
    pretty_info = ""
    for tuple in self.array:
      pretty_info += str(tuple)
      pretty_info += "\n"
    return pretty_info
    
    
    
  def AddExcelLetterColumnHeaderDataTypeTuple(self, tuple):
    self.array.append(tuple)
    self.array = sorted(self.array, key=lambda tuple: tuple[0])
    
  def GetInfoAt(self, position):
    array = []
    for tuple in self.array:
      array.append(tuple[position])
    return array
    
  def GetDictByKeyValuePosition(self, key_position, value_position):
    dict = {}
    for tuple in self.array:
      key = tuple[key_position]
      value = tuple[value_position]
      dict[key] = value 
    return dict

    
    
  def GetColumnLetters(self):    
    return self.GetInfoAt(0)
  
  def GetColumnNames(self):
    return self.GetInfoAt(1)
  
  def GetDataTypes(self):
    return self.GetDictByKeyValuePosition(1,2)
    
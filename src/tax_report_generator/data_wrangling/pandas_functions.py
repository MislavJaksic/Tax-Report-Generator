import pandas



def GetColumnFromFrame(column, frame):
  return frame[column]
  
def GetFirstValueFromColumnFromFrame(column, frame):
  values = GetColumnValuesFromFrame(column, frame)
  return values[0]
  
def GetValueFromColumnFromFrameIfColumnHasValue(value_column, frame, search_column, value):
  rows = GetRowsInFrameWithValueInColumn(frame, value, search_column)
  if rows.empty:
    rows = GetRowsInFrameWithValueInColumn(frame, str(value), search_column)
  if rows.empty:
    rows = GetRowsInFrameWithValueInColumn(frame, int(value), search_column)
  if not rows.empty:
    value = GetFirstValueFromColumnFromFrame(value_column, rows)
  else:
    value = "ERROR_NO_VALUE_FOUND"
  return value
  
def GetColumnValuesFromFrame(column, frame):
  return frame[column].values
  
def GetColumnNames(frame):
  return frame.columns
  
def SumColumnInFrame(column, frame):
  return frame[column].sum()
  


  
  
def SplitFrameAlongColumnWithValue(frame, column, value):
  positive_frame = GetRowsInFrameWithValueInColumn(frame, value, column)
  negative_frame = GetRowsInFrameWithoutValueInColumn(frame, value, column)
  return positive_frame, negative_frame
  
def IsFrameEmpty(frame):
  if (frame.empty):
    return True
  return False
  
def IsFrameNotEmpty(frame):
  if (IsFrameEmpty(frame)):
    return False
  return True
  
  
  
def GetRowsInFrameWithValueInColumn(frame, value, column):
  return frame[frame[column] == value]
    
def GetRowsInFrameWithoutValueInColumn(frame, value, column):
  return frame[frame[column] != value]
  
def GetRowsInFrameGreaterThenValueInColumn(frame, value, column):
  return frame[frame[column] > value]

def GetRowsInFrameLessThenValueInColumn(frame, value, column):
  return frame[frame[column] < value]
  
def GetRowsInFrameNotNullValuesInColumn(frame, column):
  return frame[frame[column].notnull()]
import pandas


def GetColumnFromFrame(column, frame):
  return frame[column]
  
def GetColumnValuesFromFrame(column, frame):
  return frame[column].values

  
  
def SplitFrameAlongColumnWithValue(frame, column, value):
  positive_frame = GetRowsInFrameWithValueInColumn(frame, value, column)
  negative_frame = GetRowsInFrameWithoutValueInColumn(frame, value, column)
  return positive_frame, negative_frame
  
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
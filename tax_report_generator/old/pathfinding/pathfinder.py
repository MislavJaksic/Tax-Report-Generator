import os
import sys



def CreateRelativePath(path_elements):
  path = os.path.join(path_elements[0])
  for element in path_elements[1:]:
    path = os.path.join(path, element)
    
  return path

def CreateAbsolutePath(path_elements):
  full_path = CreateRelativePath(path_elements)
  return os.path.abspath(full_path)

  
  
def SplitFileNameIntoNameAndExtension(file_name):
  name, extension = file_name.split(".")
  return name, extension
  
  
  
def GetDirectoryPath():
  return os.path.dirname(__file__)
  
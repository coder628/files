import os
import json

class Files:
  def __init__(self):
    pass
  def read(self, filename, type):
    if type == None:
      type='.txt'
    elif type == '.txt' or'text' or 'txt':
      type='.txt'
      
    elif type == '.json' or 'json':
      type=='.json'  
    else:
      raise TypeError(f"Sorry we do not have the '{type}' format")
    filename=str(filename+type)
    if type=='.json':
      with open(filename, 'r')as file:
      contentes=json.load(file)
    elif type == '.txt'
      with open(filename, 'r')as file:
        contents=file.read()
    print(contents)
    
    def write(self, filename, text, type):
      text=str(text)
      if type == None:
      type='.txt'
    elif type == '.txt' or'text' or 'txt':
      type='.txt'
      
    elif type == '.json' or 'json':
      type=='.json'  
    else:
      raise TypeError(f"Sorry we do not have the '{type}' format")
    filename=str(filename+type)
    if type=='.json':
      with open(filename, 'r')as file:
      json.dump(text, file)
      print(f"We have successfully writen to {filename}")
    elif type == '.txt'
      with open(filename, 'r')as file:
        file.write(text)
        print(f"We have successfully writen to {filename}")
    

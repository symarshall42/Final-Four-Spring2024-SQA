import json
import random 
import csv
import numpy


file_path = 'output.csv'

def addonef(v1):
   mystring = " "
   lista =[1,2,3]
   if(v1=='' or v1 == None):
      x=0
   try:
      lista.append(v1)
   except AssertionError as e:
      mystring ="Error:  in equate -"+str(e)
   except EOFError as e:
      mystring ="Error: Type error during open -"+str(e)
   except AttributeError as e:
      mystring ="bad value"+str(e)
   return mystring

def divide(v1, v2):
   mystring = " "
   try:
      if(v1=="" or v2 == ""):
         x=0
      else:
         int(float(v1))/int(float(v2))
   except ZeroDivisionError as e:
      mystring ="Error: Division by zero -"+str(e)
   except TypeError as e:
      mystring ="Error: Type error during division -"+str(e)
   except ValueError as e:
      mystring ="bad value"+str(e)
   except OverflowError as e:
      mystring ="Error: overflow -"+str(e)
   return mystring
def multi(v1, v2):
   mystring = " "
   try:
      if(v1=="" or v2 == ""):
         x=0
      else:
         int(float(v1))*int(float(v2))
   except OverflowError as e:
      mystring ="Error: overflow -"+str(e)
   except TypeError as e:
      mystring ="Error: Type error during division -"+str(e)
   except ValueError as e:
      mystring ="bad value"+str(e)
   return mystring
def unique(v1):
   mystring = " "
   try:
      if(v1==""):
         x=0
      else:
        numpy.unique(v1)
   except OverflowError as e:
      mystring ="Error: overflow -"+str(e)
   except TypeError as e:
      mystring ="Error: Type error during division -"+str(e)
   except ValueError as e:
      mystring ="bad value"+str(e)
   return mystring
def rangers(v1):
   mystring = " "
   try:
      if(v1==""):
         x=0
      else:
        for stills in range(v1):
            y=0
   except OverflowError as e:
      mystring ="Error: overflow -"+str(e)
   except TypeError as e:
      mystring ="Error: Type error during division -"+str(e)
   except ValueError as e:
      mystring ="bad value"+str(e)
   return mystring

def simpleFuzzer():
   listdiv = []
   listmulti = []
   listrans = []
   addone1 = []
   listnp = []
   f = open('blns.json')
   data = json.load(f)
   ls_ = list(data)
   for x in ls_:
      if isinstance(x, str):
         mod_x = x + str( random.randint(1, 10) )
      elif isinstance(x, int): 
         mod_x = x + random.random()  
      listdiv.append(divide(x, mod_x))
      listmulti.append(multi(x, mod_x))
      listnp.append(unique(x))
      addone1.append(addonef(mod_x))
      listrans.append(rangers(x))
   merged_list = [["error list"]]
   merged_list.append([["1st list"]])
   merged_list.append(listdiv)
   merged_list.append([["2ed list"]])
   merged_list.append(listmulti)
   merged_list.append([["3rd list"]])
   merged_list.append(listnp)
   merged_list.append([["4th list"]])
   merged_list.append(addone1)
   merged_list.append([["5th list"]])
   merged_list.append(listrans)
   
   with open(file_path, 'w') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)
    
    # Write data to the CSV file
    csv_writer.writerows(merged_list)
   
   
if __name__=='__main__':
    simpleFuzzer()

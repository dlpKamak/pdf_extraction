# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 12:03:17 2020
Need to test for all three input types
Mention the block issues due to indentations
two modules 

@author: PreethiK
"""
import json
import re
with open('parsed_document_Output.json') as f:
  data = json.load(f)
  i = 0
  dict = {}
  print(data)
  start = 0
  startkey = 0
#Extract headings from the parsed document and create a dictionary of 
#index for headings present
  for headings in data:
      z = re.match(r"^<h.*>.*|$",headings)
      z2 = re.match(r"^<p.*>['Course'|'Program']+ Learning ['Objectives'|'Outcomes']+.*",headings)  
      i = i+1
      if z:
          print( (z.group()).strip() , i )
          dict[z.group()] = i
      if z2:
          print( (z2.group()).replace("<p>", "<h>") , i )
          dict[(z2.group()).replace("<p>", "<h>")] = i
  
  print("DICTIONARY ITEMS")  
  for (k,v) in dict.items():     
      print(k,v)
 
#Identify the learning outcome headings from the dictionary 
#and extract start and end indexes for the paragraph

  for (k,v) in dict.items():
      z1 = re.match(r"^<h.*>['Course'|'Program']+ Learning ['Objectives'|'Outcomes']+.*",k)
      if (z1):
            print(z1.group())
            start = v
            startkey = k
            print("start",startkey)
            print("---------------")
            break
  
  temp = iter(dict) 
  for key in temp:
      if key == startkey: 
        endkey = next(temp, None)


  if endkey != None:  
      end = dict[endkey]
      print("end",endkey)
  else: 
      end = start
      print("end NA",endkey)
     

  output = ""
  for para in range(start -1 , end-1):
       output += data[para] 
       
  
  if (len(output)<600):
      temp1 = iter(dict) 
      for key in temp1:
          print(key.index)
          if key == endkey: 
            endkey1 = next(temp1, None)
            print("new end1",endkey1)
           
    
    
      if endkey1 != None:  
          end = dict[endkey1]
          print("new end1",endkey1)
      else: 
          end = start
          print("end NA",endkey1)
      newoutput = ""
      for para in range(start -1 , end-1):
          newoutput += data[para]                
      oldoutput = output
      output = newoutput
          
#Remove the metadata tags present in the output extract

  tags = ["|","<p>","<h2>" , "<h1>" ]

  for key in tags:
        output = output.replace( key, "")
  print("---------------")
  print("output length",len(output) )
  print("output",output )
        
#The final formatted output extract is available  
  file1 = open("LearningOutcome_Output.txt","w") 
  file1.write(output) 
  file1.close() 

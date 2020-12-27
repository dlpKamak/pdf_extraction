# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 12:03:17 2020

@author: PreethiK
"""
import json
import re
with open('parsed_document_Output.json') as f:
  data = json.load(f)
  i = 0
  dict = {}
  
#Extract headings from the parsed document and create a dictionary of 
#index for headings present
  for headings in data:
      z = re.match(r"^<h.*>.*|$",headings)
      i = i+1
      if z:
         # print( (z.group()).strip() , i )
          dict[z.group()] = i
 
#Identify the learning outcome headings from the dictionary 
#and extract start and end indexes for the paragraph

  for (k,v) in dict.items():
      z1 = re.match(r"<h.*>.*Learning.*|$",k)
      if (z1):
            start = v
            startkey = k
  
  temp = iter(dict) 
  for key in temp:
      if key == startkey: 
        endkey = next(temp, None) 
     
  end = dict[endkey]    

  output = ""
  for para in range(start -1 , end-1):
       output += data[para] 
       
#Remove the metadata tags present in the output extract

  tags = ["|","<p>","<h2>" , "<h1>" ]

  for key in tags:
        output = output.replace( key, "")
        
#The final formatted output extract is available

  file1 = open("LearningOutcome_Output.txt","w") 
  file1.write(output) 
  file1.close() 

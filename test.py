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
  start = 0
  startkey = 0
  dict = {}
  
  for headings in data:
      z = re.search(r"^<h.*>$",headings)
      i = i+1
      if z:
          flag = 1
          break
      else:
          flag = 0

  for headings in data:     
      z2 = re.match(r"^<p.*>['Course'|'Program']+ Learning ['Objectives'|'Outcomes']+.*",headings)  
      if z2:
          print( (z2.group()).replace("<p>", "<h>") , i )
 

 
   
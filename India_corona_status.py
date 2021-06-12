# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:10:04 2020

@author: abcd
"""

import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import os 
import numpy as np 
import matplotlib.pyplot as plt 


extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
URL = 'https://www.mohfw.gov.in/'
  
SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed', 
                 'Foreign-Confirmed','Cured','Death'] 
  
response = requests.get(URL).content 
soup = BeautifulSoup(response, 'html.parser') 
header = extract_contents(soup.tr.find_all('th')) 
  
stats = [] 
all_rows = soup.find_all('tr') 
  
for row in all_rows: 
    stat = extract_contents(row.find_all('td')) 
    if stat: 
        if len(stat) == 5: 
            # last row 
            stat = ['', *stat] 
            stats.append(stat) 
        elif len(stat) == 6: 
            stats.append(stat) 
  
stats[-1][1] = "Total Cases"
  
stats.remove(stats[-1])
objects = [] 
for row in stats : 
    objects.append(row[1])  
  
x_pos = np.arange(len(objects)) 
  
performance = [] 
for row in stats : 
    performance.append(row[2] + row[3]) 
  
table = tabulate(stats, headers=SHORT_HEADERS) 
print(table)

plt.barh(x_pos, performance, align='center', alpha=0.5, 
                 color=(234/256.0, 128/256.0, 252/256.0), 
                 edgecolor=(106/256.0, 27/256.0, 154/256.0)) 
  
plt.xticks(x_pos, objects) 
plt.ylim(1,15) 
plt.ylabel('Number of Cases') 
plt.title('Corona Virus Cases') 
plt.show() 
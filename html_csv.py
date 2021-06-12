#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:00:37 2019

@author: root
"""

import csv

def html_table_creator(cs,ht):

    start=r'<html><body><h1>student marks</h1><table border="4" cellpadding="5"><tr><th>sl.no</th><th>roll.no</th><th>name</th><th>year</th><th>percent</th></tr>'

    end=r'</table></body></html>'

    ht.write(start)

    for i in csv.reader(cs):

        ht.write(r'<tr>')

        for j in i:

            ht.write(r'<td>')

            ht.write(j)

            ht.write(r'</td>')

        ht.write(r'</tr>')

    ht.write(end)

if __name__=='__main__':
    print('Enter name,year,percentage')
    with open('marks_sample.csv', 'w') as cs:
        spamwriter = csv.writer(cs, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(4):
            spamwriter.writerow(str(i+1)+',50'+str(i+1)+','+input())
    cs=open('marks_sample.csv')
    ht=open('table.html','w')

    html_table_creator(cs,ht)

    cs.close()

    ht.close()
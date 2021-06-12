# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:56:19 2020

@author: abcd
"""

def drawboard(kamal):
    kamal = int(kamal)
    i = 0
    ho = " ---"
    ve = "|   "
    ho = ho * kamal
    ve = ve * (kamal+1)
    while i < kamal+1:
        print(ho)
        if not (i == kamal):
            print(ve)
        i += 1
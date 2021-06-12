#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:57:28 2019

@author: root
"""

def get_edges(pollsters_stateedge_dict,state):
    l=[]
    for i in pollsters_stateedge_dict.keys():
        if state in i:
            l.append((i,i[state]))
        else:
            l.append((i,'None'))
    return l
    


def main():
    pollsters_stateedge_dict = {
                  "Gallup": { "WA": 7, "CA": 15, "UT": -30 },
                  "SurveyUSA": { "CA": 14, "CO": 2, "CT": 13, "FL": 0 },
                  "Omniscient": { "AK": -14.0, "WA": -2.3, "CA": 20.9 }
                 }
    state=input()
    output=get_edges(pollsters_stateedge_dict,state)
    print(output)
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:42:48 2019

@author: root
"""

import datetime
import calendar
n=input()
day=datetime.datetime.strptime(n,'%m %d %Y').weekday()
print(calendar.day_name[day].upper())
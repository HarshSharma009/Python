# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:39:00 2020

@author: Harsh Sharma
"""

import covid
import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd


def show_data():
    data=covid.Covid()
    country_name=e1.get()
    status =data.get_status_by_country_name(country_name)
    active=status['active']
    e2.insert(0,active)
    death=status['deaths']
    e3.insert(0,death)
    confirm=status['confirmed']
    e4.insert(0,confirm)
    recover=status['recovered']
    e5.insert(0,recover)
    print(status)
    
    data={'id': status['id'],'Country': status['country'],
          'Active': status['active'],'Deaths' : status['deaths'], 'Recovered' : status['recovered'],
          'Latitude': status['latitude'],
          'Longitude': status['longitude'],
          'Last_updated' : status['last_update']}
    df =pd.DataFrame(data,index=[0])
    print(df)
    cadr={
        key:status[key]
        for key in status.keys() &{"confirmed","active","deaths","recovered"}}
    n=list(cadr.keys())
    v=list(cadr.values())
    plt.title("Country")
    plt.bar(range(len(cadr)),v,tick_label=n,label=('active'))
    plt.xlabel('x-label')
    plt.ylabel('data')
    plt.plot(range(len(cadr)))
    plt.show()
    
master=tk.Tk()
master.title("Covid-19 country status")
tk.Label(master,text="COVID-19 COUNTRY STATUS",padx=50).grid(row=0)
tk.Label(master,text="Enter Your Country Name: -").grid(row=2)
e1=tk.Entry(master)
e1.grid(row=2,column=3)
tk.Button(master,text='Show',command=show_data).grid(row=5,column=3,sticky=tk.W,pady=4)

tk.Label(master,text="Active Cases : -").grid(row=8)

e2=tk.Entry(master)
e2.grid(row=8,column=3)

tk.Label(master,text="Death Cases : -").grid(row=9)
e3=tk.Entry(master)
e3.grid(row=9,column=3)

tk.Label(master,text="Confirmed Cases : -").grid(row=10)
e4=tk.Entry(master)
e4.grid(row=10,column=3)

tk.Label(master,text="Recovered Cases : -").grid(row=11)
e5=tk.Entry(master)
e5.grid(row=11,column=3)
tk.Label(master,text="By Harsh Sharma").grid(row=12,column=4)

master.mainloop()
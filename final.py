#log.py
#!/usr/local/bin/python
#-*-coding: utf-8-*-
from tkinter import *
import logging
import tkinter.filedialog as fd
import pandas as pd
import numpy as np
import csv
import sys

def openScrFile():
    openFile(l1Value)

def openRsltFile():
    openFile(l2Value)

def openFile(l1Value):
    file_name = fd.askopenfilename()
    if file_name == None:
        reurn

    l1Value.set(file_name)

def sum_():
    pd.read_csv(l1Value.get())
#summ
    a= (df.groupby(['referer','ts']).sum())

    pd.DataFrame.to_csv(l2Value.get())

def min_():
    #min
    pd.read_csv(l1Value.get())
    b= (df.groupby(['referer','ts']).min())
    pd.DataFrame.to_csv(l2Value.get())

def max_():
    pd.read_csv(l1Value.get())
#max
    c= (df.groupby(['referer','ts']).max())
    pd.DataFrame.to_csv(l2Value.get())
def count_():
    pd.read_csv(l1Value.get())
#count
    d= (df.groupby(['referer','ts']).count())
    pd.DataFrame.to_csv(l2Value.get())

def mean_():
    pd.read_csv(l1Value.get())
#average
    e= (df.groupby(['referer','ts']).mean())
    pd.DataFrame.to_csv(l2Value.get())    

root = Tk()

b1 = Button(root, text="src", command=openScrFile)
b1.pack()
l1Value = StringVar()
l1 = Label(root, textvariable = l1Value)
l1.pack()

b2 = Button(root, text="rslt", command=openRsltFile)
b2.pack()
l2Value = StringVar()
l2 = Label(root, textvariable = l2Value)
l2.pack()

b3 = Button(root, text="summ", command=sum_)
b3.pack()
b4 = Button(root, text="min", command=min_)
b4.pack()

b5 = Button(root, text="max", command=max_)
b5.pack()

b6 = Button(root, text="count", command=count_)
b6.pack()

b7 = Button(root, text="average", command=mean_)
b7.pack()

root.mainloop()

    

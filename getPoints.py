# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:46:31 2024

@author: Allison
"""

import pandas as pd

def getPoints(filename):
    df = pd.read_excel(filename,index_col=0)
    df = df.set_index('Name')
    df = df.drop(columns='Initial')
    print(df)
   
    return(df)


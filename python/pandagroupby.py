# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:48:39 2018

@author: peiji
"""

import pandas as pd
import numpy as np

data = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

de = data.groupby('E')

#for p in de.groups:
#    print(p)
#    print(de.get_group(p))

for k in de.groups:
    s = ''
    dd = de.get_group(k).values
#    print(dd)
    
    for row in dd:
        s = s + str(row[3]) + ',' + str(row[2]) + ';'
    print(s)

    
    
    









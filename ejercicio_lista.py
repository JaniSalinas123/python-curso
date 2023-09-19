# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:55:39 2023

@author: Janise
"""


listaS=[]
listaotros=[]
listaR=[]
lista=["R1",
       "R2",
       "R3",
       "R4",
       "S1",
       "S2",
       "S3",
       "AP1",
       "FW1",
       "OLT1"]
for items in lista :
    if "R" in items:
        listaR.append(items)
        
    elif"S" in items:
        listaS.append(items)
        
    else:
        listaotros.append(items)
        
print(listaR,listaS,listaotros)

    

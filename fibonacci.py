# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 19:21:39 2023

@author: Janise
"""

#fibonacci 
def fibona (n):
    lista=[0,1]
    for i in range(2,n):
        calculo=lista[-1]+lista[-2]
        lista.append(calculo)
    return lista

n=5
resultado=fibona(n)
print(resultado)

    
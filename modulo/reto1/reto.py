# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 18:55:56 2023

@author: Janise
"""


def fbo(n):
    lista=[0,1]
    for i in range(2,n):
        secuencia=lista[-1]+lista[-2]
        lista.append(secuencia)
        
    return(lista)
        
n=8
resultado= fbo(n)
print(resultado)





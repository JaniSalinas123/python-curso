# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:30:25 2023

@author: Janise
"""

numero=input("ingrese el numero que debo contar: ")
numero=int(numero)
contador=1
while True:
    print(contador)
    contador+=1
    if contador <= numero:
        break
    
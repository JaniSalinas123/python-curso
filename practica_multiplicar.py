# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:43:51 2023

@author: Janise
"""

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for numero in numero:
    print(f"Tabla de multiplicar del {numero}:")

    for numeros in range(1, 16):
        resultado = numero * numeros
        print(f"{numero} x {numeros} = {resultado}")
        
        
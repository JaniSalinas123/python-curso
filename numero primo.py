# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:50:17 2023

@author: Janise
"""

n = int(input("Ingrese un número: "))

 

# Función para verificar si es primo

def es_primo(numero):

    if numero <= 1:

        return False

    for i in range(2, numero):

        if numero % i == 0:

            return False

    return True

 

# Verifica si es un número primo e imprime el resultado

if es_primo(n):

    print("Es primo")

else:

    print("No es primo")


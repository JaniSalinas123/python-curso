# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:12:45 2023

@author: Janise
"""

try:
    x=int(input("ingrese un numero: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("you cannot divide by zero")
except ValueError:
    print("ingrese  un entero: ")
except:
    print("no es posible")
print("THE END")
    
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:13:35 2023

@author: Janise
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
carrera = input("Ingrese su carrera: ")
semestre = int(input("Ingrese la cantidad de semestres que estudió: "))
edad = int(input("Ingrese su edad: "))

if edad <= 5:
    resultado = "es de primera infancia"
elif edad >= 6 and edad <= 11:
    resultado = "es de infancia"
elif edad >= 12 and edad <= 18:
    resultado = "es adolescente"
elif edad >= 19 and edad <= 26:
    resultado = "es joven"
elif edad >= 27 and edad <= 59:
    resultado = "es adulto"
else:
    resultado = "es anciano"

print(nombre + " " + apellido + " estudió " + carrera + " durante " + str(semestre) + " semestres. Como dato curioso, su familiar es considerado " + resultado)

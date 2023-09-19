# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:38:45 2023

@author: Janise
"""

datos=1
nativa=100
if datos==nativa:
    print("las variables son iguales")
else:
    print("las variables no son iguales")


acl=int(input("ingrese el vato del # de ACL: "))
if acl >1 and acl<=99:
    print("Es un ACL estandar")
elif acl >=100 and acl<=199:
    print("Es un ACL extendida")
else:
    print("no es un ACL")


edad=int(input("Ingrese "))
#!/usr/bin/env python3

"""Imprime a tabuada de 1 a 10.

---Taboada do 1---
     1 x 1 = 1
     2 x 1 = 2
     3 x 1 = 3
...
-------------------
---Taboada do 2---
     2 x 1 = 2 
     2 x 2 = 4
...

"""
__version__ = "0.1.0"
__author__  = "Emerson Rocha"


#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(numeros)

numeros = list(range(1, 11))

#Iterable(percorriveis)

#para
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada de {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2 
        print ("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)

#Ejercicio 1.1 
import unittest
from guia6 import *

def pertenece (lista: list[int], e: int) -> bool:
    return e in lista
   
    
print(pertenece ([1,2,3,4,5], 6))


def pertenece2 (lista: list[int], e: int) -> bool:
    for i in lista:
        if i == e:
            return True
    return False
     
        
    
# ejercicio 1.3

def suma_total (s: list[int]) -> int:
    suma: int = 0
    for e in s:
        suma += e
    return suma


print(suma_total([1,2,3,4,5]))
print(suma_total([]))
print(suma_total([1,2]))

def es_par(e:int) -> bool:
    par = e%2 == 0
    return par

lista = [1,2,3,4,5]
def CerosEnPosicionesPares(s: list[int]) -> None:
    indice: int = 0
    for i in range(len(s)):
        if es_par(indice):
            s[i] = 0
        indice += 1
    

print("Lista antes de la funciòn: ")
print(lista)
print(CerosEnPosicionesPares(lista))
print("Lista despuès de la funciòn: ")
print(lista)



#Ejercicio 1.1 
import unittest
from guia7 import *

def pertenece (lista: list[int], e: int) -> bool:
    return e in lista
   
    
print(pertenece ([1,2,3,4,5], 6))


def pertenece2 (lista: list[int], e: int) -> bool:
    for i in lista:
        if i == e:
            return True
    return False
     
#ejercicio 1.2

def divide_a_todos(lista: list[int], e: int) -> bool:
    divide = True
    indice = 0
    while indice < len(lista) :
        for i in range(len(lista)):
            if e % lista[i] != 0:
                divide = False
            indice +=1
        
        
    return divide

print(divide_a_todos([1,3,3,2],4))

    
# ejercicio 1.3

def suma_total (s: list[int]) -> int:
    suma: int = 0
    for e in s:
        suma += e
    return suma


print(suma_total([1,2,3,4,5]))
print(suma_total([]))
print(suma_total([1,2]))

#ejercicio 1.4

def maximo (lista:list[int]) -> int:
    max_actual: int = lista[0]
    for i in range(len(lista)):
        if max_actual <= lista[i]:
            max_actual = lista[i]
    return max_actual

print(maximo([1,2,3,4]))

#ejercicio 1.5

def minimo (lista:list[int]) -> int:
    min_actual: int = lista[0]
    for i in range(len(lista)):
        if min_actual >= lista[i]:
            min_actual = lista[i]
    return min_actual

print(minimo([3,2,3,1]))

#ejercicio 1.6

def ordenados(lista:list[int]) -> bool:
    orden = True
    indice = 0
    elemento = lista[0]
    while indice < len(lista):
        for i in range(len(lista)):
            if elemento > lista[i]:
                orden = False
            elemento = lista[i]
            indice +=1
    return orden

print(ordenados([1,2,3,-2,5]))
    

#ejercicio 1.7

def pos_maximo(lista:list[int]) -> int:
    if not lista:
        return -1
    
    pos_max: int = 0
    max_actual: int = lista[0]
    for i in range(1,len(lista)):
        if max_actual <= lista[i]:
            max_actual = lista[i]
            pos_max = i
    
    return pos_max

print(pos_maximo([1,2,8,1,2]))

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

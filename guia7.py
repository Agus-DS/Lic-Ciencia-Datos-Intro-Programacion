#Ejercicio 1.1 
import unittest
from guia7 import *

from queue import LifoQueue as Pila
import random
from queue import Queue as Cola

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

matriz = [[1,2,3],[2,3,4]]

def columna (m:list[int], c:int) -> list[int]:
    matriz_t = []
    for i in range(len(m)):
        for e in range (len(i)):
            matriz_t = matriz_t.append(e)

# ejercicio 6.4
"""def columnas_ordeandas (m:list[list[int]]) -> list[bool]:
    while indiceDeColumnaActual < len(m[0]):
        columnasOrdenadas.append(estaOrdenado(columnaDeIndice(indiceDeColumnaActual),m))
        return columnasOrdenadas
    
    def columnaDeIndice(indiceDecolumna: int, m:list[list[int]]) -> columna:
        for indiceDefila in range(len(m)):
            columnaDeseada.append(M[indiceDefila, indiceDeColumna])
        return columnaDeseada"""
    

#ejercicio 1 guia8
def generar_nros_al_azar (cantidad: int, desde:int, hasta:int) -> Pila:
    inicio = 0 
    pila = Pila()
     
    while inicio < cantidad:
        pila.put(random.randint(desde,hasta))
        inicio += 1
    return pila

     
    
miPila = (generar_nros_al_azar(4,0,10))
print (miPila.queue)

#ejercicio 3 guia 8

def buscarElMaximo(p:Pila) -> int:
    lista: list = []
    elemento: list = []

    while not p.empty():
        elemento = p.get()

        lista.append(elemento)

    for elemento in range(len(lista)-1,-1,-1):
        p.put(lista[elemento])
    
    maximo_actual:int = lista[0]

    #for i in range(1,len(lista)):
        #if lista[i] < maximo_actual:

    
    return maximo_actual 

print(buscarElMaximo(miPila))

#ejercicio 13 guia8
def armar_secuencia_bingo() -> Cola[int]:
    cola = Cola()
    indice = 0
    while indice < 100:
        cola.put(random.randint(0,99))
        indice += 1
    return cola

carton = armar_secuencia_bingo()
print(carton.queue)

def carton () -> list[int]:
    carton = []
    indice = 0
    elemento = 0
    while indice < 12:
        elemento = random.randint(0,99)
        if elemento in carton:
            carton.append(elemento)
            indice += 1
        else:
            carton.append(random.randint(0,99))
            indice += 1
    return carton
print(carton())

def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int]) -> int:
    jugada = 0
    numeroDelBolillero = 0
    while jugada <= 100:
        boli

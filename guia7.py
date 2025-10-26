#Ejercicio 1.1 

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
    if not lista:
        divide = False
        return divide 
    
    divide = True
    indice = 0
    while indice < len(lista) :
        for i in range(len(lista)):
            if   lista[i] % e != 0:
                divide = False
            indice +=1
        
        
    return divide

print(divide_a_todos([3,3,4],2))


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
    if not lista:
        max_actual = 0
        return max_actual
    
    max_actual: int = lista[0]
    
    for i in range(len(lista)):
        
        if max_actual <= lista[i]:
            max_actual = lista[i]
    return max_actual

print(maximo([1,2,4,2]))

#ejercicio 1.5

def minimo (lista:list[int]) -> int:
    if not lista:
        min_actual = 0
        return min_actual
    
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
    if not lista:
        orden = True
        return orden
    
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
        if max_actual <lista[i]:
            max_actual = lista[i]
            pos_max = i
    
    return pos_max

print(pos_maximo([9,3,8,1,9]))

#ejercicio 1.8

def pos_minimo(lista:list[int]) -> int:
    if not lista:
        return -1
    
    pos_min: int = 0
    min_actual: int = lista[0]
    for i in range(1,len(lista)):
        if min_actual >= lista[i]:
            min_actual = lista[i]
            pos_min = i
    
    return pos_min

print(pos_minimo([1,1,2,2]))



#ejercicio 1.9

def long_mayor_a_siete (lista:list[str]) -> bool:
    long_palabra = 7
    long_mayor_siete = False
    for p in lista:
        if len(p) > long_palabra:
            long_mayor_siete = True

    return long_mayor_siete

print (long_mayor_a_siete(['bue','es','esto','salud']))

#ejercicio 1.10

def reverso(palabra:str) -> str:
    reverso = palabra[::-1]
    return reverso

def es_palindroma(palabra:str)-> bool:
    palindroma = False
    if not palabra:
        palindroma = True
        return palindroma
    if palabra == reverso(palabra):
        palindroma = True
    elif len(palabra) == 1:
        palindroma = True 

    return palindroma

print(es_palindroma('bue'))

#ejercicio 1.11

def iguales_consecutivos(lista:list[int]) -> bool:
    
    contador_repetidos = 1

    if not lista:
        tres_consecutivos = False
        return tres_consecutivos
    
    tres_consecutivos = False
    numero_anterior = lista[0]
    
    for n in range(1,len(lista)):
        if lista[n] == numero_anterior:
            numero_anterior = lista[n]
            contador_repetidos += 1
            if contador_repetidos == 3:
                tres_consecutivos = True
        else:
            numero_anterior = lista[n]
            contador_repetidos = 1
    

    return tres_consecutivos

print(iguales_consecutivos([1,2,2,3,3,3]))

#ejercicio 1.12
print('ejercicio 1.12')
def hay_repetidos(lista:list[str]) -> bool:
    repetidos = False
    for i in range(len(lista)):
       if pertenece(lista[i+1::],lista[i]):
           repetidos = True
    return repetidos



def vocales_distintas(palabra:str) -> bool:
    vocales = ['a','e','i','o','u']
    vocales_palabra = []
    for i in palabra:
        if i in vocales:
            vocales_palabra.append(i)
    
    return hay_repetidos(vocales_palabra)

print(vocales_distintas('vaso'))

#ejercicio 1.13
print('#ejercicio 1.13')

def ordenados2(lista:list[str]) -> bool:
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

print(ordenados2('48'))

def pos_sec_oredenada_mas_larga(lista:list[int]) -> int:
    if not lista:
        posicion = 0
        return posicion
    
    posicion = 0
    secuencia_mas_larga = str(lista[0])
    
    for i in range(1,len(lista)):

        if ordenados2(str(lista[i])):
            if len(secuencia_mas_larga) < len(str(lista[i])):
                posicion  = i
                secuencia_mas_larga = str(lista[i])
    return posicion
        
print(pos_sec_oredenada_mas_larga([1,2,14,237]))

#ejercicio 1.14

def es_par(e:int) -> bool:
    par = e%2 == 0
    return par

def cantidad_digitos_impares(lista:list[int]) -> int:
    digitos_impares = 0

    if not lista:
        return digitos_impares
    
    for e in lista:
       for digito in str(e):
        if not es_par (int(digito)) :
           digitos_impares += 1
    
    return digitos_impares
        
print(cantidad_digitos_impares([1,4,52,33,283]))
    

#ejercicio 2.1


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

#ejercicio 2.3

def sin_vocales(palabra:str) -> str:
    vocales = ['a','e','i','o','u']
    palabra_sin_vocales = ''
    
    if palabra == '':
        return palabra_sin_vocales

    for l in palabra:
        if not l in vocales:
            palabra_sin_vocales += l

    return palabra_sin_vocales

print(sin_vocales('Hola'))

#ejercicio 2.4

def reemplaza_vocales(palabra:str) -> str:
    vocales = ['a','e','i','o','u']
    palabra_reemplazada = ''

    if palabra == '':
        return palabra_reemplazada
    else:
        for p in palabra:
            if p in vocales:
                palabra_reemplazada += '-'
            else:
                palabra_reemplazada += p
        return palabra_reemplazada
    
print(reemplaza_vocales(''))

#ejercicio 2.5

def da_vuelta_str(palabra:str) -> str:
    palabra_al_reves = ''
    if palabra == '':
        return palabra_al_reves
    else:
        for i in range(len(palabra)):
            palabra_al_reves += palabra[len(palabra)-i-1]
    
    return palabra_al_reves

print(da_vuelta_str('rosa'))

#ejercicio 2.6

def eliminar_repetidos(palabra:str) -> str:
    palabra_sin_repetidos = ''
    if palabra == '':
        return palabra_sin_repetidos
    else:
        for p in range(len(palabra)):
            if not pertenece(palabra[p+1::],palabra[p]):
                palabra_sin_repetidos += palabra[p]
        return palabra_sin_repetidos
print('#ejercicio 2.6')
print(eliminar_repetidos('masa'))

#ejercicio 3

def resultado_materia(notas:list[int]) -> int:
    promedio = 0
    suma_notas = 0
    resu = 0
    for n in notas:
        suma_notas += n
        promedio = suma_notas/len(notas)
        if n >= 4 and promedio >=7:
            resu = 1
        elif n >=4 and (promedio <7 or promedio >=4):
            resu = 2
        elif n < 4:
            resu = 3
            return resu 
        
    return resu
print(resultado_materia([4,4,4,4]))


def saldo(movimientos:list[tuple[str,int]]) -> int:
    ingresos = 0
    retiros = 0
    for movimiento in movimientos:
        if movimiento[0] == 'I':
            ingresos += movimiento[1]
        else:
             retiros +=  movimiento[1] 
    return ingresos-retiros

print(saldo([('I',2000),('R',1000),('I',500),('R',200)]))


#ejercicio 5.1

print("Ejercicio 5.1")
def pertenece_a_cada_uno_v1(lista:list[list[int]],elemento: int) -> list[bool]:
    lista_bool = []
    for l in lista:
        if pertenece(l,elemento):
            lista_bool.append(True)
        else:
            lista_bool.append(False)
    return lista_bool

print(pertenece_a_cada_uno_v1([[1,4],[2,3]],4))

#Ejercicio 6.1

def es_matriz(matriz: list[list[int]]) -> bool:
    es_matriz_bool = False
    longitud_fila = len(matriz[0])
    for i in range(len(matriz)):
        if len(matriz[i]) == longitud_fila:
            es_matriz_bool = True
        else:
            es_matriz_bool = False
    
    return es_matriz_bool

print(es_matriz([[2,3,4],[2,3,3],[2,2]]))

#Ejercicio 6.2
print("#Ejercicio 6.2")
def filas_ordenadas(matriz:list[list[int]]) -> list[bool]:
    fila_ordenada = []
    for f in matriz:
        if ordenados(f):
            fila_ordenada.append(True)
        else:
            fila_ordenada.append(False)
    
    return fila_ordenada

print(filas_ordenadas([[1,2],[4,3]]))

# ejercicio 6.3

def columna (m:list[int], c:int) -> list[int]:
    matriz_t = []
    for f in m:
        matriz_t.append(f[c])
    return matriz_t

print(columna([[1,2],[3,4]],0))
        

    
# ejercicio 6.4

print("ejercicio 6.4")
def columnas_ordeandas (matriz:list[list[int]]) -> list[bool]:
    estan_ordenadas = []

    for indiceColumna in range(len(matriz)):

        estan_ordenadas.append(ordenados(columna(matriz,indiceColumna)))

    return estan_ordenadas

print(columnas_ordeandas([[3,6,9],[4,7,8],[5,8,3]]))


#ejercicio 6.5

print("#ejercicio 6.5")

def transponer(matriz:list[list[int]]) -> list[list[int]]:
    matriz_transpuesta = []
   
    for indiceColumna in range(len(matriz)):
        matriz_transpuesta.append(columna(matriz,indiceColumna))
    
    return matriz_transpuesta

print("Matriz A:[[1,2],[3,4]] ")
print(transponer([[1,2],[3,4]]))

#ejercicio 6.6

print("#ejercicio 6.6")

def gana_vertical(tateti:list[list[str]]) -> int:
    ganaX = 1
    ganaO = 0
    empate = 2
    for i in range(len(tateti)):
        contador_elementoX = 0
        contador_elementoO = 0
        for elemento in columna(tateti,i):
            if elemento == "x":
                contador_elementoX += 1
            elif elemento == "o":
                contador_elementoO +=1
        
            if contador_elementoX == 3:
                return ganaX
            elif contador_elementoO == 3:
                return ganaO
    return empate

def gana_horizontal(tateti:list[list[str]]) -> int:
    ganaX = 1
    ganaO = 0
    empate = 2
    for fila in tateti:
        contador_elementoX = 0
        contador_elementoO = 0
        for elemento in fila:
            if elemento == "x":
                contador_elementoX += 1
            elif elemento == "o":
                contador_elementoO += 1
            if contador_elementoX== 3:
                return ganaX
            elif contador_elementoO == 3:
                return ganaO
    return empate




def gana_diagonal(tateti:list[list[str]]) -> int:
    ganaX = 1
    ganaO = 0
    empate = 2
    if tateti[0][0] == "x" and tateti[1][1] == "x" and tateti[2][2] == "x":
        return ganaX
    elif tateti[0][0] == "o" and tateti[1][1] == "o" and tateti[2][2] == "o":
        return ganaO
    elif tateti[0][2] == "x" and tateti[1][1] == "x" and tateti[2][0] == "x":
        return ganaX
    elif tateti[0][2] == "o" and tateti[1][1] == "o" and tateti[2][0] == "o":
        return ganaO
    else:
        return empate

def quien_gana_tateti(tateti:list[list[str]]) -> int:
    ganaX = 1
    ganaO = 0
    empate = 2
    gana_v = gana_vertical(tateti)
    gana_h = gana_horizontal(tateti)
    gana_d = gana_diagonal(tateti)

    if gana_v == ganaX or gana_v == ganaO:
        return gana_v
    elif gana_h == ganaX or gana_h == ganaO:
        return gana_h
    elif gana_d == ganaX or gana_d == ganaO:
        return gana_d
    else:
        return empate


print(quien_gana_tateti([["x","o",""],["x","x","o"],["x","o","o"]]))
#print(gana_horizontal([["x","x","o"],["o","x","o"],["x","o","o"]]))


#ejercicio 7.1

def lista_estudiantes() -> list[str]:
    lista_est = []
    agrego_estudiante = True
    while agrego_estudiante:
        estudiante = input('Vamos a crear una lista de estudiantes, cuando quieras terminar. Escribí listo o da enter: ')
        if estudiante == 'listo' or estudiante == '':
            agrego_estudiante = False
        else:
            lista_est.append(estudiante)
    
    return(lista_est)

print(lista_estudiantes())

#ejercicio 7.2

def calculo_el_saldo(historial:tuple[str,int]) -> int:
    saldo = 0
    for movimiento in historial:
        if movimiento[0] == "C":
            saldo += movimiento[1]
        else:
            saldo = saldo - movimiento[1]
    return saldo

def carga_la_sube_rata() -> list[tuple[str,int]]:
    historial = []
    agrego_movimientos = True
    saldo = 0
    while agrego_movimientos:
        movimiento = input('Elegí tu operación, poneiendo la letra correspondiente en mayísciñas.: \n C: Carga crédito \n D: Retirás crédito \n X: Listo! \n -->: ')
        if movimiento == "C":
            carga = int(input('Pasame el valor a cargar: '))
            historial.append(("C",carga))
        elif movimiento == "D":
            descarga = int(input("Cuánto vas a retirar?: "))
            historial.append(("D",descarga))
        elif movimiento == "X":
            agrego_movimientos = False
        else:
            print("Tenés que elegir una opción \n")
    saldo = calculo_el_saldo(historial)
    return historial


print(carga_la_sube_rata())

import random
from random import shuffle


def sumo_carta(carta:int) -> int:
    puntaje = 0
    if carta == 10 or carta == 11 or carta == 12:
        puntaje += 0.5
    else:
        puntaje += carta           
    return puntaje

def siete_y_medio() -> list[int]:
    historial_cartas = []
    cartas = [1,2,3,4,5,6,7,10,11,12]
    shuffle(cartas)
    sigo_sacando = True
    carta = 0
    puntaje = 0
    while sigo_sacando:
        eleccion = input("Escribí si 'saco'o 'me planto': ")
        if eleccion == 'saco':
           carta = cartas.pop()
           historial_cartas.append(carta)
           puntaje += sumo_carta(carta)

        elif eleccion == 'me planto' or len(cartas) == 0:
            sigo_sacando = False
    if puntaje > 7.5:
        print("Perdiste")
    else:
        print("Ganaste")
    return historial_cartas

print(siete_y_medio())

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

from queue import LifoQueue as Pila
import random
from queue import Queue as Cola
from typing import TextIO


#ejercicio 1
def generar_nros_al_azar (cantidad: int, desde:int, hasta:int) -> Pila:
    inicio = 0 
    pila = Pila()
     
    while inicio < cantidad:
        pila.put(random.randint(desde,hasta))
        inicio += 1
    return pila


print("Ejercicio 1")
miPila = (generar_nros_al_azar(4,0,10))
print (f"Veo la pila que generé{miPila.queue}")

# ejercicio 2

def cantidad_de_elementos(p:Pila) -> int:
    cantidad_elementos:int = 0
    elementos: list = []
    
    while not p.empty():
        cantidad_elementos += 1
        elementos.append(p.get())
    
    for i in range(len(elementos)-1,-1,-1):
       p.put(elementos[i])
    
    return cantidad_elementos

print("Ejercicio 2")
print(cantidad_de_elementos(miPila))
print (f"retorno la pila ya que no quiero modificar sus valores:{miPila.queue}")

# ejercicio 3
def buscarElMaximo(p:Pila) -> int:
    lista: list = []
    elemento: list = []

    while not p.empty():
        elemento = p.get()

        lista.append(elemento)

    for i in range(len(lista)-1,-1,-1):
        p.put(lista[i])
    
    maximo_actual:int = lista[0]

    for i in range(1,len(lista)):
        if lista[i] > maximo_actual:
            maximo_actual = lista[i]
        

    
    return maximo_actual 

print(f"Este es el máximo de esa pila: {buscarElMaximo(miPila)}")

#ejercicio 4
def buscar_nota_maxima(p:Pila[tuple[str,int]]) -> tuple[str,int]:
    lista_notas:list[tuple[str,int]] = []


    while not p.empty():
        lista_notas.append(p.get())
    for i in range(len(lista_notas)-1,-1,-1):
        p.put(lista_notas[i])

    nota_max: int = lista_notas[0][1]
    materia_max_actual: list[str,int] = []

    for materia in lista_notas:
        if materia[1] > nota_max:
           materia_max_actual = materia
           nota_max = materia[1]
    
    return materia_max_actual

print("ejercicio 4")

pilaNotas: Pila = Pila()
pilaNotas.put(("Analisis",8))
pilaNotas.put(("IP-AED1",10))
pilaNotas.put(("Algebra",7))
print(f"mi pila antes de la función: {pilaNotas.queue}")
print(f"Esta es la materia con la nota más alta: {buscar_nota_maxima(pilaNotas)}")
print(f"mi pila después de la función:{pilaNotas.queue} ")

#Ejercicio 5

def esta_bien_balanceada(formula:str) -> bool:
    pilaConParentesis:list[str] = Pila()
    for elemento in formula:
        if elemento == "(" or elemento == ")":
            pilaConParentesis.put(elemento)
        
    cantParentesisCierre: int = 0
    cantParentesisApertura: int = 0 
    bienBalanceada = True
    ultimoElemento: str = ""

    while not pilaConParentesis.empty():
        ultimoElemento = pilaConParentesis.get()

        if ultimoElemento == ")":
            cantParentesisCierre += 1
        else:
            cantParentesisApertura +=1

        if cantParentesisCierre < cantParentesisApertura:
            bienBalanceada = False
            return bienBalanceada
    if cantParentesisCierre != cantParentesisApertura:
        bienBalanceada = False

    return bienBalanceada
        
        
print("Ejercicio 5")
print(esta_bien_balanceada("10 * (1 + (2*(-1)))"))
            
    
        
# ejercicio 6
print("Ejercicio 6")
def hagoOperacion(num1: float, num2: float, operador:str) -> float:
    resultado: float = 0
    for elemento in operador:
        if elemento == "+":
           resultado = num1 + num2
        elif elemento == "-":
            resultado = num1 - num2
        elif elemento == "*":
            resultado = num1 * num2
        elif elemento == "/":
            resultado = num1/num2
    return resultado

def split2(texto:str) -> list[str]:
    numero:str = ""
    lista: list[str] = []
    for elemento in texto:
        if elemento == " ":
            lista.append(numero)
            numero = ""
        else:
            numero += elemento
    lista.append(numero)
    return lista

print(split2("2 4 + 10 - 2 -"))

def evaluar_post_fix(operaciones: str) -> float:
    pilaConOperandos: Pila = Pila()
    operadores: list[str] = ["+","*","-","/"]
    resultado: float = 0
    operando1 : int = 0
    operador: str = ""
    listado: list[str] = split2(operaciones)

    for elemento in listado:
        if elemento not in operadores:
            pilaConOperandos.put(elemento)
        elif elemento in operadores:
            operador = elemento
            operando1 = int(pilaConOperandos.get())
            operando2 = int(pilaConOperandos.get())
            resultado = hagoOperacion(operando2,operando1,operador)
            pilaConOperandos.put(resultado)

    return resultado

print(evaluar_post_fix("3 4 + 5 * 2 -"))
    
"""#ejercicio 13 guia8
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
        boli"""



def promedio_por_estudiante(notas:list[tuple[str,float]]) -> dict[str,float]:
    promedio_estudiantes : dict[str,float] = dict()
    for nombre in estudiantes(notas):
        promedio_estudiantes[nombre] = promedio_del_estudiante(nombre,notas)
        return promedio_estudiantes

def promedio_del_estudiante(nombre_estudiante: str,notas: list[tuple[str,float]]) -> float:
    suma_notas: float = 0
    cant_notas: int = 0

    for (nombre,nota) in notas:
        if nombre == nombre_estudiante:
            suma_notas += nota
            cant_notas += 1
        
    return suma_notas/cant_notas
    
def estudiantes(notas:list[tuple[str,float]]) -> list[str]:
    estudiantes: dict[str,int] = dict()
    for (nombre,_) in notas:
        estudiantes[nombre] = 0
    return list(estudiantes.keys())

print(promedio_por_estudiante([("Sole",9.5),("Maxi",8.0),("Sole",9.0)])["Sole"])


#ejercicio 19.1


def contar_lineas(nombre_archivo:str) -> int:
    archivo: TextIO = open(nombre_archivo,"r+")
    lineas = archivo.readlines()
    archivo.close()
    return len(lineas)

def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    archivo_entrada: TextIO = open(nombre_archivo_entrada,"r")
    lineas_archivo_entrada = archivo_entrada.readlines()
    archivo_entrada.close()

    lineas_no_comentario = []
    for linea in lineas_archivo_entrada:
        if not es_comentario(linea):
            lineas_no_comentario.append(linea)
    
    archivo_salida = open(nombre_archivo_salida,"w")
    archivo_salida.write(lineas_no_comentario)
    archivo_salida.close()

def es_comentario(lineas:str)  -> bool:
    i = 0
    es_comentario = True
    
    while i 

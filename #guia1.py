#guia1

print("Ejercicio 1-1\n")
# Ejercicio 1

def imprimir_hola_mundo () -> str:
    return print("¡Hola mundo!")

imprimir_hola_mundo()

print("\nEjercicio1-2\n")
# 2
def imprimir_un_verso() -> str:
    return print("Hoy asume lo que venga\nSea para bien o todo mal\nY aunque pierda todo lo que tenga\nSe va a morder para aguantar.")

imprimir_un_verso()

print("\nEjercicio1-3\n")
#3
import math
def raizDe2 () -> float: 
    return print(round(math.sqrt(2),4))

raizDe2()

print("\nEjercicio1-4\n")

# 4
def factorial_de_dos() -> int:
    return print(2*1)

factorial_de_dos()

print("\nEjercicio1-5\n")

# 5

def perimetro () -> float:
    return print((2*math.pi))

perimetro()

print("\nEjercicio 2-1\n")

#Ejercicio 2
def imprimir_saludo (nombre: str) -> str:
    print ("Hola " + nombre)

imprimir_saludo('Agustin')

print("\nEjercicio 2-2\n")

def fahrenheit_a_celsius (t: float) -> float:
    res = ((t-32)*5)/9
    return res

print(fahrenheit_a_celsius (4))

print("\nEjercicio 2-3\n")

def imprimir_dos_veces(est: str) -> str:
    ref = est+est
    return ref

print(imprimir_dos_veces("Te cantaron pajaritos en el aire! \n"))

def es_multiplo_de (n:int, m: int) -> bool:
    multiplo = n%m == 0
    return multiplo

print(es_multiplo_de(7,2))

print("\nEjercicio 2-4\n")

def es_par(n:int) -> bool:
    num = es_multiplo_de(n,2)
    return num
print(es_par(9))

print("\nEjercicio 2-5\n")

def cantidad_de_pizzas(n:int,min_porciones:int) -> int:
    porciones = n * min_porciones
    pizzas = round(porciones / 8,0)
    return pizzas

print(cantidad_de_pizzas(10,4))
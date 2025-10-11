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
    return print(pizzas)

cantidad_de_pizzas(10,4)

print("\nEjercicio 3-1\n")

def alguno_es_cero (n:float,m:float) -> bool:
    res = n == 0 or m == 0
    return print(res)

alguno_es_cero(0/2,3/4)

print("\nEjercicio 3-2\n")

def ambos_son_cero (n:float,m:float) -> bool:
    res = n == 0 and m == 0
    return print(res)

ambos_son_cero(1/3,0/3)

print("\nEjercicio 3-3\n")

def es_nombre_largo (nombre: str) -> bool:
    res = len(nombre) >= 3 and  len(nombre) <= 8
    return print(res) 

es_nombre_largo("sarasassa")

print("\nEjercicio 3-4\n")

def es_bisiesto(año:int) -> bool:
    res = es_multiplo_de(año,400) or (es_multiplo_de(año,4) and (not es_multiplo_de(año,100)))
    return print(res)

es_bisiesto(2000)

print("\nEjercicio 4\n")

def peso_pino(altura: int) -> int:
    paso_a_cm = altura*100
    res = paso_a_cm * 3 + max((paso_a_cm - 300) *2,0)
    return res

print(peso_pino(2))

def es_peso_util(peso:int) -> bool:
    res = (peso >= 400) and (peso <= 1000)
    return(res)

es_peso_util(1001)

def sirve_pino(altura: int) -> bool:
    peso = peso_pino(altura)
    print("El peso en kg es:" + str(peso))
    sirve = es_peso_util(peso)
    return sirve


print(sirve_pino(5))

print("\nEjercicio 5-1\n")

def devolver_doble_si_es_par(numero: int) -> int:
    if es_par(numero):
        return numero * 2
    else : return numero

print(devolver_doble_si_es_par(9))

print("\nEjercicio 5-2\n")

def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if es_par(numero):
        return numero
    else : return numero +1

print(devolver_valor_si_es_par_sino_el_que_sigue(3))

print("\nEjercicio 5-3\n")

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if es_multiplo_de(numero,3):
        return numero*2
    elif  es_multiplo_de(numero,9):
        return numero*3
    else : return numero

print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(12))

print("\nEjercicio 5-4\n")

def lindo_nombre(nombre: str) -> str:
    if len(nombre) >=5:
        return ('Tu nombre tiene muchas letras')
    else: return ('Tu nombre tiene menos de 5 caracteres')

print(lindo_nombre('Juan'))

print("\nEjercicio 5-5\n")

def elRango(numero: int) -> str:
    if numero < 5:
        return ('Menor a 5')
    elif numero >= 10 and numero <= 20:
        return('Entre 10 y 20')
    elif numero >= 20:
        return ('Mayor a 20')
    else: return ('Rango no definido')

print(elRango(-1))

print("\nEjercicio 5-6\n")

def la_pala(sexo: str, edad: int) -> str:
    if sexo == 'M' and edad >= 65 or edad < 18:
        return 'Anda de vacaciones!'
    elif sexo == 'F' and edad >= 60 or edad < 18:
        return 'Anda de vacaciones!'
    else: return 'Te toca trabajar'

print(la_pala('M',25))

print("\nEjercicio 6-1\n")

def imprime_del_1_al_10() -> int:
    n = 0
    while n>= 0 and n <10:
         n += 1
         print(n)
   

##imprime_del_1_al_10()

print("\nEjercicio 6-2\n")

def imprime_pares_del_10_al_40() -> int:
    n = 10
    while n>= 10 and n <40:
         n += 2
         print(n)

imprime_pares_del_10_al_40()

print("\nEjercicio 6-3\n")

def imprime_eco_10_veces() -> str:
    n = 0 
    while n>= 0 and n<10:
        n += 1
        print('eco')

imprime_eco_10_veces()

print("\nEjercicio 6-4\n")

def conteo_despegue(n:int) -> str:
    while n>= 1:
        print (n)
        n -=1
    
    print('Despegue!')

conteo_despegue(10)

print("\nEjercicio 6-5\n")

def viaje_en_el_tiempo(start_year: int, end_year:int) -> str:
    while start_year > end_year:
        start_year -= 1
        print('Viajó un año al pasado, estamos en el año: ' + str(start_year))
        

viaje_en_el_tiempo(2025,2020)

print("\nEjercicio 6-6\n")

def viaje_en_el_tiempo2(start_year: int, end_year:int) -> str:
    while start_year > end_year:
        print('Viajamos 20 años en el pasado, estamos en el año: ' + str(start_year))
        start_year -= 20
        
        

viaje_en_el_tiempo2(2025,-384)

print("\nEjercicio 7-1\n")

def imprime_del_1_al_10_v2() -> int:
    for n in range (1,11,1):
         print(n)
    
imprime_del_1_al_10_v2()

print("\nEjercicio 7-2\n")

def imprime_pares_del_10_al_40_v2() -> int:
    for n in range(10,41,2):
        print (n)

imprime_pares_del_10_al_40_v2()


print("\nEjercicio 7-3\n")

def imprime_eco_10_veces_v2() -> str:
    for n in range(1,11,1):
        print ('eco')
    
imprime_eco_10_veces_v2()

print("\nEjercicio 7-4\n")

def conteo_despegue_v2(n:int) -> str:
    for n in range(n,0,-1):
        print(n)
    print('Despegue!')

conteo_despegue(10)

print("\nEjercicio 7-5\n")

def viaje_en_el_tiempo_v2(start_year: int, end_year:int) -> str:
   for start_year in range(start_year,end_year-1,-1):
        print('Viajó un año al pasado, estamos en el año: ' + str(start_year))
        

viaje_en_el_tiempo_v2(2025,2020)

print("\nEjercicio 7-6\n")

def viaje_en_el_tiempo2_v2(start_year: int, end_year:int) -> str:
    for start_year in range(start_year,end_year,-20):
        print('Viajamos 20 años en el pasado, estamos en el año: ' + str(start_year))
        

viaje_en_el_tiempo2_v2(2025,-384)



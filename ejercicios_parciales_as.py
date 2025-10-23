# Ejercicios de parcial

def uno_si_cero_no(condicion:bool) -> int:
    return 1 if condicion else 0

def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
    cantidad_camas = len(camas_por_piso[0])
    cantidad_camas_libres = 0
    cantidad_camas_ocupadas = 0
    lista_camas = []

    for piso in range(len(camas_por_piso)):
        for cama_libre in camas_por_piso[piso]:
            cantidad_camas_libres += uno_si_cero_no(cama_libre)
        
        lista_camas.append(round(cantidad_camas_libres/cantidad_camas,1))
        cantidad_camas_libres = 0
        

    return lista_camas

print(nivel_de_ocupacion([[False,False,False],[False,False,True],[True,True,True]]))

A = [[1,2],[3,4]]

"""def cambiar_matriz(A:list[list[int]]) -> None: 
    if (len(A) == 1):
        meclarLosElementos(A):
    else:
        MezclarLasFilas(A)

def MezclarLosElementos(A):
    "Desplaza los elementos de A a una posicion a la izquierda"

def MezclarLasFilas(A):
    "Desplaza las filas de A a una posicion arriba""
"""
def cantidadJugadasyPromedioPersona(jugadas:list[int]) -> tuple[int,float]:

    suma_intentos = 0
    intentos_validos = 0
    
    
    for i in range(len(jugadas)):
        if jugadas[i] > 0 and jugadas[i] < 61:
            intentos_validos += 1
            suma_intentos += jugadas[i]

    return (intentos_validos,suma_intentos/intentos_validos)

print(cantidadJugadasyPromedioPersona([61,60,59,58]))

def promedioSalidas(registro:dict[str,list[int]]) -> dict[str,tuple[int,float]]:
    lista_nombres = list(registro.keys())
    diccionario_promedios = dict()

    for nombre in lista_nombres:
        for jugadas in registro:
            diccionario_promedios[nombre] = cantidadJugadasyPromedioPersona(jugadas)
        
    
    return diccionario_promedios
            

print(promedioSalidas({'a':[61,60,59,58],'b':[1,2,3,0]}))


        




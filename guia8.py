#ejercicio 3.16
from typing import TextIO


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

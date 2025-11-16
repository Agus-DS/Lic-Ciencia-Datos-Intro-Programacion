# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def ultima_aparicion(s:list[int], e: int) -> int:
    ultima_posición:int = 0
    for i in range(len(s)):
         if s[i] == e:
             ultima_posición = i
             
    return ultima_posición

print(ultima_aparicion([-1,4,0,4,100,0,100,0,-1,-1],0))

def fila_capicua(fila:list[int]) -> bool:
    fila_alvere:list[int] = []
    for i in range(len(fila)-1,-1,-1):
        fila_alvere.append(fila[i])
    
    return fila == fila_alvere
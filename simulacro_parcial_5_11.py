from queue import Queue as Cola
# Ejercicio 1

def acorto_lista(lista: list[int] , arranco_desde:int) -> list[int]:
    lista_acortada:list[int] = []
    arranco_desde += 1
    for i in range((arranco_desde), len(lista)):
        lista_acortada.append(lista[i])
    
    return lista_acortada

def primer_numero_suma_n_veces(numero:int, lista_acortada:list[int], n:int) -> int:
    parejas_que_suman:int = 0
    numero_a_sumar:int = numero
    i: int = 0
    while i < len(lista_acortada):
        if numero_a_sumar + lista_acortada[i] == n:
            parejas_que_suman +=1 
        i +=1

    return parejas_que_suman


def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    parejas_que_suman:int = 0
    pareja_que_suman_parcial:int = 0
    i: int = 0

    while i < len(s): 
      pareja_que_suman_parcial = primer_numero_suma_n_veces(s[i],acorto_lista(s,i),n) 
      parejas_que_suman += pareja_que_suman_parcial
      i += 1
    
    return parejas_que_suman


print(cantidad_parejas_que_suman([1,3,2,5,4,8] , 5))
 
# Ejercicio 2 


def pasar_por_autoservicio(clientes: Cola[tuple[str, str, int]]) -> str:
    cliente_parcial:tuple[str,str,int] = ()
    cliente_que_pasa:str = ""
    cantidad_clientes:int = len(clientes.queue)
    for cliente in range(cantidad_clientes):
        cliente_parcial = clientes.get()
        if cliente_parcial[1] != 'efectivo' and cliente_parcial[2] <= 15 and cliente_que_pasa == "":
            cliente_que_pasa += cliente_parcial[0]
        else:
            clientes.put(cliente_parcial)

    return cliente_que_pasa

clientes: Cola[tuple[str,str,int]] = Cola()
clientes.put(("Ana","efectivo",13))
clientes.put(("Juan","efectivo",22))
clientes.put(("Bruno","efectivo",14))
clientes.put(("Agustín","transferencia",5))
print(f"Cola auto servicio antes de la función: {clientes.queue}")
print(pasar_por_autoservicio(clientes))
print(print(f"Cola auto servicio después de la función: {clientes.queue}"))

# Ejercicio 3 
matriz: list[list[int]] = [[1,2,3],[40,50,60],[-7,-8,-9]]
matriz2:list[list[int]] = [[1,2,3], [4,5,6] , [7,8,9], [10,11,12]]
def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int) -> None:
    fila:int = 0
    cantidad_filas_de_A: int = len(A)
    A2:list[list[int]] = []
    valor_parcial_col2_de_A: int = 0
    valor_parcial_col1_de_A: int = 0
    for fila in A:
        A2 += [fila.copy()]
    
    for fila in range(len(A)):
        valor_parcial_col2_de_A = A[cantidad_filas_de_A-1-fila][col2]
        valor_parcial_col1_de_A = A[cantidad_filas_de_A-1-fila][col1]
        A2[fila][col1] = valor_parcial_col2_de_A
        A2[fila][col2] = valor_parcial_col1_de_A
    
    fila = 0
    columna: int = 0
    for fila in range(len(A)):
        for columna in range(len(A[fila])):
            A[fila][columna] = A2[fila][columna]

   
    
    
print(f"Matriz antes de la fucnión {matriz2}")
print(intercambiar_e_invertir_columnas(matriz2,1,2))
print(f"Matriz despues de la fucnión {matriz2}")
print(f"Matriz antes de la fucnión {matriz}")
print(intercambiar_e_invertir_columnas(matriz,1,2))
print(f"Matriz despues de la fucnión {matriz}")

# Ejercicio 4
def mantuvieron_residencia(censo1: dict[str, str], censo2: dict[str, str]) -> dict[str, int]:
    lista_con_nombres:list[str] = list(censo1.keys())
    residencia: dict[str,int] = {}
    
    for nombre in lista_con_nombres:
        
        if censo1[nombre] == censo2[nombre]:
            
            if censo1[nombre] in residencia:
                residencia[censo1[nombre]] = residencia[censo1[nombre]] +1
            
            else:
                
                residencia[censo1[nombre]] = 1

        
    
    return residencia

print(mantuvieron_residencia({'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}, 
                  {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}))


def sumar_elementos(s: list[int]) -> int:
   res: int = 0
   for i in range(1, len(s)):
        res += s[i]
   return res

print(sumar_elementos([4,2,3]))
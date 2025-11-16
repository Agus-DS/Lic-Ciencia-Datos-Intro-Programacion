import unittest
from queue import Queue as Cola
from simulacro_parcial_5_11 import *

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej1Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        self.method = cantidad_parejas_que_suman

    def test_lista_vacia_devuelve_cero(self):
        entrada: list[int] = []
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 0)
        self.assertEqual(res, 0)
        self.assertEqual(entrada, entrada_copia)

    def test_un_elemento_no_puede_formar_pareja(self):
        entrada: list[int] = [1]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 1)
        self.assertEqual(res, 0)
        self.assertEqual(entrada, entrada_copia)

    def test_parejas_repetidas_cuenta_todas(self):
        entrada: list[int] = [2, 2, 2, 2, 2]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 4)
        self.assertEqual(res, 10)
        self.assertEqual(entrada, entrada_copia)

    def test_no_hay_parejas_con_si_mismo(self):
        entrada: list[int] = [2, 1]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 4)
        self.assertEqual(res, 0)
        self.assertEqual(entrada, entrada_copia)

    def test_parejas_suman_valores_varios(self):
        entrada: list[int] = [1, 3, 2, 5, 4, 8]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 5)
        self.assertEqual(res, 2)
        self.assertEqual(entrada, entrada_copia)

    def test_parejas_con_numeros_negativos(self):
        entrada: list[int] = [-1, 6, -2, 3, 7, -3]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 5)
        self.assertEqual(res, 2)
        self.assertEqual(entrada, entrada_copia)
    
    def test_todos_negativos(self):
        entrada: list[int] = [-1, -2, -3, -4, -5, -6]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, -5)
        self.assertEqual(res, 2)
        self.assertEqual(entrada, entrada_copia)
    
    def test_todos_forman_pareja(self):
        entrada: list[int] = [1, 3, 4, 5, 6, 2]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 7)
        self.assertEqual(res, 3)
        self.assertEqual(entrada, entrada_copia)
    
    def test_suman_cero(self):
        entrada: list[int] = [1, 3, -1, 5, -6, 6]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 0)
        self.assertEqual(res, 2)
        self.assertEqual(entrada, entrada_copia)
    
    def test_no_hay_parejas(self):
        entrada: list[int] = [1, 2, 3, 4, 5, 6]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 12)
        self.assertEqual(res, 0)
        self.assertEqual(entrada, entrada_copia)



'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej2Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej2Test, self).__init__(*args, **kwargs)
        self.method = pasar_por_autoservicio
    
    def test_unico_cliente_se_retira(self):
        clientes = crear_cola([("Pedro", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Pedro")
    
    def test_unico_cliente_se_retira_y_cola_queda_vacia(self):
        clientes = crear_cola([("Juana", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Juana")

        self.assertTrue(clientes.empty())
    
    def test_cliente_al_final_de_la_cola_se_retira(self):
        clientes = crear_cola([("Ana", "efectivo", 13), ("Juan", "qr", 22), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Bruno")
    
    def test_cliente_al_inicio_de_la_cola_se_retira(self):
        clientes = crear_cola([("Jessica", "tarjeta", 14), ("Ana", "efectivo", 13), ("Juan", "qr", 22)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Jessica")
    
    def test_cliente_al_medio_de_la_cola_se_retira(self):
        clientes = crear_cola([("Juan", "qr", 22), ("Jorge", "tarjeta", 14), ("Ana", "efectivo", 13)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Jorge")
    
    def test_cliente_al_medio_de_la_cola_se_retira_y_el_resto_quedan(self):
        clientes = crear_cola([("Juan", "tarjeta", 22), ("Silvia", "qr", 14), ("Ana", "efectivo", 13)])
        clientes_final = crear_cola([("Juan", "tarjeta", 22), ("Ana", "efectivo", 13)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Silvia")
        self.assertEqual(clientes.queue, clientes_final.queue)

    def test_selecciona_al_primer_cliente_con_varios_candidatos(self):
        clientes = crear_cola([("Juan", "qr", 22), ("Mercedes", "qr", 8), ("Pedro", "transferencia", 12), ("Ana", "efectivo", 13), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Mercedes")

    def test_selecciona_al_primer_cliente_con_varios_candidatos_y_el_resto_quedan(self):
        clientes = crear_cola([("Juan", "qr", 22), ("Mercedes", "qr", 8), ("Pedro", "transferencia", 12), ("Ana", "efectivo", 13), ("Bruno", "tarjeta", 14)])
        clientes_final = crear_cola([("Juan", "qr", 22), ("Pedro", "transferencia", 12), ("Ana", "efectivo", 13), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Mercedes")
        self.assertEqual(clientes.queue, clientes_final.queue)

    def test_selecciona_al_primer_cliente_con_todos_candidatos(self):
        clientes = crear_cola([("Marcelo", "qr", 8), ("Pedro", "transferencia", 12), ("Ana", "qr", 13), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Marcelo")

    def test_selecciona_al_primer_cliente_con_todos_candidatos_y_el_resto_quedan(self):
        clientes = crear_cola([("Marcelo", "qr", 8), ("Pedro", "transferencia", 12), ("Ana", "qr", 13), ("Bruno", "tarjeta", 14)])
        clientes_final = crear_cola([("Pedro", "transferencia", 12), ("Ana", "qr", 13), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Marcelo")
        self.assertEqual(clientes.queue, clientes_final.queue)

def crear_cola(elementos):
    cola = Cola()
    for elem in elementos:
        cola.put(elem)
    return cola

class Ej3Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej3Test, self).__init__(*args, **kwargs)
        self.method = intercambiar_e_invertir_columnas
    
    def test_intercambiar_e_invertir_columnas_en_matriz_1x2(self):
        matriz = [
            [10, 20]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [20, 10]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_en_matriz_2x2(self):
        matriz = [
            [1, 2],
            [3, 4]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [4, 3],
            [2, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_en_matriz_3x3(self):
        matriz = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 2)
        matriz_esperada = [
            [9, 2, 7],
            [6, 5, 4],
            [3, 8, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)

    def test_intercambiar_e_invertir_columnas_3x2(self):
        matriz = [
            [1, 2],
            [4, 5],
            [7, 8]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [8, 7],
            [5, 4],
            [2, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)

    def test_intercambiar_e_invertir_columnas_2x3(self):
        matriz = [
            [1, 2, 6],
            [4, 5, 4]
        ]
        intercambiar_e_invertir_columnas(matriz, 1, 2)
        matriz_esperada = [
            [1, 4, 5],
            [4, 6, 2],
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_iguales(self):
        matriz = [
            [1, 2, 1],
            [4, 5, 4],
            [7, 8, 7]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 2)
        matriz_esperada = [
            [7, 2, 7],
            [4, 5, 4],
            [1, 8, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_con_ceros(self):
        matriz = [
            [1, 0, 3],
            [4, 0, 6],
            [7, 0, 9]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [0, 7, 3],
            [0, 4, 6],
            [0, 1, 9]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_con_negativos(self):
        matriz = [
            [1, -2, 3],
            [-4, 5, -6],
            [-7, -8, 9]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 2)
        matriz_esperada = [
            [9, -2, -7],
            [-6, 5, -4],
            [3, -8, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_en_matriz_3x10(self):
        matriz = [
            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
        ]
        intercambiar_e_invertir_columnas(matriz, 5, 8)
        matriz_esperada = [
            [11, 12, 13, 14, 15, 39, 17, 18, 36, 20],
            [21, 22, 23, 24, 25, 29, 27, 28, 26, 30],
            [31, 32, 33, 34, 35, 19, 37, 38, 16, 40]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_en_matriz_8x3(self):
        matriz = [
            [11, 12, 13],
            [21, 22, 23],
            [31, 32, 33],
            [41, 42, 43],
            [51, 52, 53],
            [61, 62, 63],
            [71, 72, 73],
            [81, 82, 83],
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [82, 81, 13],
            [72, 71, 23],
            [62, 61, 33],
            [52, 51, 43],
            [42, 41, 53],
            [32, 31, 63],
            [22, 21, 73],
            [12, 11, 83],
        ]
        self.assertEqual(matriz, matriz_esperada)

class Ej4Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej4Test, self).__init__(*args, **kwargs)
        self.method = mantuvieron_residencia

    def test_sin_habitantes(self):
        censo1 = {}
        censo2 = {}
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_una_sola_persona_mantiene(self):
        censo1 = {'Juan': 'Merlo'}
        censo2 = {'Juan': 'Merlo'}
        esperado = {'Merlo': 1}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_una_sola_persona_se_muda(self):
        censo1 = {'Juan': 'Merlo'}
        censo2 = {'Juan': 'Castelar'}
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_sin_residencia_mantenida(self):
        censo1 = {'Armando': 'San Miguel',
                  'Julieta': 'Ezeiza'}
        censo2 = {'Armando': 'La Matanza',
                  'Julieta': 'Zarate'}
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)
        
    def test_residencia_mantenida_en_una_localidad(self):
        censo1 = {'Juan': 'Merlo', 'Ana': 'Merlo'}
        censo2 = {'Juan': 'Castelar', 'Ana': 'Merlo'}
        esperado = {'Merlo': 1}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_residencia_mantenida_en_varias_localidades(self):
        censo1 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo2 = {'Carolina': 'Florencio Varela',
                  'Ignacio': 'Ciudad Autónoma de Buenos Aires',
                  'Malena': 'Berazategui',
                  'Oriana': 'Ciudad Autónoma de Buenos Aires',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'Quilmes',
                  'Maria': 'Quilmes'}
        
        esperado = {'Florencio Varela': 1, 'Quilmes': 2}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_todos_mantienen_residencia(self):
        censo1 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo2 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Oriana': 'San Miguel',
                  'Malena': 'Avellaneda',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Maria': 'Quilmes'}
        
        esperado = {'Florencio Varela': 1, 'Quilmes': 3, 'La Plata': 1, 'Avellaneda': 1, 'San Miguel': 1}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_todos_se_mudan(self):
        censo1 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo2 = {'Carolina': 'Ezeiza',
                  'Tony': 'Avellaneda',
                  'Oriana': 'Quilmes',
                  'Malena': 'La Plata',
                  'Gonzalo': 'San Isidro',
                  'Ignacio': 'Florencio Varela',
                  'Maria': 'Berazategui'}
        
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_residencias_cruzadas_no_mantenidas(self):
        censo1 = {'Armando': 'San Miguel',
                  'Julieta': 'Ezeiza'}
        censo2 = {'Armando': 'Ezeiza',
                  'Julieta': 'San Miguel'}
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_no_modifica_inputs(self):
        censo1 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo1_copia = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo2 = {'Carolina': 'Florencio Varela',
                  'Ignacio': 'Ciudad Autónoma de Buenos Aires',
                  'Malena': 'Berazategui',
                  'Oriana': 'Ciudad Autónoma de Buenos Aires',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'Quilmes',
                  'Maria': 'Quilmes'}
        
        censo2_copia = {'Carolina': 'Florencio Varela',
                  'Ignacio': 'Ciudad Autónoma de Buenos Aires',
                  'Malena': 'Berazategui',
                  'Oriana': 'Ciudad Autónoma de Buenos Aires',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'Quilmes',
                  'Maria': 'Quilmes'}
        
        esperado = {'Florencio Varela': 1, 'Quilmes': 2}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)
        self.assertEqual(censo1, censo1_copia)
        self.assertEqual(censo2, censo2_copia)
  
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
import unittest
from guia7 import *


class Test_suma_total (unittest.TestCase):
    def test_lista_vacia(self):
        s = []
        self.assertEqual(suma_total(s),0)

    def test_lista_con_solo_elemento(self):
        s = [2]
        self.assertEqual(suma_total(s),2)

    def test_lista_con_muchos_elementos(self):
        s = [1,2,3,4]
        self.assertEqual(suma_total(s),10)

    def test_lista_con_negativos(self):
        s = [1,-1,2,-2]
        self.assertEqual(suma_total(s),0)


class Test_divide_todos (unittest.TestCase):
    def test_solo_divide_primero(self):
        s = [4,3,3,5]
        self.assertFalse(divide_a_todos(s,4),False)

    def test_lista_vacia(self):
        s = []
        self.assertFalse(divide_a_todos(s,1),False)

    def test_solo_divide_ultimo(self):
        s = [3,3,3,4]
        self.assertFalse(divide_a_todos(s,2),False)

    def test_lista_con_elementos(self):
        s = [2,4,6,10]
        self.assertTrue(divide_a_todos(s,2),True)

class Test_maximo (unittest.TestCase):
    def test_lista_vacia(self):
        s = []
        self.assertEqual(maximo(s),0)

    def test_negativos(self):
        s = [1,-3,2]
        self.assertEqual(maximo(s),2)

class Test_ordenados(unittest.TestCase):
    def test_lista_vacia(self):
        s = []
        self.assertTrue(ordenados(s),True)

    def test_lista_negativos_en_desorden(self):
        s = [1,-3,2]
        self.assertFalse(ordenados(s),False)
    
    def test_lista_negativos_en_orden(self):
        s = [-3,1,2]
        self.assertTrue(ordenados(s),True)

    def test_lista_positivos_en_orden(self):
        s = [1,2,3,5]
        self.assertTrue(ordenados(s),True)

class Test_pos_max(unittest.TestCase):
    def test_lista_vacia(self):
        s = []
        self.assertEqual(pos_maximo(s),-1)

    def test_varios_max(self):
        s = [1,2,5,5]
        self.assertEqual(pos_maximo(s),2)
    
    def test_un_solo_valor(self):
        s = [3]
        self.assertEqual(pos_maximo(s),0)

class Test_pos_min (unittest.TestCase):
    def test_lista_vacia(self):
        s = []
        self.assertEqual(pos_minimo(s),-1)
    
    def test_varios_min(self):
        s = [1,1,2,3]
        self.assertEqual(pos_minimo(s),1)

class test_long_mayor_siete(unittest.TestCase):
    def test_lista_vacia(self):
        s = []
        self.assertFalse(long_mayor_a_siete(s),False)
    
    def test_sin_palabras_mayor_siete(self):
        s = ['sol','vino','palta']
        self.assertFalse(long_mayor_a_siete(s),False)
    
    def test_con_palabras_mayor_siete(self):
        s = ['es','bue','estomago']
        self.assertTrue(long_mayor_a_siete(s),True)    
    
class test_es_palindroma(unittest.TestCase):
    def test_vacio(self):
        s = ''
        self.assertTrue(es_palindroma(s),True)
    
    def test_una_sola_letra(self):
        s = 's'
        self.assertTrue(es_palindroma(s),True)
    
    def test_palabra_no_palindroma(self):
        s = 'bola'
        self.assertFalse(es_palindroma(s),False)

    def test_palabra_palindroma(self):
        s = 'ana'
        self.assertTrue(es_palindroma(s),True)

class test_iguales_consecutivos(unittest.TestCase):
    def test_vacio(self):
        s = []
        self.assertFalse(iguales_consecutivos(s),False)
    
    def test_tres_consecutivos_al_principio(self):
        s = [1,1,1,2,3]
        self.assertTrue(iguales_consecutivos(s),True)
    
    def test_tres_consecutivos_con_uno_distinto_al_final(self):
        s = [1,2,3,3,3,5]
        self.assertTrue(iguales_consecutivos(s),True)

class test_pos_sec_mas_larga(unittest.TestCase):
    def test_lista_vacia(self):
        s = []
        self.assertEqual(pos_sec_oredenada_mas_larga(s),0)
    
    def test_pos_elemento_largo_no_ordenado(self):
        s = [1,2,48,273]
        self.assertEqual(pos_sec_oredenada_mas_larga(s),2)
    
    def test_pos_elemento_largo_ordenado(self):
        s = [1,2,48,237,34]
        self.assertEqual(pos_sec_oredenada_mas_larga(s),3)

class test_cantidad_digitos_impares(unittest.TestCase):
    def test_lista_vacia(self):
        s = []
        self.assertEqual(cantidad_digitos_impares(s),0)
    
    def test_lista_con_4_digitos_impares(self):
        s = [1,4,52,33,282]
        self.assertEqual(cantidad_digitos_impares(s),4)
    
    def test_lista_con_digitos_pares(self):
        s = [2,4,6,82,846]
        self.assertEqual(cantidad_digitos_impares(s),0)
    
class test_sin_vocales(unittest.TestCase):
    def test_palabra_vacia(self):
        s = ''
        self.assertEqual(sin_vocales(s),'')
    
    def test_solo_consonantes(self):
        s = 'sltr'
        self.assertEqual(sin_vocales(s),'sltr')
    
    def test_palabra_con_vocales(self):
        s = 'vamos'
        self.assertEqual(sin_vocales(s),'vms')
    
class test_reemplaza_vocales(unittest.TestCase):
    def test_palabra_vacia(self):
        s = ''
        self.assertEqual(reemplaza_vocales(s),'')
    
    def test_sin_vocales(self):
        s = 'msl'
        self.assertEqual(reemplaza_vocales(s),'msl')
    
    def test_con_vocales(self):
        s = 'hola'
        self.assertEqual(reemplaza_vocales(s),'h-l-')

class test_da_vuelta_str(unittest.TestCase):
    def test_palabra_vacia(self):
        s = ''
        self.assertEqual(da_vuelta_str(s),'')
    
    def test_palabra(self):
        s = 'palabra'
        self.assertEqual(da_vuelta_str(s),'arbalap')


class test_eliminar_repetidos(unittest.TestCase):
    def test_palabra_vacia(self):
        s = ''
        self.assertEqual(eliminar_repetidos(s),'')
    
    def test_sin_repetidos(self):
        s = 'mora'
        self.assertEqual(eliminar_repetidos(s),'mora')
    
    def test_con_repetidos(self):
        s = 'moro'
        self.assertEqual(eliminar_repetidos(s),'mro')

class test_saldo(unittest.TestCase):
    def test_solo_ingresos(self):
        s = [('I',1000),('I',2000)]
        self.assertEqual(saldo(s),3000)
    
    def test_solo_retiros(self):
        s = [('R',2000),('R',1000)]
        self.assertEqual(saldo(s),-3000)
    
    def test_ingresos_y_retiros(self):
        s = [('I',2000),('R',1000),('I',500),('R',200)]
        self.assertEqual(saldo(s),1300)

class test_pertenece_a_cada_uno_v1(unittest.TestCase):
    def test_lista_vacia(self):
        s = [[]]
        self.assertEqual(pertenece_a_cada_uno_v1(s,3),[False])
    
    def test_todo_true(self):
        s = [[1,2],[2,3]]
        self.assertEqual(pertenece_a_cada_uno_v1(s,2),[True,True])
    
    def test_uno_true_otro_false (self):
        s = [[1,4],[2,3]]
        self.assertEqual(pertenece_a_cada_uno_v1(s,2),[False,True])
    

if __name__ == "__main__" :
    unittest.main()

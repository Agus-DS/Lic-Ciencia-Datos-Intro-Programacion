import unittest
from guia7 import *


class Test_suma_total (unittest.TestCase):
    def test_lista_vacia(self):
        s = []
        self.assertEqual(suma_total(s),0)

    def test_lista_con_solo_elemento(self):
        s = [2]
        self.assertEqual(suma_total[s],2)

    def test_lista_con_muchos_elementos(self):
        s = [1,2,3,4]
        self.assertEqual(suma_total(s),10)

    def test_lista_con_negativos(self):
        s = [1,-1,2,-2]
        self.assertEqual(suma_total(s),0)


class Test_divide_todos (unittest.TestCase):
    def test_solo_divide_primero(self):
        s = [4,3,3,5]
        self.assertTrue(divide_a_todos(s),4,False)

    def test_lista_vacia(self):
        s = []
        self.assertTrue(divide_a_todos(s),1,False)

    def test_solo_divide_ultimo(self):
        s = [3,3,3,4]
        self.assertTrue(divide_a_todos(s),2,False)

    def test_lista_con_elementos(self):
        s = [2,4,6,10]
        self.assertEqual(divide_a_todos(s),2,True)

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
        self.assertTrue(ordenados(s),False)
    
    def test_lista_negativos_en_orden(self):
        s = [-3,1,2]
        self.assertTrue(ordenados(s),True)

    def test_lista_positivos_en_orden(self):
        s = [1,2,3,5]
        self.assertTrue(ordenados(s),True)


    
if __name__ == "__main__" :
    unittest.main()

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

    
if __name__ == "__main__" :
    unittest.main()
import unittest
from calculadora import Calculadora

calculadora_tests = Calculadora()

class TestSumaValores(unittest.TestCase):
    
    def test_suma_valores(self):
        self.assertEqual(calculadora_tests.suma(1,2,3), 6)
        self.assertEqual(calculadora_tests.suma(20, -2, -3), 15)
        self.assertAlmostEqual(calculadora_tests.suma(1.2, 3.6, 10.3), 15.1)
    
    def test_un_valor(self):
        self.assertEqual(calculadora_tests.suma(1), 1)
    
    def test_suma_raises(self):
        
        with self.assertRaises(TypeError):
            calculadora_tests.suma()
            
        with self.assertRaises(TypeError):
                    calculadora_tests.suma("papas")
    

class TestMultiplicacionValores(unittest.TestCase):
    
    def test_multiplicacion_valores(self):
            self.assertEqual(calculadora_tests.multiplicacion(1,2,3), 6)
            self.assertEqual(calculadora_tests.multiplicacion(20, -2, -3), 120)
            self.assertAlmostEqual(calculadora_tests.multiplicacion(1.2, 3.6, 10.3), 44.496)
        
    def test_un_valor(self):
        self.assertEqual(calculadora_tests.multiplicacion(1), 1)
    
    def test_multiplicacion_raises(self):
        
        with self.assertRaises(TypeError):
            calculadora_tests.multiplicacion()
            
        with self.assertRaises(TypeError):
                    calculadora_tests.multiplicacion("papas")


if __name__ == '__main__':
    unittest.main()
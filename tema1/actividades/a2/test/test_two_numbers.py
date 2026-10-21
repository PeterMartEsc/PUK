import unittest
from calculadora import Calculadora

calculadora_tests = Calculadora()

class TestRestaValores(unittest.TestCase):
    
    def test_resta_valores(self):
        self.assertEqual(calculadora_tests.resta(4, 2), 2)
        self.assertEqual(calculadora_tests.resta(-30, 10), -40)
        self.assertAlmostEqual(calculadora_tests.resta(8.5, 3.1), 5.4)
    
    def test_resta_raises(self):
            
        with self.assertRaises(TypeError):
            calculadora_tests.resta("papas")
    

class TestDivisionValores(unittest.TestCase):
    
    def test_division_valores(self):
            self.assertEqual(calculadora_tests.division(15,5), 3)
            self.assertEqual(calculadora_tests.division(20, -2), -10)
            self.assertAlmostEqual(calculadora_tests.division(44.2, 22.1), 2)
    
    def test_division_raises(self):
            
        with self.assertRaises(ValueError):
            calculadora_tests.division(10, 0)
            
        with self.assertRaises(TypeError):
            calculadora_tests.division("papas")


if __name__ == '__main__':
    unittest.main()
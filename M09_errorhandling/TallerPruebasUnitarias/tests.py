import unittest

from prueba import SumNumbers

class TestSum(unittest.TestCase):
    def test_sum_number_default_args(self):
        '''
        Verifica los valores por defecto.
        '''
        self.assertEqual(SumNumbers(), 5050)
        self.assertEqual(SumNumbers(numbers=None), 5050)

    if __name__ == '__main__':
        unittest.main()

#! Para llamar la prueba => python -m unittest -v tests
#!                          tests es el nombre del archivo de prueba.
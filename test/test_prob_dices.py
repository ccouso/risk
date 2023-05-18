import unittest
from io import StringIO
import sys

# Importa la función que deseas probar
from src import risk_prob_function as rprob

class TestProbAttackersDefenders(unittest.TestCase):
    def test_prob_3_attackers_2_defenders(self):
        expected_result = ('0.3717', '0.3358', '0.2926')
        result = rprob.prob_3_attackers_2_defenders()
        self.assertEqual(result, expected_result)

    def test_prob_2_attackers_2_defenders(self):
        expected_result = ('0.2276', '0.3241', '0.4483')
        result = rprob.prob_2_attackers_2_defenders()
        self.assertEqual(result, expected_result)

    def test_prob_1_attackers_2_defenders(self):
        expected_result = ('0.2546', '0.7454')
        result = rprob.prob_1_attackers_2_defenders()
        self.assertEqual(result, expected_result)

    def test_prob_3_attackers_1_defenders(self):
        expected_result = ('0.6597', '0.3403')
        result = rprob.prob_3_attackers_1_defenders()
        self.assertEqual(result, expected_result)

    def test_prob_2_attackers_1_defenders(self):
        expected_result = ('0.5787', '0.4213')
        result = rprob.prob_2_attackers_1_defenders()
        self.assertEqual(result, expected_result)

    def test_prob_1_attackers_1_defenders(self):
        expected_result = ('0.4167', '0.5833')
        result = rprob.prob_1_attackers_1_defenders()
        self.assertEqual(result, expected_result)


    def test_calculate_simple_prob(self):
        event_A = 10
        total = 25
        expected_result = '0.4000'
        result = rprob.calculate_simple_prob(event_A, total)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    # Redirige la salida de la consola para evitar la impresión innecesaria
    sys.stdout = StringIO()
    unittest.main()
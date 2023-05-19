import unittest
from io import StringIO
import sys

# Importa la función que deseas probar
from src import risk_prob_function as rprob
from src import risk_sim as rsim

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


class Test_Sim_Risk(unittest.TestCase):
    def test_only_3_attackers(self):
        TOTAL_BATTLES = 50000
        attacker = 10
        defender = 10
        type_of_battle = "only_3_attackers"

        expected_result = ('0.34', '0.66')
        result = rsim.risk_simulator(TOTAL_BATTLES, attacker, defender, type_of_battle)

        self.assertEqual(format(float(result[4]), ".2f"), expected_result[0])
        self.assertEqual(format(float(result[5]), ".2f"), expected_result[1])

    def test_conventional(self):
        TOTAL_BATTLES = 20000
        attacker = 10
        defender = 10
        type_of_battle = "conventional"

        expected_result_min = ('0.56', '0.43')
        expected_result_max = ('0.57', '0.44')
        result = rsim.risk_simulator(TOTAL_BATTLES, attacker, defender, type_of_battle)

        self.assertGreaterEqual(format(float(result[4]), ".2f"), expected_result_min[0])
        self.assertGreaterEqual(format(float(result[5]), ".2f"), expected_result_min[1])
        self.assertLessEqual(format(float(result[4]), ".2f"), expected_result_max[0])
        self.assertLessEqual(format(float(result[5]), ".2f"), expected_result_max[1])


if __name__ == '__main__':
    # Redirige la salida de la consola para evitar la impresión innecesaria
    sys.stdout = StringIO()
    unittest.main()
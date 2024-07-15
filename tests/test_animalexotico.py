import unittest
from animal.animalexotico import Huron, BoaConstrictor


class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Hurón", 1.2, 2, "EEUU", 0.08)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        self.assertAlmostEqual(self.huron.calcular_flete(), 0.096)


class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = BoaConstrictor("Soru", 1.2, 5, "Sudan", 0.2)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        self.assertAlmostEqual(self.boa.calcular_flete(), 0.24)

    def test_comer_ratones(self):
        self.boa.comer_ratones(5)
        self.assertEqual(self.boa.obtener_ratones_comidos(), 5)


if __name__ == '__main__':
    unittest.main()

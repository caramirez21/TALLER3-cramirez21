import unittest
from animal.animalexotico import BoaConstrictor, Huron


class Guarderia:
    def __init__(self):
        self.boas = [BoaConstrictor("Boa1", 1.0, 3, "Brasil", 0.3),
                     BoaConstrictor("Boa2", 1.5, 4, "India", 0.4)]
        self.hurones = [Huron("Huron1", 1.1, 2, "EEUU", 0.08),
                        Huron("Huron2", 1.3, 3, "Canada", 0.09)]

    def alimentar_boa(self, boa, cantidad_ratones):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.comer_ratones(cantidad_ratones)
            return "Éxito"
        except ValueError as e:
            return "La boa está llena"


class TestGuarderia(unittest.TestCase):
    def setUp(self):
        self.guarderia = Guarderia()
        self.boa1 = self.guarderia.boas[0]

    def test_alimentar_boa_exito(self):
        self.assertEqual(self.guarderia.alimentar_boa(self.boa1, 5), "Éxito")

    def test_alimentar_boa_llena(self):
        self.assertEqual(self.guarderia.alimentar_boa(self.boa1, 20), "La boa está llena")

    def test_alimentar_boa_inexistente(self):
        self.assertEqual(self.guarderia.alimentar_boa(None, 5), "Esta Boa no existe!")


if __name__ == '__main__':
    unittest.main()

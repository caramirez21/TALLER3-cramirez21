from animal.animalexotico import Huron, BoaConstrictor
from tests.test_guarderia import Guarderia

# Uso de las clases
huron = Huron("Hurón", 1.2, 2, "EEUU", 0.08)
print(f"Sonido del {huron.obtener_nombre()}: {huron.hacer_sonido()}")

boa1 = BoaConstrictor("Soru", 1.2, 5, "Sudan", 0.2)
boa1.comer_ratones(5)
print(f"Ratones comidos por {boa1.obtener_nombre()}: {boa1.obtener_ratones_comidos()}")
print(f"Sonido de la {boa1.obtener_nombre()}: {boa1.hacer_sonido()}")

# Pruebas de Guarderia
guarderia = Guarderia()
print(guarderia.alimentar_boa(boa1, 5))  # Éxito
print(guarderia.alimentar_boa(boa1, 20))  # La boa está llena
print(guarderia.alimentar_boa(None, 5))   # Esta Boa no existe!

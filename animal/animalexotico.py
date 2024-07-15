from .animal import Animal


class AnimalExotico(Animal):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos

    def calcular_flete(self):
        return self.__impuestos * self.obtener_peso()

    def obtener_pais_origen(self):
        return self.__pais_origen

    def obtener_impuestos(self):
        return self.__impuestos


# Uso Clase

aexotico1 = AnimalExotico("Chaux", 120, 4, "Australia", 1000)
# print(f"Flete para {aexotico1.obtener_nombre()}: {aexotico1.calcular_flete()}")


class Huron(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)

    def hacer_sonido(self):
        return "¡Eek Eek!"


huron = Huron("Hurón", 1.2, 2, "EEUU", 0.08)
print(f"Sonido del {huron.obtener_nombre()}: {huron.hacer_sonido()}")


class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

    def comer_ratones(self, cantidad=1):
        if cantidad >= 20:
            raise ValueError("Demasiados Ratones!")
        if cantidad > 0:
            self.__ratones_comidos = cantidad
            return True
        else:
            return False

    def obtener_ratones_comidos(self):
        return self.__ratones_comidos


boa1 = BoaConstrictor("Soru", 1.2, 5, "Sudan", 0.2)
boa1.comer_ratones(5)
print(f"Ratones comidos por {boa1.obtener_nombre()}: {boa1.obtener_ratones_comidos()}")
print(f"Sonido de la {boa1.obtener_nombre()}: {boa1.hacer_sonido()}")

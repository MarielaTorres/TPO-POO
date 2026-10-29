class Sala:
    def __init__(self, id_sala, nombre, capacidad):
        self.id_sala = id_sala
        self.nombre = nombre
        self.capacidad = capacidad

    def ver_datos(self):
        print("Sala:", self.nombre)
        print("Capacidad:", self.capacidad)

    def tiene_capacidad(self, cantidad):
        return cantidad <= self.capacidad

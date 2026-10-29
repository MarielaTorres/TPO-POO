class Persona:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def ver_datos(self):
        print(self.nombre, self.apellido, "-", self.email)


class Speaker(Persona):
    def __init__(self, nombre, apellido, email, especialidad):
        super().__init__(nombre, apellido, email)
        self.especialidad = especialidad

    def ver_datos(self):
        super().ver_datos()
        print("Especialidad:", self.especialidad)


# Pruebas
speaker1 = Speaker(
    "Ana",
    "Martinez",
    "ana@ejemplo.com",
    "Cloud Computing"
)

speaker1.ver_datos()

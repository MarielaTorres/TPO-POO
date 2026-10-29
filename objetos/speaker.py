from objetos.persona import Persona
class Speaker(Persona):
    def __init__(self, nombre, apellido, email, especialidad):
        super().__init__(nombre, apellido, email)
        self.especialidad = especialidad

    def ver_datos(self):
        super().ver_datos()
        print("Especialidad:", self.especialidad)


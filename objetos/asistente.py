from objetos.persona import Persona

class Asistente(Persona):
    def __init__(self, nombre, apellido, email, dni):
        super().__init__(nombre, apellido, email)
        self.dni = dni
        self.inscripciones = []

    def ver_inscripciones(self):
        print("Inscripciones de:", self.nombre)
        for inscripcion in self.inscripciones:
            print("-", inscripcion.evento.nombre)


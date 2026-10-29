class Persona:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
    def ver_datos(self):
        print(self.nombre, self.apellido, "-", self.email)
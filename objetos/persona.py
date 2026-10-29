class Persona:
    def __init__(self, nombre, apellido, email, id_persona=None):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def ver_datos(self):
        print(self.nombre, self.apellido, "-", self.email)

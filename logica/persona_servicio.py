from objetos.persona import Persona
from db.persona_repositorio import PersonaRepositorio

class PersonaServicio:
    def __init__(self):
        self.repositorio = PersonaRepositorio()

    def registrar_persona(self, nombre, apellido, email):
        nombre = nombre.strip()
        apellido = apellido.strip()
        email = email.strip().lower()

        if not nombre or not apellido or not email:
            raise ValueError("Todos los campos son obligatorios.")

        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("El correo electrónico no es válido.")

        persona = Persona(nombre, apellido, email)

        self.repositorio.guardar(persona)

        return persona

    def listar_personas(self):
        return self.repositorio.listar()

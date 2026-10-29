from objetos.persona import Persona

class Organizador(Persona):
    def __init__(self, nombre, apellido, email, empresa):
        super().__init__(nombre, apellido, email)
        self.empresa = empresa
        self.eventos = []

    def crear_evento(self, evento):
        self.eventos.append(evento)
        print("Evento registrado:", evento.nombre)

    def ver_eventos(self):
        print("Eventos organizados por", self.nombre)
        for evento in self.eventos:
            print("-", evento.nombre)

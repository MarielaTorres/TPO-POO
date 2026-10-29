class Evento:
    def __init__(self, id_evento, nombre, fecha, lugar, capacidad):
        self.id_evento = id_evento
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar
        self.capacidad = capacidad
        self.charlas = []
        self.salas = []
        self.inscripciones = []

    def agregar_charla(self, charla):
        self.charlas.append(charla)
        print("Charla agregada:", charla.titulo)

    def agregar_sala(self, sala):
        self.salas.append(sala)
    
    def cupos_disponibles(self):
        confirmadas = 0

        for inscripcion in self.inscripciones:
            if inscripcion.estado == "Confirmada":
                confirmadas += 1

        return self.capacidad - confirmadas

    def ver_datos(self):
        print("Evento:", self.nombre)
        print("Fecha:", self.fecha)
        print("Lugar:", self.lugar)
        print("Capacidad:", self.capacidad)
        print("Cupos disponibles:", self.cupos_disponibles())

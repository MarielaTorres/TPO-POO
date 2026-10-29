from datetime import date

class Inscripcion:
    def __init__(self, id_inscripcion, asistente, evento):
        self.id_inscripcion = id_inscripcion
        self.asistente = asistente
        self.evento = evento
        self.fecha = date.today()
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado == "Cancelada":
            print("No se puede confirmar una inscripción cancelada.")
            return False

        if self.estado == "Confirmada":
            print("La inscripción ya está confirmada.")
            return False

        if self.evento.cupos_disponibles() <= 0:
            print("No hay cupos disponibles.")
            return False

        # Verificamos que el asistente no tenga otra
        # inscripción activa al mismo evento.
        for inscripcion in self.evento.inscripciones:
            if (inscripcion.asistente is self.asistente
                    and inscripcion.estado == "Confirmada"):
                print("El asistente ya está inscripto.")
                return False

        self.estado = "Confirmada"
        self.evento.inscripciones.append(self)
        self.asistente.inscripciones.append(self)

        print("Inscripción confirmada.")
        return True

    def cancelar(self):
        if self.estado != "Confirmada":
            print("No hay una inscripción confirmada para cancelar.")
            return False

        self.estado = "Cancelada"
        print("Inscripción cancelada.")
        return True

    def ver_datos(self):
        print("Asistente:", self.asistente.nombre)
        print("Evento:", self.evento.nombre)
        print("Estado:", self.estado)

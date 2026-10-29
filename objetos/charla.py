class Charla:
    def __init__(self, id_charla, titulo, horario_inicio, horario_fin):
        self.id_charla = id_charla
        self.titulo = titulo
        self.horario_inicio = horario_inicio
        self.horario_fin = horario_fin
        self.speaker = None
        self.sala = None

    def asignar_speaker(self, speaker):
        self.speaker = speaker

    def asignar_sala(self, sala):
        self.sala = sala

    def ver_datos(self):
        print("Charla:", self.titulo)
        print("Inicio:", self.horario_inicio)
        print("Fin:", self.horario_fin)

        if self.speaker is not None:
            print("Speaker:", self.speaker.nombre, self.speaker.apellido)

        if self.sala is not None:
            print("Sala:", self.sala.nombre)

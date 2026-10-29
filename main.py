from datetime import datetime

from objetos.organizador import Organizador
from objetos.speaker import Speaker
from objetos.asistente import Asistente
from objetos.evento import Evento
from objetos.charla import Charla
from objetos.sala import Sala
from objetos.inscripcion import Inscripcion


# Creo un organizador
organizador1 = Organizador(
    "María", "Gómez",
    "maria@ejemplo.com", "Tech Eventos"
)

# Creo un speaker
speaker1 = Speaker(
    "Ana", "Martínez",
    "ana@ejemplo.com", "Cloud Computing"
)

# Creo un asistente
asistente1 = Asistente(
    "Juan", "Pérez",
    "juan@ejemplo.com", "12345678"
)

# Creo dos eventos independientes
evento1 = Evento(
    1, "AWS Community Day",
    datetime(2026, 11, 20),
    "Buenos Aires", 150
)

evento2 = Evento(
    2, "Workshop de IA",
    datetime(2026, 12, 5),
    "Buenos Aires", 30
)

# Asignar los eventos al organizador
organizador1.crear_evento(evento1)
organizador1.crear_evento(evento2)

# Creo una charla
charla1 = Charla(
    1,
    "Introducción a AWS",
    datetime(2026, 11, 20, 10, 0),
    datetime(2026, 11, 20, 11, 0)
)

# Asignar un speaker
charla1.asignar_speaker(speaker1)

# Agregar la charla al primer evento
evento1.agregar_charla(charla1)

# Mostrar información
print("\n--- ORGANIZADOR ---")
organizador1.ver_eventos()

print("\n--- EVENTO 1 ---")
evento1.ver_datos()

print("\n--- EVENTO 2 ---")
evento2.ver_datos()

print("\n--- CHARLA ---")
charla1.ver_datos()

# Crear una sala
sala1 = Sala(1, "Auditorio Principal", 100)

# Asociar la sala al evento y a la charla
evento1.agregar_sala(sala1)
charla1.asignar_sala(sala1)

# Crear una inscripción
inscripcion1 = Inscripcion(1, asistente1, evento1)

# Confirmar la inscripción
inscripcion1.confirmar()

print("\n--- INSCRIPCION ---")
inscripcion1.ver_datos()

print("\n--- CUPOS ---")
print("Cupos disponibles:", evento1.cupos_disponibles())

# Ver las inscripciones del asistente
asistente1.ver_inscripciones()


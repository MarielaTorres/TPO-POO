from objetos.persona import Persona
from db.persona_repositorio import PersonaRepositorio


repositorio = PersonaRepositorio()

# Crear una persona
persona1 = Persona(
    "Ana",
    "Martinez",
    "ana@ejemplo.com"
)

# Guardar la persona
id_generado = repositorio.guardar(persona1)

print("Persona guardada con ID:", id_generado)

# Consultar los registros existentes
print("\n--- PERSONAS REGISTRADAS ---")

personas = repositorio.listar()

for persona in personas:
    print(
        persona.id_persona,
        persona.nombre,
        persona.apellido,
        persona.email
    )

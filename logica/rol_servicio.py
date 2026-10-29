from db.rol_repositorio import RolRepositorio

class RolServicio:

    def __init__(self):
        self.repositorio = RolRepositorio()

    def validar_persona(self, id_persona):
        if not self.repositorio.persona_existe(id_persona):
            raise ValueError(
                "No existe una persona con ese ID."
            )

    def registrar_asistente(self, id_persona, dni):
        self.validar_persona(id_persona)

        dni = dni.strip()
        if not dni:
            raise ValueError("El DNI es obligatorio.")

        self.repositorio.agregar_asistente(
            id_persona, dni
        )

    def registrar_speaker(
        self, id_persona, especialidad, biografia
    ):
        self.validar_persona(id_persona)

        especialidad = especialidad.strip()
        if not especialidad:
            raise ValueError(
                "La especialidad es obligatoria."
            )

        self.repositorio.agregar_speaker(
            id_persona, especialidad, biografia.strip()
        )

    def registrar_organizador(self, id_persona, empresa):
        self.validar_persona(id_persona)

        empresa = empresa.strip()
        if not empresa:
            raise ValueError("La empresa es obligatoria.")

        self.repositorio.agregar_organizador(
            id_persona, empresa
        )

    def listar(self, rol):
        return self.repositorio.listar_roles(rol)

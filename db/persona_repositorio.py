from db.conexion import conectar
from objetos.persona import Persona

class PersonaRepositorio:

    def guardar(self, persona):
        conexion = conectar()
        cursor = None

        try:
            cursor = conexion.cursor()

            sql = """
                INSERT INTO persona
                    (nombre, apellido, email)
                VALUES (%s, %s, %s)
            """

            valores = (
                persona.nombre,
                persona.apellido,
                persona.email
            )

            cursor.execute(sql, valores)
            conexion.commit()

            persona.id_persona = cursor.lastrowid

            return persona.id_persona

        except Exception:
            conexion.rollback()
            raise

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def listar(self):
        conexion = conectar()
        cursor = None

        try:
            cursor = conexion.cursor(dictionary=True)

            cursor.execute("""
                SELECT id_persona, nombre, apellido, email
                FROM persona
                ORDER BY id_persona
            """)

            registros = cursor.fetchall()
            personas = []

            for registro in registros:
                persona = Persona(
                    registro["nombre"],
                    registro["apellido"],
                    registro["email"],
                    registro["id_persona"]
                )

                personas.append(persona)

            return personas

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

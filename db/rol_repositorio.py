from db.conexion import conectar

class RolRepositorio:

    def persona_existe(self, id_persona):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute(
                "SELECT id_persona FROM persona WHERE id_persona = %s",
                (id_persona,)
            )
            return cursor.fetchone() is not None
        finally:
            cursor.close()
            conexion.close()

    def agregar_asistente(self, id_persona, dni):
        sql = """
            INSERT INTO asistente (id_persona, dni)
            VALUES (%s, %s)
        """
        self._ejecutar(sql, (id_persona, dni))

    def agregar_speaker(self, id_persona, especialidad, biografia):
        sql = """
            INSERT INTO speaker
                (id_persona, especialidad, biografia)
            VALUES (%s, %s, %s)
        """
        self._ejecutar(
            sql, (id_persona, especialidad, biografia)
        )

    def agregar_organizador(self, id_persona, empresa):
        sql = """
            INSERT INTO organizador (id_persona, empresa)
            VALUES (%s, %s)
        """
        self._ejecutar(sql, (id_persona, empresa))

    def listar_roles(self, rol):
        tablas = {
            "asistente": "asistente",
            "speaker": "speaker",
            "organizador": "organizador"
        }

        if rol not in tablas:
            raise ValueError("Rol inválido")

        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        try:
            # El nombre de tabla procede de una lista fija,
            # nunca de texto libre introducido por el usuario.
            sql = f"""
                SELECT p.id_persona, p.nombre,
                       p.apellido, p.email, r.*
                FROM persona p
                INNER JOIN {tablas[rol]} r
                    ON p.id_persona = r.id_persona
                ORDER BY p.apellido, p.nombre
            """
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close()
            conexion.close()

    def _ejecutar(self, sql, valores):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute(sql, valores)
            conexion.commit()
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()

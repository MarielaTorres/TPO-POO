from pathlib import Path
from db.conexion import conectar
import mysql.connector


CARPETA = Path(__file__).resolve().parent
RUTA_SQL = CARPETA / "schema.sql"


def crear_base_de_datos():
    conexion = None
    cursor = None

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        with open(RUTA_SQL, "r", encoding="utf-8") as archivo:
            script_sql = archivo.read()

        # Ejecutar las instrucciones SQL del archivo
        instrucciones = script_sql.split(";")

        for instruccion in instrucciones:
            instruccion = instruccion.strip()

            if instruccion:
                cursor.execute(instruccion)

        conexion.commit()

        print("Tablas creadas correctamente en MySQL.")

    except (mysql.connector.Error, OSError) as error:
        if conexion is not None:
            conexion.rollback()
        print("Error al crear las tablas:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()


if __name__ == "__main__":
    crear_base_de_datos()

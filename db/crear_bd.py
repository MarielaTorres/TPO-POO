import sqlite3
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
RUTA_BD = CARPETA / "eventmanager.db"
RUTA_SQL = CARPETA / "schema.sql"

def crear_base_de_datos():
    with sqlite3.connect(RUTA_BD) as conexion:
        conexion.execute("PRAGMA foreign_keys = ON")

        with open(RUTA_SQL, "r", encoding="utf-8") as archivo:
            script_sql = archivo.read()

        conexion.executescript(script_sql)

    print("Base de datos creada correctamente.")
    print("Ubicación:", RUTA_BD)


if __name__ == "__main__":
    crear_base_de_datos()

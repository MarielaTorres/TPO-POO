import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv


# Buscar el archivo .env en la raíz del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parent.parent
load_dotenv(RUTA_PROYECTO / ".env")

def conectar():
    conexion = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return conexion

if __name__ == "__main__":
    try:
        conexion = conectar()
        print("Conexión a MySQL exitosa.")
        conexion.close()

    except mysql.connector.Error as error:
        print("Error de conexión:", error)

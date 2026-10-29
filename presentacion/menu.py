import mysql.connector

from logica.persona_servicio import PersonaServicio
from logica.rol_servicio import RolServicio

def mostrar_menu():
    print("\n================================")
    print("          EVENTMANAGER")
    print("================================")
    print("1. Gestionar eventos")
    print("2. Gestionar organizadores")
    print("3. Gestionar speakers")
    print("4. Gestionar asistentes")
    print("5. Gestionar charlas")
    print("6. Gestionar salas")
    print("7. Gestionar inscripciones")
    print("8. Gestionar personas")
    print("0. Salir")
    print("================================")


def menu_personas():
    servicio = PersonaServicio()

    while True:
        print("\n--- GESTIÓN DE PERSONAS ---")
        print("1. Registrar persona")
        print("2. Listar personas")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")

            try:
                persona = servicio.registrar_persona(
                    nombre, apellido, email
                )

                print("Persona registrada correctamente.")
                print("ID generado:", persona.id_persona)

            except ValueError as error:
                print("Error de validación:", error)

            except mysql.connector.IntegrityError as error:
                if error.errno == 1062:
                    print("Ya existe una persona con ese email.")
                else:
                    print("Error de integridad:", error)

            except mysql.connector.Error as error:
                print("Error al guardar en MySQL:", error)

        elif opcion == "2":
            try:
                personas = servicio.listar_personas()

                if not personas:
                    print("No hay personas registradas.")

                for persona in personas:
                    print(
                        persona.id_persona,
                        "-",
                        persona.nombre,
                        persona.apellido,
                        "-",
                        persona.email
                    )

            except mysql.connector.Error as error:
                print("Error al consultar MySQL:", error)

        elif opcion == "0":
            break

        else:
            print("Opción incorrecta.")


def iniciar_menu():
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "8":
            menu_personas()

        elif opcion == "2":
            menu_roles("organizador")

        elif opcion == "3":
            menu_roles("speaker")

        elif opcion == "4":
            menu_roles("asistente")

        elif opcion in ("1", "5", "6", "7"):
            print("Esta funcionalidad está en desarrollo.")

        elif opcion == "0":
            print("Gracias por utilizar EventManager.")

        else:
            print("Opción incorrecta.")


def menu_roles(tipo):
    servicio = RolServicio()

    while True:
        print("\n--- GESTIÓN DE", tipo.upper(), "---")
        print("1. Asignar rol a una persona")
        print("2. Listar personas con este rol")
        print("0. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            break

        elif opcion == "1":
            try:
                id_persona = int(input("ID de persona: "))

                if tipo == "asistente":
                    dni = input("DNI: ")
                    servicio.registrar_asistente(
                        id_persona, dni
                    )

                elif tipo == "speaker":
                    especialidad = input("Especialidad: ")
                    biografia = input("Biografía: ")
                    servicio.registrar_speaker(
                        id_persona, especialidad, biografia
                    )

                elif tipo == "organizador":
                    empresa = input("Empresa: ")
                    servicio.registrar_organizador(
                        id_persona, empresa
                    )

                print("Rol registrado correctamente.")

            except ValueError as error:
                print("Error de validación:", error)

            except mysql.connector.IntegrityError as error:
                if error.errno == 1062:
                    print("El rol o identificador ya existe.")
                else:
                    print("Error de integridad:", error)

            except mysql.connector.Error as error:
                print("Error de MySQL:", error)

        elif opcion == "2":
            try:
                registros = servicio.listar(tipo)

                if not registros:
                    print("No hay registros.")

                for registro in registros:
                    print(
                        registro["id_persona"],
                        registro["nombre"],
                        registro["apellido"],
                        "-",
                        registro["email"]
                    )

            except mysql.connector.Error as error:
                print("Error de MySQL:", error)

        else:
            print("Opción incorrecta.")

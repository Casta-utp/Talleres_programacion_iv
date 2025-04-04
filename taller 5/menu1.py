from punto1 import *

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Llenar lista de personal")
        print("2. Mostrar lista de personal")
        print("3. Calcular sueldo (solo para profesores)")
        print("4. Mostrar materias asignadas")
        print("5. Calcular promedio (solo para alumnos o profesores ayudantes)")
        print("6. Guardar lista de personal en archivo")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            PersonalUniversitario.llenar_lista_personal()

        elif opcion == "2":
            print("\n--- Lista de Personal ---")
            for personal in PersonalUniversitario.listaPersonal:
                print(personal)

        elif opcion == "3":
            print("\n--- Calcular Sueldo ---")
            for i, personal in enumerate(PersonalUniversitario.listaPersonal):
                if isinstance(personal, Profesor):
                    print(f"{i + 1}. {personal.nombre}")
            indice = int(input("Seleccione un profesor por número: ")) - 1
            if 0 <= indice < len(PersonalUniversitario.listaPersonal):
                profesor = PersonalUniversitario.listaPersonal[indice]
                if isinstance(profesor, Profesor):
                    print(f"Sueldo de {profesor.nombre}: {profesor.sueldo()}")
                else:
                    print("La persona seleccionada no es un profesor.")
            else:
                print("Índice no válido.")

        elif opcion == "4":
            print("\n--- Mostrar Materias Asignadas ---")
            for i, personal in enumerate(PersonalUniversitario.listaPersonal):
                print(f"{i + 1}. {personal.nombre}")
            indice = int(input("Seleccione una persona por número: ")) - 1
            if 0 <= indice < len(PersonalUniversitario.listaPersonal):
                personal = PersonalUniversitario.listaPersonal[indice]
                print(f"Materias asignadas a {personal.nombre}: {personal.materias()}")
            else:
                print("Índice no válido.")

        elif opcion == "5":
            print("\n--- Calcular Promedio ---")
            for i, personal in enumerate(PersonalUniversitario.listaPersonal):
                if isinstance(personal, (Alumno, ProfesorAyudante)):
                    print(f"{i + 1}. {personal.nombre}")
            indice = int(input("Seleccione un alumno o profesor ayudante por número: ")) - 1
            if 0 <= indice < len(PersonalUniversitario.listaPersonal):
                persona = PersonalUniversitario.listaPersonal[indice]
                if isinstance(persona, (Alumno, ProfesorAyudante)):
                    print(f"Promedio de {persona.nombre}: {persona.promedio()}")
                else:
                    print("La persona seleccionada no es un alumno o profesor ayudante.")
            else:
                print("Índice no válido.")

        elif opcion == "6":
            PersonalUniversitario.guardar_lista_personal()
            print("Lista de personal guardada en 'personal.txt'.")

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Llamar al menú principal
menu()

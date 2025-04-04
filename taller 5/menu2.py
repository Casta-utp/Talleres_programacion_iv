from punto2 import *
from time import sleep

def main():
    talleres = []
    empleados = []
    carros = []
    clientes = []

    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear Taller")
        print("2. Crear Empleado")
        print("3. Crear Carro")
        print("4. Crear Cliente")
        print("5. Mostrar Información")
        print("6. Guardar Información")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del taller: ")
            direccion = input("Dirección del taller: ")
            telefono = input("Teléfono del taller: ")
            taller = Taller(nombre, direccion, telefono, [])
            talleres.append(taller)
            print("Taller creado exitosamente.")

        elif opcion == "2":
            print("\n--- Crear Empleado ---")
            print("1. Mecanico")
            print("2. Recepcionista")
            print("3. Gerente")
            tipo_empleado = input("Seleccione el tipo de empleado: ")

            nombre_taller = input("Nombre del taller: ")
            if nombre_taller not in [taller.nombre for taller in talleres]:
                print("Taller no encontrado.")
                continue
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            nombre_empleado = input("Nombre del empleado: ")
            edad_empleado = int(input("Edad del empleado: "))
            fecha_ingreso = int(input("Año de ingreso: "))
            salario = float(input("Salario: "))

            if tipo_empleado == "1":
                especialidad = input("Especialidad del mecánico: ")
                horas = int(input("Horas trabajadas: "))
                empleado = Mecanico(nombre_taller, direccion, telefono, [], nombre_empleado, edad_empleado, fecha_ingreso, salario, especialidad, horas)
            elif tipo_empleado == "2":
                turno = input("Turno del recepcionista: ")
                empleado = Recepcionista(nombre_taller, direccion, telefono, [], nombre_empleado, edad_empleado, fecha_ingreso, salario, turno)
            elif tipo_empleado == "3":
                bono = float(input("Bono del gerente: "))
                empleado = Gerente(nombre_taller, direccion, telefono, [], nombre_empleado, edad_empleado, fecha_ingreso, salario, bono)
            else:
                print("Opción no válida.")
                continue

            empleados.append(empleado)
            print("Empleado creado exitosamente.")

        elif opcion == "3":
            nombre_taller = input("Nombre del taller: ")
            if nombre_taller not in [taller.nombre for taller in talleres]:
                print("Taller no encontrado.")
                continue
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            marca = input("Marca del carro: ")
            modelo = input("Modelo del carro: ")
            color = input("Color del carro: ")
            placa = input("Placa del carro: ")
            carro = Carros(nombre_taller, direccion, telefono, [], marca, modelo, color, placa)
            carros.append(carro)
            print("Carro creado exitosamente.")

        elif opcion == "4":
            nombre_taller = input("Nombre del taller: ")
            if nombre_taller not in [taller.nombre for taller in talleres]:
                print("Taller no encontrado.")
                continue
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            nombre_cliente = input("Nombre del cliente: ")
            edad_cliente = int(input("Edad del cliente: "))
            telefono_cliente = input("Teléfono del cliente: ")
            cliente = Clientes(nombre_taller, direccion, telefono, [], nombre_cliente, edad_cliente, telefono_cliente)
            clientes.append(cliente)
            print("Cliente creado exitosamente.")

        elif opcion == "5":
            print("\n--- Mostrar Información ---")
            print("1. Talleres")
            print("2. Empleados")
            print("3. Carros")
            print("4. Clientes")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                for taller in talleres:
                    print(taller)
            elif sub_opcion == "2":
                for empleado in empleados:
                    print(empleado)
            elif sub_opcion == "3":
                for carro in carros:
                    print(carro)
            elif sub_opcion == "4":
                for cliente in clientes:
                    print(cliente)
            else:
                print("Opción no válida.")

        elif opcion == "6":
            print("\n--- Guardar Información ---")
            print("1. Talleres")
            print("2. Empleados")
            print("3. Carros")
            print("4. Clientes")
            sub_opcion = input("Seleccione una opción: ")
            if sub_opcion == "1":
                Taller.guardar_talleres(talleres)
            elif sub_opcion == "2":
                Taller.guardar_empleados(empleados)
            elif sub_opcion == "3":
                Taller.guardar_carros(carros)
            elif sub_opcion == "4":
                Taller.guardar_clientes(clientes)
            else:
                print("Opción no válida.")

        elif opcion == "7":
            print("Saliendo del programa")
            for i in range(3):
                sleep(0.5)
                print(".", end=" ", flush=True)
            print()  # Move to the next line after printing dots
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
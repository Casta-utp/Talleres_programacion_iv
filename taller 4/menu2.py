from punto2 import *

def main():
    vehiculo = Vehiculo("", "")
    lista = []

    while True:
        print("\nMenú de opciones:")
        print("1. Llenar lista de vehículos")
        print("2. Mostrar lista de vehículos")
        print("3. Guardar lista de vehículos en archivo")
        print("4. Cargar lista de vehículos desde archivo")
        print("5. Consultar calidad de ruedas")
        print("6. Consultar combustible aconsejado")
        print("7. Tiempo de viaje (Pereira-Destino)")
        print("8. Vehiculos con x ruedas")
        print("9. Gasto de combustible")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            vehiculo.llenar_lista(lista)
        elif opcion == "2":
            vehiculo.mostrar_lista(lista)
        elif opcion == "3":
            vehiculo.guardar_lista(lista)
        elif opcion == "4":
            vehiculo.cargar_lista(lista)
        elif opcion == "5":
            try:
                indice = int(input("Ingrese el índice del vehículo: "))
                vehiculo = lista[indice]
                vehiculo.ruedas_calidad(vehiculo.marca, vehiculo.tipo)
            except (IndexError, ValueError):
                print("Índice no válido. Por favor, intente de nuevo.")
        elif opcion == "6":
            try:
                indice = int(input("Ingrese el índice del vehículo: "))
                vehiculo = lista[indice]
                vehiculo.combustible_aconsejado(vehiculo.marca, vehiculo.tipo)
            except (IndexError, ValueError):
                print("Índice no válido. Por favor, intente de nuevo.")
        elif opcion == "7":
            try:
                indice = int(input("Ingrese el índice del vehículo: "))
                vehiculo = lista[indice]
                velocidad = int(input("Ingrese la velocidad del vehículo (km/h): "))
                vehiculo.tiempo_viaje(velocidad)
            except (IndexError, ValueError):
                print("Índice no válido. Por favor, intente de nuevo.")
        elif opcion == "8":
            vehiculo.listar_vehiculos_ruedas(lista)
        elif opcion == "9":
            try:
                indice = int(input("Ingrese el índice del vehículo: "))
                vehiculo = lista[indice]
                vehiculo.consumo_gasolina(vehiculo.marca, vehiculo.tipo)
            except (IndexError, ValueError):
                print("Índice no válido. Por favor, intente de nuevo.")
        elif opcion == "10":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()

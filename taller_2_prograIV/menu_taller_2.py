from taller_2 import Lista, Lista_usuario, Ordenar_lista, Libro, Casa, Pelicula, Bodega, Lampara, Modem, Router, Maletin, Paciente_oncologico, Gato

def menu():
    while True:
        print("\nMenu:")
        print("1. Ejercicio 1: Lista de números")
        print("2. Ejercicio 2: Lista de usuarios")
        print("3. Ejercicio 3: Ordenar lista de palabras")
        print("4. Ejercicio 4: Clases varias")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            lista = Lista()
            lista.llenar_lista()
            lista.sumar_digitos()
            lista.guardar_ambas_listas()
        elif opcion == "2":
            lista_usuario = Lista_usuario()
            lista_usuario.incluir_usuarios()
            lista_usuario.conteo_usuario()
            lista_usuario.impar_par()
            lista_usuario.guardar_usuarios()
        elif opcion == "3":
            ordenar_lista = Ordenar_lista()
            ordenar_lista.llenar_lista()
            ordenar_lista.ordenar_palabras()
            ordenar_lista.guardar_lista()
        elif opcion == "4":
            while True:
                print("\nEjercicio 4: Clases varias")
                print("1. Libro")
                print("2. Casa")
                print("3. Pelicula")
                print("4. Bodega")
                print("5. Lampara")
                print("6. Modem")
                print("7. Router")
                print("8. Maletin")
                print("9. Paciente Oncologico")
                print("10. Gato")
                print("11. Volver al menu principal")
                
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "1":
                    libro = Libro()
                    libro.ingresar_datos()
                    print(f"Precio con IVA: {libro.precio_iva()}")
                    libro.guardar_datos()
                elif sub_opcion == "2":
                    casa = Casa()
                    casa.ingresar_datos()
                    casa.valor_metro()
                    casa.subsidio()
                    casa.pagar_impuestos()
                    casa.guardar_datos()
                elif sub_opcion == "3":
                    pelicula = Pelicula()
                    pelicula.ingresar_datos()
                    pelicula.duracion_horas()
                    pelicula.es_clasico()
                    pelicula.puntaje()
                    pelicula.guardar_datos()
                elif sub_opcion == "4":
                    bodega = Bodega()
                    bodega.ingresar_datos()
                    bodega.agregar_producto()
                    bodega.mostrar_inventario()
                    bodega.guardar_datos()
                elif sub_opcion == "5":
                    lampara = Lampara()
                    lampara.ingresar_datos()
                    lampara.encender()
                    lampara.apagar()
                    lampara.guardar_datos()
                elif sub_opcion == "6":
                    modem = Modem()
                    modem.ingresar_datos()
                    modem.encender()
                    modem.apagar()
                    modem.guardar_datos()
                elif sub_opcion == "7":
                    router = Router()
                    router.ingresar_datos()
                    router.conectar_dispositivo()
                    router.desconectar_dispositivo()
                    router.guardar_datos()
                elif sub_opcion == "8":
                    maletin = Maletin()
                    maletin.ingresar_datos()
                    maletin.abrir_maletin()
                    maletin.agregar_objeto()
                    maletin.cerrar_maletin()
                    maletin.guardar_datos()
                elif sub_opcion == "9":
                    paciente = Paciente_oncologico()
                    paciente.ingresar_datos()
                    paciente.tratamiento_aplicado()
                    paciente.tiempo_tratamiento()
                    paciente.tiempo_vida()
                    paciente.guardar_datos()
                elif sub_opcion == "10":
                    gato = Gato()
                    gato.ingresar_datos()
                    gato.vacunar()
                    gato.alimentar()
                    gato.guardar_datos()
                elif sub_opcion == "11":
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
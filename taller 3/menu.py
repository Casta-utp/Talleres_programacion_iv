from punto_1 import Avion
from punto_1 import Celular
from punto_1 import Asignatura
from punto_1 import Ejercito
from punto_1 import Silla
from punto_1 import Audifonos
from punto_2 import Rectangulo
from punto_3 import Empleado
from punto_4 import Calculadora
from punto_5 import Lista
from punto_6 import ArchivoEjemplo

def menu():
    while True:
        print("1. Clases ejercicio #1")
        print("2. Ejercicio #2")
        print("3. Ejercicio #3")
        print("4. Ejercicio #4")
        print("5. Ejercicio #5")
        print("6. Ejercicio #6")
        print("7. Salir")

        opcion = int(input("Ingrese la opción: "))

        print("\n")

        if opcion == 1:
            print("Clases ejercicio #1, escoge una opción:")
            print("1. Avion")
            print("2. Celular")
            print("3. Asignatura")
            print("4. Ejercito")
            print("5. Silla")
            print("6. Audifonos")
            print("7. Salir")
            opcion_clases = int(input("Ingrese la opción: "))
            print("\n")

            if opcion_clases == 1:
                avion = Avion()
                avion.llenar_datos()
                avion.cargar_bodega()
                print(avion)
            elif opcion_clases == 2:
                celular = Celular()
                celular.llenar_datos()
                celular.instalar_aplicacion()
                celular.desinstalar_aplicacion()
                celular.mostrar_aplicaciones()
                print(celular)
            elif opcion_clases == 3:
                asignatura = Asignatura()
                asignatura.llenar_datos()
                asignatura.agregar_estudiantes()
                asignatura.mostrar_estudiantes()
                print(asignatura)
            elif opcion_clases == 4:
                ejercito = Ejercito()
                ejercito.llenar_datos()
                ejercito.agregar_soldados()
                ejercito.mostrar_soldados()
                print(ejercito)
            elif opcion_clases == 5:
                silla = Silla()
                silla.llenar_datos()
                silla.calcular_volumen()
                print(silla)
            elif opcion_clases == 6:
                audifonos = Audifonos()
                audifonos.llenar_datos()
                audifonos.conectar_bluetooth()
                print(audifonos)
            elif opcion_clases == 7:
                pass
        elif opcion == 2:
            rectangulo = Rectangulo()
            rectangulo.llenar_datos()
            rectangulo.imprimir_rectangulo()
            rectangulo.calcular_area()
            rectangulo.calcular_perimetro()
            print(rectangulo)
        elif opcion == 3:
            empleado = Empleado()
            empleado.llenar_datos()
            empleado.calcular_salario()
            empleado.calcular_tiempo_pension()
            empleado.calcular_pension_salud()
            empleado.guardar_datos()
            print(empleado)
        elif opcion == 4:
            calculadora = Calculadora()
            calculadora.llenar_datos()
            print(calculadora)
            calculadora.sumar()
            print(calculadora)
            calculadora.restar()
            print(calculadora)
            calculadora.multiplicar()
            print(calculadora)
            calculadora.dividir()
            print(calculadora)
            calculadora.potencia()
            print(calculadora)
            calculadora.modulo()
            print(calculadora)
            calculadora.raiz_cuadrada()
            print(calculadora)
            calculadora.raiz_n()
            print(calculadora)
            calculadora.logaritmo()
            print(calculadora)
            calculadora.logaritmo_base_n()
            print(calculadora)
            calculadora.seno()
            print(calculadora)
        elif opcion == 5:
            lista = Lista()
            lista.guardar_lista()
            lista.llenar_lista_numeros
            lista.llenar_lista_palabras
            lista.guardar_lista_numeros
            lista.guardar_lista_palabras
            lista.llenar_lista_impares
            lista.guardar_lista_impares
            lista.imprimir_media_lista
            print(lista)
        elif opcion == 6:
            # Ejemplo de uso de la clase
            archivo = ArchivoEjemplo('archivo_ejemplo.txt')
            archivo.leer_archivo()
            archivo.escribir_archivo('Este es un ejemplo de escritura con la sentencia with.\n')
            archivo.anadir_contenido('Añadiendo una nueva línea al archivo.\n')
            archivo.sobrescribir_inicio('Sobrescribiendo el inicio del archivo.\n')
            archivo.obtener_posicion_cursor(10)
            archivo.leer_linea_por_linea()
            archivo.leer_todas_las_lineas()
            archivo.escribir_multiples_lineas([
                'Primera línea.\n',
                'Segunda línea.\n',
                'Tercera línea.\n'
            ])
        elif opcion == 7:
            break


menu()


#para comentar control + k + c
#para descomentar control + k + u

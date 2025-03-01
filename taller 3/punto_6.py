class ArchivoEjemplo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer_archivo(self):
        with open(self.nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)

    def escribir_archivo(self, contenido):
        with open(self.nombre_archivo, 'w') as archivo:
            archivo.write(contenido)

    def anadir_contenido(self, contenido):
        with open(self.nombre_archivo, 'a') as archivo:
            archivo.write(contenido)

    def sobrescribir_inicio(self, contenido):
        with open(self.nombre_archivo, 'r+') as archivo:
            archivo.seek(0)
            archivo.write(contenido)
            archivo.seek(0)
            contenido = archivo.read()
            print(contenido)

    def obtener_posicion_cursor(self, posicion):
        with open(self.nombre_archivo, 'r') as archivo:
            archivo.seek(posicion)
            posicion_actual = archivo.tell()
            print(f'La posición actual del cursor es: {posicion_actual}')

    def leer_linea_por_linea(self):
        with open(self.nombre_archivo, 'r') as archivo:
            linea = archivo.readline()
            while linea:
                print(linea, end='')
                linea = archivo.readline()

    def leer_todas_las_lineas(self):
        with open(self.nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                print(linea, end='')

    def escribir_multiples_lineas(self, lineas):
        with open(self.nombre_archivo, 'w') as archivo:
            archivo.writelines(lineas)


# # Ejemplo de uso de la clase
# archivo = ArchivoEjemplo('archivo_ejemplo.txt')
# archivo.leer_archivo()
# archivo.escribir_archivo('Este es un ejemplo de escritura con la sentencia with.\n')
# archivo.anadir_contenido('Añadiendo una nueva línea al archivo.\n')
# archivo.sobrescribir_inicio('Sobrescribiendo el inicio del archivo.\n')
# archivo.obtener_posicion_cursor(10)
# archivo.leer_linea_por_linea()
# archivo.leer_todas_las_lineas()
# archivo.escribir_multiples_lineas([
#     'Primera línea.\n',
#     'Segunda línea.\n',
#     'Tercera línea.\n'
# ])

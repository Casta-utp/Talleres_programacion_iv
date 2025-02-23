from io import *

class Lista:

    lista = []

    digitos = []

    def llenar_lista(self):
        while True:
            try:
                elemento = int(input("Ingrese un numero, presione 0 para finalizar: "))
                if 10 <= elemento <= 99:
                    self.lista.append(elemento)
                if elemento < 10 or elemento > 99:
                    print("Por favor, ingrese un número entre 10 y 99.")
                if elemento == 0:
                    break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        return self.lista
    
    def sumar_digitos(self):
        for i in self.lista:
            self.digitos.append(i//10 + i%10)
        return self.digitos
    
    def guardar_ambas_listas(self):
        with open("datos_ejercicio_1.txt", "w") as file:
            file.write(f"Lista completa: {self.lista}\n")
            file.write(f"Lista de digitos: {self.digitos}\n")
        print("Datos guardados...")


class Lista_usuario:

    lista_usuario = []

    conteo = {}

    def incluir_usuarios(self):
        while True:
            ingresar = input("Ingrese un usuario: ")
            if ingresar:
                self.lista_usuario.append(ingresar)
            else:
                break
        return self.lista_usuario

    def conteo_usuario(self):
        for usuario in self.lista_usuario:
            if usuario in self.conteo:
                self.conteo[usuario] += 1
            else:
                self.conteo[usuario] = 1
        return self.conteo
    
    def impar_par(self):
        for i in self.conteo:
            if self.conteo[i] % 2 == 0:
                print(f"El usuario {i} tiene un número par de repeticiones.")
            else:
                print(f"El usuario {i} tiene un número impar de repeticiones.")
    
    def guardar_usuarios(self):
        with open("datos_ejercicio_2.txt", "w") as file:
            file.write(f"Usuarios: {self.lista_usuario}\n")
            file.write(f"Conteo de usuarios: {self.conteo}\n")
        print("Datos guardados...")


class Ordenar_lista:

    lista_palabras = []

    lista_ordenada = []

    def llenar_lista(self):
        while True:
            ingresar = input("Ingrese una palabra, presione enter para finalizar: ")
            if ingresar:
                self.lista_palabras.append(ingresar)
            elif not ingresar and len(self.lista_palabras) < 15: 
                print("Por favor, la lista debe tener al menos 15 palabras.")
            else:
                break
        return self.lista_palabras

    def ordenar_palabras(self):
        for i in self.lista_palabras:
            if len(i) % 2 == 0:
                self.lista_ordenada.append(i)
        for i in self.lista_palabras:
            if len(i) % 2 != 0:
                self.lista_ordenada.append(i)
        return self.lista_ordenada
    
    def guardar_lista(self):
        with open("datos_ejercicio_3.txt", "w") as file:
            file.write(f"Lista de palabras: {self.lista_palabras}\n")
            file.write(f"Lista de palabras ordenadas: {self.lista_ordenada}\n")
        print("Datos guardados...")

class Libro:

    id = 0
    titulo = ""
    autor = ""
    editorial = ""
    precio = 0

    def ingresar_datos(self):
        self.id = int(input("Ingrese el ID del libro: "))
        self.titulo = input("Ingrese el título del libro: ")
        self.autor = input("Ingrese el autor del libro: ")
        self.editorial = input("Ingrese la editorial del libro: ")
        self.precio = int(input("Ingrese el precio del libro: "))
        return self.id, self.titulo, self.autor, self.editorial, self.precio

    def precio_iva(self):
        return self.precio * 1.19
    
    def guardar_datos(self):
        with open("datos_libro.txt", "w") as file:
            file.write(f"ID: {self.id}\n")
            file.write(f"Título: {self.titulo}\n")
            file.write(f"Autor: {self.autor}\n")
            file.write(f"Editorial: {self.editorial}\n")
            file.write(f"Precio: {self.precio}\n")
            file.write(f"Precio con IVA: {self.precio_iva()}\n")
        print("Datos guardados...")

class Casa:

    direccion = ""
    ciudad = ""
    valor = 0
    estrato = 0
    area = 0

    def ingresar_datos(self):
        self.direccion = input("Ingrese la dirección de la casa: ")
        self.ciudad = input("Ingrese la ciudad de la casa: ")
        self.valor = int(input("Ingrese el valor de la casa: "))
        self.estrato = int(input("Ingrese el estrato de la casa: "))
        self.area = int(input("Ingrese el área de la casa en metros cuadrados: "))
        return self.direccion, self.ciudad, self.valor, self.estrato, self.area
    
    def valor_metro(self):
        print(f"El valor por metro cuadrado de la casa es de ${self.valor/self.area}.")

    def subsidio(self):
        if self.estrato == 1:
            print("La casa es elegible para un subsidio.")
        else:
            print("La casa no es elegible para un subsidio.")
    
    def pagar_impuestos(self):
        if self.valor > 100000000:
            print("Debe pagar impuestos.")
        else:
            print("No debe pagar impuestos.")
    
    def guardar_datos(self):
        with open("datos_casa.txt", "w") as file:
            file.write(f"Dirección: {self.direccion}\n")
            file.write(f"Ciudad: {self.ciudad}\n")
            file.write(f"Valor: {self.valor}\n")
            file.write(f"Estrato: {self.estrato}\n")
            file.write(f"Área: {self.area}\n")
        print("Datos guardados...")

class Pelicula:

    titulo = ""
    director = ""
    genero = ""
    duracion = 0
    año = 0
    puntuacion = 0

    def ingresar_datos(self):
        self.titulo = input("Ingrese el título de la película: ")
        self.director = input("Ingrese el director de la película: ")
        self.genero = input("Ingrese el género de la película: ")
        self.duracion = int(input("Ingrese la duración de la película en minutos: "))
        self.año = int(input("Ingrese el año de la película: "))
        self.puntuacion = int(input("Ingrese la puntuación de la película: "))
        return self.titulo, self.director, self.genero, self.duracion, self.año

    def duracion_horas(self):
        horas = self.duracion // 60
        minutos = self.duracion % 60
        print(f"La duración de la película es de {horas} horas y {minutos} minutos.")
    
    def es_clasico(self):
        if self.año < 2000:
            print("La película es un clásico.")
        else:
            print("La película no es un clásico.")

    def puntaje(self):
        if self.puntuacion > 5:
            print("La película es buena.")
        else:
            print("La película es mala.")

    def guardar_datos(self):
        with open("datos_pelicula.txt", "w") as file:
            file.write(f"Título: {self.titulo}\n")
            file.write(f"Director: {self.director}\n")
            file.write(f"Género: {self.genero}\n")
            file.write(f"Duración: {self.duracion}\n")
            file.write(f"Año: {self.año}\n")
            file.write(f"Puntuación: {self.puntuacion}\n")
        print("Datos guardados...")
    
class Bodega:

    inventario = {}
    nombre = ""
    ubicacion = ""
    capacidad = 0
    encargado = ""

    def ingresar_datos(self):
        self.nombre = input("Ingrese el nombre de la bodega: ")
        self.ubicacion = input("Ingrese la ubicación de la bodega: ")
        self.capacidad = int(input("Ingrese la capacidad de la bodega: "))
        self.encargado = input("Ingrese el nombre del encargado de la bodega: ")
        return self.nombre, self.ubicacion, self.capacidad, self.encargado
    
    def agregar_producto(self):
        while True:
            producto = input("Ingrese el nombre del producto: ")
            if producto:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                self.inventario[producto] = cantidad
            else:
                break
        return self.inventario
    
    def mostrar_inventario(self):
        for producto in self.inventario:
            print(f"{producto}: {self.inventario[producto]}")

    def guardar_datos(self):
        with open("datos_bodega.txt", "w") as file:
            file.write(f"Nombre: {self.nombre}\n")
            file.write(f"Ubicación: {self.ubicacion}\n")
            file.write(f"Capacidad: {self.capacidad}\n")
            file.write(f"Encargado: {self.encargado}\n")
            file.write(f"Inventario: {self.inventario}\n")
        print("Datos guardados...")
    
class Lampara:

    tipo = ""
    color = ""
    potencia = 0
    precio = 0
    encendida = False

    def ingresar_datos(self):
        self.tipo = input("Ingrese el tipo de lámpara: ")
        self.color = input("Ingrese el color de la lámpara: ")
        self.potencia = int(input("Ingrese la potencia de la lámpara: "))
        self.precio = int(input("Ingrese el precio de la lámpara: "))
        return self.tipo, self.color, self.potencia, self.precio
    
    def encender(self):
        self.encendida = True
        print("La lámpara está encendida.")

    def apagar(self):
        self.encendida = False
        print("La lámpara está apagada.")

    def guardar_datos(self):
        with open("datos_lampara.txt", "w") as file:
            file.write(f"Tipo: {self.tipo}\n")
            file.write(f"Color: {self.color}\n")
            file.write(f"Potencia: {self.potencia}\n")
            file.write(f"Precio: {self.precio}\n")
            file.write(f"Encendida: {self.encendida}\n")
        print("Datos guardados...")

class Modem:

    marca = ""
    modelo = ""
    velocidad = 0
    precio = 0
    encendido = False

    def ingresar_datos(self):
        self.marca = input("Ingrese la marca del modem: ")
        self.modelo = input("Ingrese el modelo del modem: ")
        self.velocidad = int(input("Ingrese la velocidad del modem: "))
        self.precio = int(input("Ingrese el precio del modem: "))
        return self.marca, self.modelo, self.velocidad, self.precio

    def encender(self):
        self.encendido = True
        print("El modem está encendido.")

    def apagar(self):
        self.encendido = False
        print("El modem está apagado.")

    def guardar_datos(self):
        with open("datos_modem.txt", "w") as file:
            file.write(f"Marca: {self.marca}\n")
            file.write(f"Modelo: {self.modelo}\n")
            file.write(f"Velocidad: {self.velocidad}\n")
            file.write(f"Precio: {self.precio}\n")
            file.write(f"Encendido: {self.encendido}\n")
        print("Datos guardados...")

class Router:

    marca = ""
    modelo = ""
    velocidad = 0
    precio = 0
    dispositivos_conectados = 0

    def ingresar_datos(self):
        self.marca = input("Ingrese la marca del router: ")
        self.modelo = input("Ingrese el modelo del router: ")
        self.velocidad = int(input("Ingrese la velocidad del router: "))
        self.precio = int(input("Ingrese el precio del router: "))
        self.dispositivos_conectados = int(input("Ingrese el número de dispositivos conectados: "))
        return self.marca, self.modelo, self.velocidad, self.precio, self.dispositivos_conectados

    def conectar_dispositivo(self):
        self.dispositivos_conectados += 1
        print(f"Dispositivo conectado. Total de dispositivos: {self.dispositivos_conectados}")

    def desconectar_dispositivo(self):
        if self.dispositivos_conectados > 0:
            self.dispositivos_conectados -= 1
            print(f"Dispositivo desconectado. Total de dispositivos: {self.dispositivos_conectados}")
        else:
            print("No hay dispositivos para desconectar.")

    def guardar_datos(self):
        with open("datos_router.txt", "w") as file:
            file.write(f"Marca: {self.marca}\n")
            file.write(f"Modelo: {self.modelo}\n")
            file.write(f"Velocidad: {self.velocidad}\n")
            file.write(f"Precio: {self.precio}\n")
            file.write(f"Dispositivos conectados: {self.dispositivos_conectados}\n")
        print("Datos guardados...")

class Maletin:

    contenido = {}
    espacio = 0
    peso = 0
    color = ""
    cerrado = True

    def ingresar_datos(self):
        self.espacio = int(input("Ingrese el espacio del maletín: "))
        self.peso = int(input("Ingrese el peso del maletín: "))
        self.color = input("Ingrese el color del maletín: ")
        return self.espacio, self.peso, self.color

    def agregar_objeto(self):
        if self.cerrado:
            print("El maletín está cerrado. No se puede agregar nada.")
            return self.contenido
        
        while True:
            objeto = input("Ingrese el nombre del objeto: ")
            if objeto:
                peso_objeto = int(input("Ingrese el peso del objeto: "))
                if peso_objeto + self.peso > self.espacio:
                    print("No hay espacio suficiente.")
                else:
                    self.contenido[objeto] = peso_objeto
                    self.peso += peso_objeto
            else:
                break
        return self.contenido
    
    def cerrar_maletin(self):
        self.cerrado = True
    
    def abrir_maletin(self):
        self.cerrado = False
    
    def guardar_datos(self):
        with open("datos_maletin.txt", "w") as file:
            file.write(f"Espacio: {self.espacio}\n")
            file.write(f"Peso: {self.peso}\n")
            file.write(f"Color: {self.color}\n")
            file.write(f"Contenido: {self.contenido}\n")
            file.write(f"Cerrado: {self.cerrado}\n")
        print("Datos guardados...")
    
class Paciente_oncologico:

    nombre = ""
    edad = 0
    diagnostico = ""
    tratamiento = False
    fecha = ""
    etapa = 0

    def ingresar_datos(self):
        self.nombre = input("Ingrese el nombre del paciente: ")
        self.edad = int(input("Ingrese la edad del paciente: "))
        self.diagnostico = input("Ingrese el diagnóstico del paciente: ")
        self.tratamiento = input("Ingrese el tratamiento del paciente: ")
        self.fecha = input("Ingrese la fecha de la consulta: ")
        self.etapa = int(input("Ingrese la etapa del paciente: "))
        return self.nombre, self.edad, self.diagnostico, self.tratamiento, self.fecha

    def tratamiento_aplicado(self):
        self.tratamiento = True
        print("Tratamiento aplicado.")
    
    def tiempo_tratamiento(self):
        if self.tratamiento:
            print("El paciente lleva en tratamiento.")
        else:
            print("El paciente no lleva en tratamiento.")
    
    def tiempo_vida(self):
        if self.etapa == 1:
            print("El paciente tiene una esperanza de vida de 5 años.")
        elif self.etapa == 2:
            print("El paciente tiene una esperanza de vida de 3 años.")
        elif self.etapa == 3:
            print("El paciente tiene una esperanza de vida de 1 año.")
        elif self.etapa == 4:
            print("El paciente tiene una esperanza de vida de 6 meses.")
    
    def guardar_datos(self):
        with open("datos_paciente.txt", "w") as file:
            file.write(f"Nombre: {self.nombre}\n")
            file.write(f"Edad: {self.edad}\n")
            file.write(f"Diagnóstico: {self.diagnostico}\n")
            file.write(f"Tratamiento: {self.tratamiento}\n")
            file.write(f"Fecha: {self.fecha}\n")
        print("Datos guardados...")

class Gato:

    nombre = ""
    raza = ""
    edad = 0
    peso = 0
    vacunas = False

    def ingresar_datos(self):
        self.nombre = input("Ingrese el nombre del gato: ")
        self.raza = input("Ingrese la raza del gato: ")
        self.edad = int(input("Ingrese la edad del gato: "))
        self.peso = int(input("Ingrese el peso del gato: "))
        self.vacunas = input("Ingrese si el gato tiene vacunas: ")
        return self.nombre, self.raza, self.edad, self.peso, self.vacunas
    
    def vacunar(self):
        self.vacunas = True
        print("Gato vacunado.")
    
    def alimentar(self):
        if self.peso < 5:
            print("El gato está bajo de peso.")
        elif 5 <= self.peso <= 10:
            print("El gato tiene un peso normal.")
        else:
            print("El gato tiene sobrepeso.")
    
    def guardar_datos(self):
        with open("datos_gato.txt", "w") as file:
            file.write(f"Nombre: {self.nombre}\n")
            file.write(f"Raza: {self.raza}\n")
            file.write(f"Edad: {self.edad}\n")
            file.write(f"Peso: {self.peso}\n")
            file.write(f"Vacunas: {self.vacunas}\n")
        print("Datos guardados...")
    
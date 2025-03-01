class Avion:

    def __init__(self):
        self.modelo = ""
        self.capacidad = 0
        self.velocidad = 0
        self.altura = 0
        self.peso = 0
        self.combustible = 0
        self.bodega = []

    def __str__(self):
        return f"Modelo: {self.modelo}, Capacidad: {self.capacidad}, Velocidad: {self.velocidad}, Altura: {self.altura}, Peso: {self.peso}, Combustible: {self.combustible}"
    
    def llenar_datos(self):
        self.modelo = input("Ingrese el modelo del avion: ")
        self.capacidad = int(input("Ingrese la capacidad del avion (kg): "))
        self.velocidad = int(input("Ingrese la velocidad del avion: "))
        self.altura = int(input("Ingrese la altura del avion: "))
        self.peso = int(input("Ingrese el peso del avion: "))
        self.combustible = int(input("Ingrese el combustible del avion: "))

    def cargar_bodega(self):
        while True:
            carga = input("Ingrese la carga que desea agregar a la bodega: ")
            self.bodega.append(carga)
            peso = int(input("Ingrese el peso de la carga: "))
            self.peso += peso
            continuar = input("Desea agregar otra carga? (s/n): ")
            if continuar.lower() == "n":
                break
            else:
                if self.peso > self.capacidad:
                    print("El peso de la carga excede el limite permitido.")
                    break
    
# avion = Avion()
# avion.llenar_datos()
# avion.cargar_bodega()
# print(avion)

class Celular:

    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.color = ""
        self.precio = 0
        self.camara = ""
        self.memoria = ""
        self.bateria = 0
        self.aplicaciones = []

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}, Camara: {self.camara}, Memoria: {self.memoria}, Bateria: {self.bateria}"
    
    def llenar_datos(self):
        self.marca = input("Ingrese la marca del celular: ")
        self.modelo = input("Ingrese el modelo del celular: ")
        self.color = input("Ingrese el color del celular: ")
        self.precio = int(input("Ingrese el precio del celular: "))
        self.camara = input("Ingrese la camara del celular: ")
        self.memoria = input("Ingrese la memoria del celular: ")
        self.bateria = int(input("Ingrese la bateria del celular: "))

    def instalar_aplicacion(self):
        while True:
            aplicacion = input("Ingrese la aplicacion que desea instalar: ")
            self.aplicaciones.append(aplicacion)
            continuar = input("Desea instalar otra aplicacion? (s/n): ")
            if continuar.lower() == "n":
                break
    
    def desinstalar_aplicacion(self):
        while True:
            aplicacion = input("Ingrese la aplicacion que desea desinstalar: ")
            self.aplicaciones.remove(aplicacion)
            continuar = input("Desea desinstalar otra aplicacion? (s/n): ")
            if continuar.lower() == "n":
                break

    def mostrar_aplicaciones(self):
        for aplicacion in self.aplicaciones:
            print(aplicacion)
    

class Asignatura:
    
    def __init__(self):
        self.nombre = ""
        self.codigo = ""
        self.creditos = 0
        self.docente = ""
        self.estudiantes = []
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}, Creditos: {self.creditos}, Docente: {self.docente}"
    
    def llenar_datos(self):
        self.nombre = input("Ingrese el nombre de la asignatura: ")
        self.codigo = input("Ingrese el codigo de la asignatura: ")
        self.creditos = int(input("Ingrese los creditos de la asignatura: "))
        self.docente = input("Ingrese el docente de la asignatura: ")

    def inscribir_estudiante(self):
        while True:
            estudiante = input("Ingrese el nombre del estudiante que desea inscribir: ")
            self.estudiantes.append(estudiante)
            continuar = input("Desea inscribir otro estudiante? (s/n): ")
            if continuar.lower() == "n":
                break
    
    def retirar_estudiante(self):
        while True:
            estudiante = input("Ingrese el nombre del estudiante que desea retirar: ")
            self.estudiantes.remove(estudiante)
            continuar = input("Desea retirar otro estudiante? (s/n): ")
            if continuar.lower() == "n":
                break

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)

class Ejercito:
    
    def __init__(self):
        self.nombre = ""
        self.pais = ""
        self.comandante = ""
        self.soldados = []
        self.armas = []
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Pais: {self.pais}, Comandante: {self.comandante}" 
    
    def llenar_datos(self):
        self.nombre = input("Ingrese el nombre del ejercito: ")
        self.pais = input("Ingrese el pais del ejercito: ")
        self.comandante = input("Ingrese el comandante del ejercito: ")

    def reclutar_soldado(self):
        while True:
            soldado = input("Ingrese el nombre del soldado que desea reclutar: ")
            self.soldados.append(soldado)
            continuar = input("Desea reclutar otro soldado? (s/n): ")
            if continuar.lower() == "n":
                break
    
    def despedir_soldado(self):
        while True:
            soldado = input("Ingrese el nombre del soldado que desea despedir: ")
            self.soldados.remove(soldado)
            continuar = input("Desea despedir otro soldado? (s/n): ")
            if continuar.lower() == "n":
                break

    def armar_ejercito(self):
        while True:
            arma = input("Ingrese el nombre del arma que desea agregar: ")
            self.armas.append(arma)
            continuar = input("Desea agregar otra arma? (s/n): ")
            if continuar.lower() == "n":
                break
    
    def mostrar_soldados(self):
        for soldado in self.soldados:
            print(soldado)

    def mostrar_armas(self):
        for arma in self.armas:
            print(arma)

class Silla:
    
    def __init__(self):
        self.material = ""
        self.color = ""
        self.peso = 0
        self.precio = 0
        self.tipo = ""
    
    def __str__(self):
        return f"Material: {self.material}, Color: {self.color}, Peso: {self.peso}, Precio: {self.precio}, Tipo: {self.tipo}"
    
    def llenar_datos(self):
        self.material = input("Ingrese el material de la silla: ")
        self.color = input("Ingrese el color de la silla: ")
        self.peso = int(input("Ingrese el peso de la silla: "))
        self.precio = int(input("Ingrese el precio de la silla: "))
        self.tipo = input("Ingrese el tipo de la silla: ")

    def mostrar_pais(self):
        if self.material == "madera":
            print("La silla es de origen nacional")
        elif self.material == "metal":
            print("La silla es de origen chino")
        else:
            print("La silla es de origen desconocido")

    def precio_iva(self):
        iva = self.precio * 0.19
        precio_total = self.precio + iva
        print(f"El precio total de la silla es: {precio_total}")
    
    def agregar_descuento(self):
        descuento = int(input("Ingrese el descuento que desea aplicar: "))
        precio_descuento = self.precio_iva - descuento
        print(f"El precio de la silla con descuento es: {precio_descuento}")
    
class Audifonos:
    
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.color = ""
        self.precio = 0
        self.tipo = ""
        self.conexion = ""
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}, Tipo: {self.tipo}, Conexion: {self.conexion}"
    
    def llenar_datos(self):
        self.marca = input("Ingrese la marca de los audifonos: ")
        self.modelo = input("Ingrese el modelo de los audifonos: ")
        self.color = input("Ingrese el color de los audifonos: ")
        self.precio = int(input("Ingrese el precio de los audifonos: "))
        self.tipo = input("Ingrese el tipo de los audifonos: ")
        self.conexion = input("Ingrese la conexion de los audifonos: ")

    def mostrar_marca(self):
        if self.marca == "sony":
            print("Los audifonos son de alta calidad")
        elif self.marca == "samsung":
            print("Los audifonos son de calidad media")
        else:
            print("Los audifonos son de baja calidad")
    
    def mostrar_tipo(self):
        if self.tipo == "in-ear":
            print("Los audifonos son pequeños")
        elif self.tipo == "on-ear":
            print("Los audifonos son medianos")
        else:
            print("Los audifonos son grandes")
    
    def mostrar_conexion(self):
        if self.conexion == "bluetooth":
            print("Los audifonos son inalambricos")
        else:
            print("Los audifonos son alambricos")
    





                

    
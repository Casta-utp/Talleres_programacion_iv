class PersonalUniversitario:

    listaPersonal = []
    
    def __init__(self, nombre, edad, fechaIngreso):
        self.nombre = nombre
        self.edad = edad
        self.fechaIngreso = fechaIngreso

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de Ingreso: {self.fechaIngreso}"
    
    def antiguedad(self, fechaIngreso):
        fechaActual = 2025
        antiguedad = fechaActual - fechaIngreso
        return antiguedad
    
    def llenar_lista_personal():
        while True:
            print("\nSeleccione el tipo de personal a agregar:")
            print("1. Profesor")
            print("2. Alumno")
            print("3. Profesor Ayudante")
            print("4. Salir")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                fechaIngreso = int(input("Fecha de Ingreso: "))
                tipo = input("Tipo (Catedratico/De planta/Ocasional): ")
                horas = int(input("Horas: "))
                profesor = Profesor(nombre, edad, fechaIngreso, tipo, horas)
                PersonalUniversitario.listaPersonal.append(profesor)

            elif opcion == "2":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                fechaIngreso = int(input("Fecha de Ingreso: "))
                carrera = input("Carrera: ")
                semestre = int(input("Semestre: "))
                materias = input("Materias (separadas por coma): ").split(", ")
                alumno = Alumno(nombre, edad, fechaIngreso, carrera, semestre, materias)
                PersonalUniversitario.listaPersonal.append(alumno)

            elif opcion == "3":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                fechaIngreso = int(input("Fecha de Ingreso: "))
                tipo = input("Tipo (Catedratico/De planta/Ocasional): ")
                horas = int(input("Horas: "))
                carrera = input("Carrera: ")
                semestre = int(input("Semestre: "))
                materias = input("Materias (separadas por coma): ").split(", ")
                profesor_ayudante = ProfesorAyudante(nombre, edad, fechaIngreso, tipo, horas, carrera, semestre, materias)
                PersonalUniversitario.listaPersonal.append(profesor_ayudante)

            elif opcion == "4":
                print("Saliendo...")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

    def guardar_lista_personal():
        with open("personal.txt", "w") as archivo:
            for personal in PersonalUniversitario.listaPersonal:
                archivo.write(str(personal) + "\n")


    
class Profesor(PersonalUniversitario):
    def __init__(self, nombre, edad, fechaIngreso, tipo, horas):
        super().__init__(nombre, edad, fechaIngreso)
        self.tipo = tipo
        self.horas = horas

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de Ingreso: {self.fechaIngreso}, Tipo: {self.tipo}, Horas: {self.horas}"
    
    def sueldo(self):
        sueldo = 0
        if self.tipo == "Catedratico":
            sueldo = 18000 * self.horas
        elif self.tipo == "De planta":
            sueldo = 30000 * self.horas
        elif self.tipo == "Ocasional":
            sueldo = 15000 * self.horas
        return sueldo
    
    def materias(self):
        if self.tipo == "Catedratico":
            return ["Matemáticas Avanzadas", "Física Cuántica", "Inteligencia Artificial"]
        elif self.tipo == "De planta":
            return ["Programación", "Bases de Datos", "Redes de Computadoras"]
        elif self.tipo == "Ocasional":
            return ["Introducción a la Informática", "Matemáticas Básicas", "Estadística"]
        else:
            return ["No se han asignado materias para este tipo de profesor"]
        
class Alumno(PersonalUniversitario):
    def __init__(self, nombre, edad, fechaIngreso, carrera, semestre, materias):
        super().__init__(nombre, edad, fechaIngreso)
        self.carrera = carrera
        self.semestre = semestre
        self.materias = materias

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de Ingreso: {self.fechaIngreso}, Carrera: {self.carrera}, Semestre: {self.semestre}, Materias: {self.materias}"
    
    def materias(self):
        if self.semestre == 1:
            return ["Matemáticas Básicas", "Introducción a la Informática", "Estadística"]
        elif self.semestre == 2:
            return ["Programación", "Bases de Datos", "Redes de Computadoras"]
        elif self.semestre == 3:
            return ["Matemáticas Avanzadas", "Física Cuántica", "Inteligencia Artificial"]
        else:
            return ["No se han asignado materias para este semestre"]
        
    def promedio(self):
        materias = self.materias
        promedio = 0
        for materia in materias:
            promedio += materia
        promedio = promedio / len(materias)
        return promedio
    
class ProfesorAyudante (Profesor, Alumno):
    def __init__(self, nombre, edad, fechaIngreso, tipo, horas, carrera, semestre, materias):
        Profesor.__init__(self, nombre, edad, fechaIngreso, tipo, horas)
        Alumno.__init__(self, nombre, edad, fechaIngreso, carrera, semestre, materias)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de Ingreso: {self.fechaIngreso}, Tipo: {self.tipo}, Horas: {self.horas}, Carrera: {self.carrera}, Semestre: {self.semestre}, Materias: {self.materias}"
    
    def materias(self):
        if self.tipo == "Catedratico":
            return ["Matemáticas Avanzadas", "Física Cuántica", "Inteligencia Artificial"]
        elif self.tipo == "De planta":
            return ["Programación", "Bases de Datos", "Redes de Computadoras"]
        elif self.tipo == "Ocasional":
            return ["Introducción a la Informática", "Matemáticas Básicas", "Estadística"]
        else:
            return ["No se han asignado materias para este tipo de profesor"]
        
    def promedio(self):
        materias = self.materias
        promedio = 0
        for materia in materias:
            promedio += materia
        promedio = promedio / len(materias)
        return promedio

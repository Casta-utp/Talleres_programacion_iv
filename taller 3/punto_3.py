class Empleado:

    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.sexo = ""
        self.cargo = ""
        self.edad = 0
        self.antiguedad = 0
        self.tiempo_pension = 0
        self.semanas_cotizadas = 0
        self.salario_total = 0
        self.valor_hora = 0
        self.horas_trabajadas = 0
        self.pension = 0
        self.pension_año = 0
        self.salud = 0
        self.semanas_faltantes = 0

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Sexo: {self.sexo}, Cargo: {self.cargo}, Antiguedad: {self.antiguedad}, Salario total: {self.salario_total}, Pension: {self.pension}, Salud: {self.salud}, Pension anual: {self.pension_año}, Semanas faltantes cotizadas: {self.semanas_faltantes}, Tiempo pension: {self.tiempo_pension}"
    
    def llenar_datos(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.apellido = input("Ingrese el apellido del empleado: ")
        self.sexo = input("Ingrese el sexo del empleado: ")
        self.cargo = input("Ingrese el cargo del empleado: ")
        self.edad = int(input("Ingrese la edad del empleado: "))
        self.antiguedad = int(input("Ingrese la antiguedad del empleado: "))
        self.valor_hora = int(input("Ingrese el valor por hora de trabajo: "))
        self.horas_trabajadas = int(input("Ingrese las horas trabajadas del empleado: "))
        self.semanas_cotizadas = int(input("Ingrese las semanas cotizadas del empleado: "))

    def calcular_salario(self):
        self.salario_total = self.valor_hora * self.horas_trabajadas
        if self.antiguedad > 0:
            self.salario_total += self.salario_total * (self.antiguedad * 0.05)
        if self.salario_total > 1000000:
            self.pension = self.salario_total * 0.04
            self.salud = self.salario_total * 0.04
            self.salario_total -= self.pension + self.salud

    def calcular_tiempo_pension(self):
        if self.sexo == "masculino":
            self.tiempo_pension = 62 - self.antiguedad + self.edad
            self.semanas_faltantes = 1200 - self.semanas_cotizadas
        elif self.sexo == "femenino":
            self.tiempo_pension = 57 - self.antiguedad + self.edad 
            self.semanas_faltantes = 1200 - self.semanas_cotizadas
    
    def calcular_pension_salud(self):
        self.pension = self.salario_total * 0.04
        self.salud = self.salario_total * 0.04
        self.pension_año = self.pension * 12
    
    def guardar_datos(self):
        with open("empleados.txt", "a") as archivo:
            archivo.write(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Sexo: {self.sexo}, Cargo: {self.cargo}, Antiguedad (años): {self.antiguedad}\n, Salario total: {self.salario_total}, Pension: {self.pension}, Salud: {self.salud}, Pension anual: {self.pension_año}\n, Semanas faltantes cotizadas: {self.semanas_faltantes}, Tiempo pension (años): {self.tiempo_pension}\n")




    

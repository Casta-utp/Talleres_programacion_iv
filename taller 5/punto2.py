class Taller:

    def __init__(self, nombre, direccion, telefono, lista_pacientes):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"    
    
    def guardar_talleres(talleres):
        with open(r"C:\Users\Santi\Desktop\CUARTO SEMESTRE\Progra IV\Talleres\taller 5\archivos\talleres.txt", "w") as file:
            for taller in talleres:
                file.write(f"{taller.nombre},{taller.direccion},{taller.telefono}\n")
        print("Lista de talleres guardada exitosamente.")

    def guardar_empleados(empleados):
        with open(r"C:\Users\Santi\Desktop\CUARTO SEMESTRE\Progra IV\Talleres\taller 5\archivos\empleados.txt", "w") as file:
            for empleado in empleados:
                file.write(f"{empleado.nombre_empleado},{empleado.edad_empleado},{empleado.fecha_ingreso},{empleado.salario}\n")
        print("Lista de empleados guardada exitosamente.")

    def guardar_carros(carros):
        with open(r"C:\Users\Santi\Desktop\CUARTO SEMESTRE\Progra IV\Talleres\taller 5\archivos\carros.txt", "w") as file:
            for carro in carros:
                file.write(f"{carro.marca},{carro.modelo},{carro.color},{carro.placa}\n")
        print("Lista de carros guardada exitosamente.")

    def guardar_clientes(clientes):
        with open(r"C:\Users\Santi\Desktop\CUARTO SEMESTRE\Progra IV\Talleres\taller 5\archivos\clientes.txt", "w") as file:
            for cliente in clientes:
                file.write(f"{cliente.nombre_cliente},{cliente.edad_cliente},{cliente.telefono_cliente}\n")
        print("Lista de clientes guardada exitosamente.")
    
class Empleados(Taller):
    
    def __init__(self, nombre, direccion, telefono, lista_pacientes, nombre_empleado, edad_empleado, fecha_ingreso, salario):
        super().__init__(nombre, direccion, telefono, lista_pacientes)
        self.nombre_empleado = nombre_empleado
        self.edad_empleado = edad_empleado
        self.fecha_ingreso = fecha_ingreso
        self.salario = salario

    def __str__(self):
        return f"Nombre: {self.nombre_empleado}, Edad: {self.edad_empleado}, Fecha de Ingreso: {self.fecha_ingreso}, Salario: {self.salario}"
    
    def antiguedad(self, fecha_ingreso):
        fecha_actual = 2025
        antiguedad = fecha_actual - fecha_ingreso
        return antiguedad
    
class Mecanico(Empleados):
    
    def __init__(self, nombre, direccion, telefono, lista_pacientes, nombre_empleado, edad_empleado, fecha_ingreso, salario, especialidad, horas):
        super().__init__(nombre, direccion, telefono, lista_pacientes, nombre_empleado, edad_empleado, fecha_ingreso, salario)
        self.especialidad = especialidad
        self.horas = horas

    def __str__(self):
        return f"Nombre: {self.nombre_empleado}, Edad: {self.edad_empleado}, Fecha de Ingreso: {self.fecha_ingreso}, Salario: {self.salario}, Especialidad: {self.especialidad}, Horas: {self.horas}"
    
    def calcular_salario(self, salario, horas):
        salario_total = salario * horas
        return salario_total
    
class Recepcionista(Empleados):
    
    def __init__(self, nombre, direccion, telefono, lista_pacientes, nombre_empleado, edad_empleado, fecha_ingreso, salario, turno):
        super().__init__(nombre, direccion, telefono, lista_pacientes, nombre_empleado, edad_empleado, fecha_ingreso, salario)
        self.turno = turno

    def __str__(self):
        return f"Nombre: {self.nombre_empleado}, Edad: {self.edad_empleado}, Fecha de Ingreso: {self.fecha_ingreso}, Salario: {self.salario}, Turno: {self.turno}"
    
    def calcular_salario(self, salario, horas):
        salario_total = salario * horas
        return salario_total
    
class Gerente(Empleados):
    
    def __init__(self, nombre, direccion, telefono, lista_pacientes, nombre_empleado, edad_empleado, fecha_ingreso, salario, bono):
        super().__init__(nombre, direccion, telefono, lista_pacientes, nombre_empleado, edad_empleado, fecha_ingreso, salario)
        self.bono = bono

    def __str__(self):
        return f"Nombre: {self.nombre_empleado}, Edad: {self.edad_empleado}, Fecha de Ingreso: {self.fecha_ingreso}, Salario: {self.salario}, Bono: {self.bono}"
    
    def calcular_salario(self, salario, bono):
        salario_total = salario + bono
        return salario_total
    
class Carros(Taller):
    
    def __init__(self, nombre, direccion, telefono, lista_pacientes, marca, modelo, color, placa):
        super().__init__(nombre, direccion, telefono, lista_pacientes)
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.placa = placa

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Placa: {self.placa}"
    
    def calcular_costo(self, costo, horas):
        costo_total = costo * horas
        return costo_total
    
class Clientes(Taller):
    
    def __init__(self, nombre, direccion, telefono, lista_pacientes, nombre_cliente, edad_cliente, telefono_cliente):
        super().__init__(nombre, direccion, telefono, lista_pacientes)
        self.nombre_cliente = nombre_cliente
        self.edad_cliente = edad_cliente
        self.telefono_cliente = telefono_cliente

    def __str__(self):
        return f"Nombre: {self.nombre_cliente}, Edad: {self.edad_cliente}, Teléfono: {self.telefono_cliente}"
    
    def solicitar_servicio(self, servicio):
        return f"El cliente {self.nombre_cliente} solicita el servicio de {servicio}"
    
    def solicitar_cita(self, fecha, hora):
        return f"El cliente {self.nombre_cliente} solicita una cita para el día {fecha} a las {hora}"
    
    def solicitar_presupuesto(self, descripcion):
        return f"El cliente {self.nombre_cliente} solicita un presupuesto para {descripcion}"
    
    def solicitar_informacion(self, informacion):
        return f"El cliente {self.nombre_cliente} solicita información sobre {informacion}"
    
    def solicitar_reparacion(self, descripcion):
        return f"El cliente {self.nombre_cliente} solicita la reparación de {descripcion}"
    
    def solicitar_revision(self, descripcion):
        return f"El cliente {self.nombre_cliente} solicita la revisión de {descripcion}"
    
    def solicitar_cambio(self, descripcion):
        return f"El cliente {self.nombre_cliente} solicita el cambio de {descripcion}"
    
    def solicitar_instalacion(self, descripcion):
        return f"El cliente {self.nombre_cliente} solicita la instalación de {descripcion}"
    
    def solicitar_mantenimiento(self, descripcion):
        return f"El cliente {self.nombre_cliente} solicita el mantenimiento de {descripcion}"
    
    def solicitar_asesoria(self, descripcion):
        return f"El cliente {self.nombre_cliente} solicita asesoría sobre {descripcion}"
    
    def solicitar_repuesto(self, descripcion):
        return f"El cliente {self.nombre_cliente} solicita el repuesto de {descripcion}"
    
    def solicitar_cambio_aceite(self, descripcion):
        return f"El cliente {self.nombre_cliente} solicita el cambio de aceite de {descripcion}"
    
class Bono(Mecanico, Recepcionista, Gerente):
    
    def __init__(self, nombre, direccion, telefono, lista_pacientes, nombre_empleado, edad_empleado, fecha_ingreso, salario, turno, especialidad, horas, bono):
        super().__init__(nombre, direccion, telefono, lista_pacientes, nombre_empleado, edad_empleado, fecha_ingreso, salario, especialidad, horas)
        self.turno = turno
        self.bono = bono

    def __str__(self):
        return f"Nombre: {self.nombre_empleado}, Edad: {self.edad_empleado}, Fecha de Ingreso: {self.fecha_ingreso}, Salario: {self.salario}, Turno: {self.turno}, Especialidad: {self.especialidad}, Horas: {self.horas}, Bono: {self.bono}"
    
    def calcular_salario(self, salario, horas, bono):
        salario_total = salario * horas + bono
        return salario_total
    
    def calcular_salario(self, salario, bono):
        salario_total = salario + bono
        return salario_total
    



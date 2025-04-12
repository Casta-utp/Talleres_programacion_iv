# clases.py

class Taller:
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return f"Nombre: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}"

    def guardar_talleres(self, talleres):
        with open("archivos/talleres.txt", "w") as file:
            for taller in talleres:
                file.write(f"{taller.get_nombre()},{taller.get_direccion()},{taller.get_telefono()}\n")
        print("Lista de talleres guardada exitosamente.")


class Empleados(Taller):
    def __init__(self, nombre, direccion, telefono, nombre_empleado, edad_empleado, fecha_ingreso, salario):
        super().__init__(nombre, direccion, telefono)
        self.__nombre_empleado = nombre_empleado
        self.__edad_empleado = edad_empleado
        self.__fecha_ingreso = fecha_ingreso
        self.__salario = salario

    def get_nombre_empleado(self):
        return self.__nombre_empleado

    def get_edad_empleado(self):
        return self.__edad_empleado

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def get_salario(self):
        return self.__salario

    def set_nombre_empleado(self, nombre):
        self.__nombre_empleado = nombre

    def set_edad_empleado(self, edad):
        self.__edad_empleado = edad

    def set_fecha_ingreso(self, fecha):
        self.__fecha_ingreso = fecha

    def set_salario(self, salario):
        self.__salario = salario

    def __str__(self):
        return f"Empleado: {self.__nombre_empleado}, Edad: {self.__edad_empleado}, Ingreso: {self.__fecha_ingreso}, Salario: {self.__salario}"


class Mecanico(Empleados):
    def __init__(self, nombre, direccion, telefono, nombre_empleado, edad_empleado, fecha_ingreso, salario, especialidad, horas):
        super().__init__(nombre, direccion, telefono, nombre_empleado, edad_empleado, fecha_ingreso, salario)
        self.__especialidad = especialidad
        self.__horas = horas

    def get_especialidad(self):
        return self.__especialidad

    def get_horas(self):
        return self.__horas

    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    def set_horas(self, horas):
        self.__horas = horas

    def calcular_salario(self):
        return self.get_salario() * self.__horas


class Recepcionista(Empleados):
    def __init__(self, nombre, direccion, telefono, nombre_empleado, edad_empleado, fecha_ingreso, salario, turno):
        super().__init__(nombre, direccion, telefono, nombre_empleado, edad_empleado, fecha_ingreso, salario)
        self.__turno = turno

    def mostrar_turno(self):
        return f"Turno: {self.__turno}"

    def get_turno(self):
        return self.__turno

    def set_turno(self, turno):
        self.__turno = turno

    def calcular_salario(self, horas):
        return self.get_salario() * horas


class Gerente(Empleados):
    def __init__(self, nombre, direccion, telefono, nombre_empleado, edad_empleado, fecha_ingreso, salario, bono):
        super().__init__(nombre, direccion, telefono, nombre_empleado, edad_empleado, fecha_ingreso, salario)
        self.__bono = bono

    def obtener_bono(self):
        return self.__bono

    def get_bono(self):
        return self.__bono

    def set_bono(self, bono):
        self.__bono = bono

    def calcular_salario(self):
        return self.get_salario() + self.__bono


class Bono(Empleados):
    def __init__(self, nombre, direccion, telefono, nombre_empleado, edad_empleado, fecha_ingreso, salario, especialidad, horas, turno, bono):
        super().__init__(nombre, direccion, telefono, nombre_empleado, edad_empleado, fecha_ingreso, salario)
        self.__especialidad = especialidad
        self.__horas = horas
        self.__turno = turno
        self.__bono = bono

    def mostrar_detalle_bono(self):
        return f"Empleado: {self.get_nombre_empleado()}, Especialidad: {self.__especialidad}, Horas: {self.__horas}, Turno: {self.__turno}, Bono: {self.__bono}"

    def calcular_salario_total(self):
        return (self.get_salario() * self.__horas) + self.__bono

    def get_turno(self):
        return self.__turno

    def get_especialidad(self):
        return self.__especialidad

    def get_bono(self):
        return self.__bono

    
class Carros(Taller):
    def __init__(self, nombre, direccion, telefono, marca, modelo, color, placa):
        super().__init__(nombre, direccion, telefono)
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__placa = placa

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_color(self):
        return self.__color

    def get_placa(self):
        return self.__placa

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_color(self, color):
        self.__color = color

    def set_placa(self, placa):
        self.__placa = placa

class Clientes(Taller):
    def __init__(self, nombre, direccion, telefono, nombre_cliente, edad_cliente, telefono_cliente):
        super().__init__(nombre, direccion, telefono)
        self.__nombre_cliente = nombre_cliente
        self.__edad_cliente = edad_cliente
        self.__telefono_cliente = telefono_cliente

    def get_nombre_cliente(self):
        return self.__nombre_cliente

    def get_edad_cliente(self):
        return self.__edad_cliente

    def get_telefono_cliente(self):
        return self.__telefono_cliente

    def set_nombre_cliente(self, nombre):
        self.__nombre_cliente = nombre

    def set_edad_cliente(self, edad):
        self.__edad_cliente = edad

    def set_telefono_cliente(self, telefono):
        self.__telefono_cliente = telefono

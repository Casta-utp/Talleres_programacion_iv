from clases import Taller, Empleados, Mecanico, Recepcionista, Gerente, Carros, Clientes, Bono

# Crear taller
taller = Taller("Taller Multiservicio", "Calle 123", "3216549870")

# Crear empleados
empleado1 = Empleados("Taller Multiservicio", "Calle 123", "3216549870", "Laura Torres", 33, 2019, 30000)
mecanico1 = Mecanico("Taller Multiservicio", "Calle 123", "3216549870", "Andrés Díaz", 29, 2021, 35000, "Motor", 180)
recepcionista1 = Recepcionista("Taller Multiservicio", "Calle 123", "3216549870", "Sara Méndez", 26, 2022, 25000, "Tarde")
gerente1 = Gerente("Taller Multiservicio", "Calle 123", "3216549870", "Pedro Ríos", 45, 2015, 50000, 1000000)

# Crear carro
carro1 = Carros("Taller Multiservicio", "Calle 123", "3216549870", "Toyota", "Corolla", "Rojo", "ABC123")

# Crear cliente
cliente1 = Clientes("Taller Multiservicio", "Calle 123", "3216549870", "Marta Ruiz", 38, "3104567890")

# Crear objeto Bono con parámetros completos para todas las clases base
bono1 = Bono("Taller Multiservicio", "Calle 123", "3216549870",
             "Andrés Díaz", 29, 2021, 35000,
             "Motor", 180, "Tarde", 1000000)

# Guardar listas para luego usar en menú
lista_talleres = [taller]
lista_empleados = [empleado1, mecanico1, recepcionista1, gerente1, bono1]
lista_carros = [carro1]
lista_clientes = [cliente1]

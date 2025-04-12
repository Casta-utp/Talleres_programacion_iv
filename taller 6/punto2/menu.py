from objetos import taller, mecanico1, recepcionista1, gerente1, cliente1, carro1, bono1

# Mostrar información
print("\n--- Información del Taller ---")
print(taller)

print("\n--- Información del Mecánico ---")
print(mecanico1)

print("\n--- Información del Recepcionista ---")
print(recepcionista1)

print("\n--- Información del Gerente ---")
print(gerente1)

print("\n--- Información del Cliente ---")
print(cliente1)

print("\n--- Información del Carro ---")
print(carro1)

print("\n--- Información del Bono ---")
print(bono1)

# Llamado a métodos (ejemplos si existen en tus clases)
print("\n--- Métodos específicos ---")
print("Salario del mecánico con posible aumento:")
print(mecanico1.calcular_salario())  # Asegúrate que exista este método

print("Bono total del gerente:")
print(gerente1.obtener_bono())  # Método de ejemplo si está definido

print("Turno del recepcionista:")
print(recepcionista1.mostrar_turno())  # Método de ejemplo si está definido

print("Detalle completo del bono:")
print(bono1.mostrar_detalle_bono())  # Si definiste un método específico en la clase Bono
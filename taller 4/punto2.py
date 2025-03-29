
class Vehiculo:

    lista = []

    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo

    def __str__(self):
        return f"Marca: {self.marca}, Tipo: {self.tipo}"

    def llenar_lista(self, lista):
        while True:
            tipo = int(input("Ingrese el tipo de vehiculo: 1. Carro, 2. Camioneta, 3. Bicicleta, 4. Moto: "))
            if tipo == 1:
                tipo = "Carro"
                marca = input("Ingrese la marca del coche (Chevrolet/Toyota/Ford): ")
                cilindrada = int(input("Ingrese la cilindrada del coche: "))
                velocidad_maxima = int(input("Ingrese la velocidad máxima del coche: "))
                lista.append(Coche(marca, tipo, cilindrada, velocidad_maxima))
            elif tipo == 2:
                tipo = "Camioneta"
                marca = input("Ingrese la marca de la camioneta (Chevrolet/Toyota/Ford): ")
                cilindrada = int(input("Ingrese la cilindrada de la camioneta: "))
                velocidad_maxima = int(input("Ingrese la velocidad máxima de la camioneta: "))
                carga_maxima = int(input("Ingrese la carga máxima de la camioneta: "))
                lista.append(Camioneta(marca, tipo, cilindrada, velocidad_maxima, carga_maxima))
            elif tipo == 3:
                tipo = "Bicicleta"
                uso = input("Ingrese el uso de la bicicleta (urbano/deportivo): ").lower()
                marca = input("Ingrese la marca de la bicicleta (GW/Trek/Specialized): ")
                velocidad_maxima = int(input("Ingrese la velocidad máxima de la bicicleta: "))
                lista.append(Bicicleta(marca, tipo, uso, velocidad_maxima))
            elif tipo == 4:
                tipo = "Moto"
                marca = input("Ingrese la marca de la moto (Yamaha/Honda/Suzuki): ")
                cilindrada = int(input("Ingrese la cilindrada de la moto: "))
                velocidad_maxima = int(input("Ingrese la velocidad máxima de la moto: "))
                uso = "ninguno"
                lista.append(Moto(marca, tipo, uso, cilindrada, velocidad_maxima))
            else:
                print("Tipo de vehiculo no reconocido")
                continue

            continuar = input("¿Desea agregar otro vehículo a la lista? (s/n): ").strip().lower()
            if continuar == "n":
                break

    def ruedas_calidad(self, marca: str, tipo: str):
        if tipo == "Carro" or tipo == "Camioneta":
            if marca == "Chevrolet":
                print("Las llantas duraran 4 años")
            elif marca == "Toyota":
                print("Las llantas duraran 5 años")
            elif marca == "Ford":
                print("Las llantas duraran 3 años")
            else:
                print("Las llantas duraran 2 años")
        elif tipo == "Moto":
            if marca == "Yamaha":
                print("Las llantas duraran 2 años")
            elif marca == "Honda":
                print("Las llantas duraran 3 años")
            elif marca == "Suzuki":
                print("Las llantas duraran 1 año")
            else:
                print("Las llantas duraran 1.5 años")
        elif tipo == "Bicicleta":
            if marca == "GW":
                print("Las llantas duraran 2 años")
            elif marca == "Trek":
                print("Las llantas duraran 3 años")
            elif marca == "Specialized":
                print("Las llantas duraran 4 años")
        else:
            print("Tipo de vehiculo no reconocido")

    def combustible_aconsejado(self, marca: str, tipo: str):
        if tipo == "Carro" or tipo == "Camioneta":
            if marca == "Chevrolet":
                print("Se aconseja usar gasolina corriente")
                return "corriente"
            elif marca == "Toyota":
                print("Se aconseja usar gasolina extra")
                return "extra"
            elif marca == "Ford":
                print("Se aconseja usar gasolina corriente")
                return "corriente"
            else:
                print("Se aconseja usar gasolina corriente")
                return "corriente"
        elif tipo == "Moto":
            if marca == "Yamaha":
                print("Se aconseja usar gasolina corriente")
                return "corriente"
            elif marca == "Honda":
                print("Se aconseja usar gasolina extra")
                return "extra"
            elif marca == "Suzuki":
                print("Se aconseja usar gasolina corriente")
                return "corriente"
            else:
                print("Se aconseja usar gasolina corriente")
                return "corriente"
        elif tipo == "Bicicleta":
            print("Las bicicletas no usan combustible")
        else:
            print("Tipo de vehiculo no reconocido")

    def consumo_gasolina(self, marca: str, tipo: str):
            combustible = self.combustible_aconsejado(marca, tipo)
            distancia_mensual = 1000
            precio_corriente = 9000
            precio_extra = 10000
            consumo = 0
            if combustible == "corriente":
                consumo = int(input("Ingrese el consumo de combustible (km/L): "))
                total_gastos = (distancia_mensual / consumo) * precio_corriente
                print(f"El gasto mensual en gasolina es de ${total_gastos:.2f}")
            elif combustible == "extra":
                consumo = int(input("Ingrese el consumo de combustible (km/L): "))
                total_gastos = (distancia_mensual / consumo) * precio_extra
                print(f"El gasto mensual en gasolina es de ${total_gastos:.2f}")
            elif combustible is None:
                print(f"El tipo de vehículo '{tipo}' no requiere combustible o no es reconocido.")

    def mostrar_lista(self, lista):
        for vehiculo in lista:
            print(vehiculo)

    def guardar_lista(self, lista, filename="archivos-2/vehiculos-1.txt"):
        """Guarda la lista de vehículos en un archivo de texto."""
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for veh in lista:
                    if isinstance(veh, Coche):
                        file.write(f"Coche,{veh.marca},{veh.tipo},{veh.cilindrada},{veh.velocidad_maxima}\n")
                    elif isinstance(veh, Camioneta):
                        file.write(f"Camioneta,{veh.marca},{veh.tipo},{veh.cilindrada},{veh.velocidad_maxima},{veh.carga_maxima}\n")
                    elif isinstance(veh, Bicicleta):
                        file.write(f"Bicicleta,{veh.marca},{veh.tipo},{veh.uso},{veh.velocidad_maxima}\n")
                    elif isinstance(veh, Moto):
                        file.write(f"Moto,{veh.marca},{veh.tipo},{veh.uso},{veh.cilindrada},{veh.velocidad_maxima}\n")
            print("Lista de vehículos guardada exitosamente.")
        except Exception as e:
            print(f"Error al guardar la lista: {e}")

    def cargar_lista(self, lista, filename="archivos-2/vehiculos-1.txt"):
        """Carga la lista de vehículos desde un archivo de texto."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                lista.clear()
                for line in file:
                    data = line.strip().split(",")
                    tipo = data[0]
                    if tipo == "Coche":
                        _, marca, tipo, cilindrada, velocidad_maxima = data
                        lista.append(Coche(marca, tipo, int(cilindrada), int(velocidad_maxima)))
                    elif tipo == "Camioneta":
                        _, marca, tipo, cilindrada, velocidad_maxima, carga_maxima = data
                        lista.append(Camioneta(marca, tipo, int(cilindrada), int(velocidad_maxima), int(carga_maxima)))
                    elif tipo == "Bicicleta":
                        _, marca, tipo, uso, velocidad_maxima = data
                        lista.append(Bicicleta(marca, tipo, uso, int(velocidad_maxima)))
                    elif tipo == "Moto":
                        _, marca, tipo, uso, cilindrada, velocidad_maxima = data
                        lista.append(Moto(marca, tipo, uso, int(cilindrada), int(velocidad_maxima)))
            print("Lista de vehículos cargada exitosamente.")
        except FileNotFoundError:
            print("No se encontró un archivo guardado.")
        except Exception as e:
            print(f"Error al cargar la lista: {e}")

    def listar_vehiculos_ruedas(self, lista):
        ruedas = int(input("Ingrese el número de ruedas: "))
        for vehiculo in lista:
            if (vehiculo.tipo == "Carro" or vehiculo.tipo == "Camioneta") and ruedas == 4:
                print(vehiculo)
            elif (vehiculo.tipo == "Moto" or vehiculo.tipo == "Bicicleta") and ruedas == 2: 
                print(vehiculo)
            else:
                print(f"no hay vehiculos con {ruedas} ruedas")

    def tiempo_viaje(self, velocidad: int):
            destinos = {
                1: ("Bogota", 307),
                2: ("Medellin", 241),
                3: ("Cali", 209),
                4: ("Barranquilla", 995),
                5: ("Cartagena", 943)
            }
    
            while True:
                print("Escoja la ubicacion de destino:")
                for key, value in destinos.items():
                    print(f"{key}. {value[0]}")
    
                destino = int(input("Ingrese el numero de la ubicacion de destino: "))
                if destino in destinos:
                    distancia = destinos[destino][1]
                    tiempo = distancia / velocidad
                    print(f"El tiempo de viaje a {destinos[destino][0]} es de {tiempo:.2f} horas")
                else:
                    print("Ubicacion no reconocida")
    
                continuar = input("Desea calcular el tiempo de viaje a otra ciudad? (s/n): ")
                if continuar == "n":
                    break


class Coche(Vehiculo):

    def __init__(self, marca, tipo, cilindrada, velocidad_maxima):
        super().__init__(marca, tipo)
        self.cilindrada = cilindrada
        self.velocidad_maxima = velocidad_maxima

    def __str__(self):
        return f"Marca: {self.marca}, Cilindrada: {self.cilindrada}, Velocidad Maxima: {self.velocidad_maxima}, Tipo: {self.tipo}"


class Camioneta(Coche):
    
    def __init__(self, marca, tipo, cilindrada, velocidad_maxima, carga_maxima):
        super().__init__(marca, tipo, cilindrada, velocidad_maxima)
        self.carga_maxima = carga_maxima

    def __str__(self):
        return f"Marca: {self.marca}, Cilindrada: {self.cilindrada}, Velocidad Maxima: {self.velocidad_maxima}, Carga Maxima: {self.carga_maxima}, Tipo: {self.tipo}"


class Bicicleta(Vehiculo):
    
    def __init__(self, marca, tipo, uso, velocidad_maxima):
        super().__init__(marca, tipo)
        self.uso = uso
        self.velocidad_maxima = velocidad_maxima

    def __str__(self):
        return f"Marca: {self.marca}, Uso: {self.uso}, Velocidad Maxima: {self.velocidad_maxima}, Tipo: {self.tipo}"
    

class Moto(Bicicleta):
    
    def __init__(self, marca, tipo, uso, cilindrada, velocidad_maxima):
        super().__init__(marca, tipo, uso, velocidad_maxima)
        self.velocidad_maxima = velocidad_maxima
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca: {self.marca}, Cilindrada: {self.cilindrada}, Velocidad Maxima: {self.velocidad_maxima}, Uso: {self.uso}, Tipo: {self.tipo}"
class Calcular_area:

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def set(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser números positivos.")
        self.__base = base
        self.__altura = altura

    def get(self):
        return self.__base, self.__altura
    
    def area(self):
        return self.__base * self.__altura
    
    def get_area(self):
        return self.__base * self.__altura
    
class Calcular_area_triangulo(Calcular_area):

    def __init__(self, base, altura):
        super().__init__(base, altura)
    
    def area(self):
        return (self._Calcular_area__base * self._Calcular_area__altura) / 2
    
    def set(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser números positivos.")
        self._Calcular_area__base = base
        self._Calcular_area__altura = altura

    def get(self):
        return self._Calcular_area__base, self._Calcular_area__altura
    
    def get_area(self):
        return (self._Calcular_area__base * self._Calcular_area__altura) / 2
    
class Calcular_area_circulo(Calcular_area):

    def __init__(self, radio):
        self.set(radio)
    
    def area(self):
        return 3.14 * (self.__radio ** 2)
    
    def set(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.__radio = radio

    def get(self):
        return self.__radio
    
    def get_area(self):
        return 3.14 * (self.__radio ** 2)
    
class Calcular_area_cuadrado(Calcular_area):

    def __init__(self, lado):
        self.set(lado)

    def area(self):
        return self.__lado ** 2
    
    def set(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        self.__lado = lado

    def get(self):
        return self.__lado
    
    def get_area(self):
        return self.__lado ** 2
    
class Calcular_area_rectangulo(Calcular_area):

    def __init__(self, base, altura):
        self.set(base, altura)

    def area(self):
        return self.__base * self.__altura
    
    def set(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser números positivos.")
        self.__base = base
        self.__altura = altura

    def get(self):
        return self.__base, self.__altura
    
    def get_area(self):
        return self.__base * self.__altura
    
class Calcular_area_trapecio(Calcular_area):

    def __init__(self, base_menor, base_mayor, altura):
        self.set(base_menor, base_mayor, altura)

    def area(self):
        return ((self.__base_menor + self.__base_mayor) * self.__altura) / 2
        
    def set(self, base_menor, base_mayor, altura):
        if base_menor <= 0 or base_mayor <= 0 or altura <= 0:
            raise ValueError("Base menor, base mayor y altura deben ser números positivos.")
        self.__base_menor = base_menor
        self.__base_mayor = base_mayor
        self.__altura = altura

    def get(self):
        return self.__base_menor, self.__base_mayor, self.__altura
    
    def get_area(self):
        return ((self.__base_menor + self.__base_mayor) * self.__altura) / 2

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto de la clase Calcular_area
    area = Calcular_area(5, 10)
    print("Área del rectángulo:", area.get_area())
    
    # Crear un objeto de la clase Calcular_area_triangulo
    area_triangulo = Calcular_area_triangulo(5, 10)
    print("Área del triángulo:", area_triangulo.get_area())
    
    # Crear un objeto de la clase Calcular_area_circulo
    area_circulo = Calcular_area_circulo(5)
    print("Área del círculo:", area_circulo.get_area())
    
    # Crear un objeto de la clase Calcular_area_cuadrado
    area_cuadrado = Calcular_area_cuadrado(5)
    print("Área del cuadrado:", area_cuadrado.get_area())
    
    # Crear un objeto de la clase Calcular_area_rectangulo
    area_rectangulo = Calcular_area_rectangulo(5, 10)
    print("Área del rectángulo:", area_rectangulo.get_area())
    
    # Crear un objeto de la clase Calcular_area_trapecio
    area_trapecio = Calcular_area_trapecio(5, 10, 5)
    print("Área del trapecio:", area_trapecio.get_area())

class Rectangulo: 

    def __init__(self):
        self.base = 0
        self.altura = 0
        self.area = 0
        self.perimetro = 0
    
    def __str__(self):
        return f"Base: {self.base}, Altura: {self.altura}, Area: {self.area}, Perimetro: {self.perimetro}"
    
    def llenar_datos(self):
        self.base = int(input("Ingrese la base del rectangulo: "))
        self.altura = int(input("Ingrese la altura del rectangulo: "))
    
    def imprimir_rectangulo(self):
        for i in range(self.altura):
            for j in range(self.base):
                print("*", end="")
            print()
    
    def calcular_area(self):
        self.area = self.base * self.altura
    
    def calcular_perimetro(self):
        self.perimetro = 2 * (self.base + self.altura)

# rectangulo = Rectangulo()
# rectangulo.llenar_datos()
# rectangulo.imprimir_rectangulo()
# rectangulo.calcular_area()
# rectangulo.calcular_perimetro()
# print(rectangulo)
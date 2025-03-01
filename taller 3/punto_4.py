import math

class Calculadora:

    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.resultado = 0

    def __str__(self):
        return f"Numero 1: {self.numero1}, Numero 2: {self.numero2}, Resultado: {self.resultado}"
    
    def llenar_datos(self):
        self.numero1 = int(input("Ingrese el primer numero: "))
        self.numero2 = int(input("Ingrese el segundo numero: "))
    
    def sumar(self):
        self.resultado = self.numero1 + self.numero2
        print (f"La suma de {self.numero1} + {self.numero2} es: {self.resultado}")
    
    def restar(self):
        self.resultado = self.numero1 - self.numero2
        print (f"La resta de {self.numero1} - {self.numero2} es: {self.resultado}")

    def multiplicar(self):
        self.resultado = self.numero1 * self.numero2
        print (f"La multiplicacion de {self.numero1} * {self.numero2} es: {self.resultado}")
    
    def dividir(self):
        self.resultado = self.numero1 / self.numero2
        print (f"La division de {self.numero1} / {self.numero2} es: {self.resultado}")
    
    def potencia(self):
        self.resultado = self.numero1 ** self.numero2
        print (f"La potencia de {self.numero1} ** {self.numero2} es: {self.resultado}")

    def modulo(self):
        self.resultado = self.numero1 % self.numero2
        print (f"El modulo de {self.numero1} % {self.numero2} es: {self.resultado}")

    def raiz_cuadrada(self):
        self.resultado = math.sqrt(self.numero1)
        print (f"La raiz cuadrada de {self.numero1} es: {self.resultado}")

    def raiz_n(self):
        self.resultado = self.numero1 ** (1 / self.numero2)
        print (f"La raiz {self.numero2} de {self.numero1} es: {self.resultado}")

    def logaritmo(self):
        self.resultado = math.log(self.numero1)
        print (f"El logaritmo de {self.numero1} es: {self.resultado}")

    def logaritmo_base_n(self):
        self.resultado = math.log(self.numero1, self.numero2)
        print (f"El logaritmo base {self.numero2} de {self.numero1} es: {self.resultado}")

    def seno(self):
        self.resultado = math.sin(math.radians(self.numero1))
        print (f"El seno de {self.numero1} es: {self.resultado}")

    def coseno(self):
        self.resultado = math.cos(math.radians(self.numero1))
        print (f"El coseno de {self.numero1} es: {self.resultado}")
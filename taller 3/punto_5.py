class Lista:

    def __init__(self):
        self.lista=[1, 1991, "taller", 200, 3, "programación", 700, "utp", "POO"]
        self.lista_numeros = []
        self.lista_palabras = []
        self.lista_impares = []
        self.mitad = 0

    def __str__(self):
        return f"Lista: {self.lista}, Lista de numeros: {self.lista_numeros}, Lista de palabras: {self.lista_palabras}, Lista de impares: {self.lista_impares}"
        
    def guardar_lista(self):
        with open("lista.txt", "w") as f:
            for i in self.lista:
                f.write(str(i) + "\n")
    
    def llenar_lista_numeros(self):
        for i in self.lista:
            if type(i) == int:
                self.lista_numeros.append(i)
        print(self.lista_numeros)
    
    def llenar_lista_palabras(self):
        for i in self.lista:
            if type(i) == str:
                self.lista_palabras.append(i)
        print(self.lista_palabras)
    
    def guardar_lista_numeros(self):
        with open("lista_numeros.txt", "w") as f:
            for i in self.lista_numeros:
                f.write(str(i) + "\n")
    
    def guardar_lista_palabras(self):
        with open("lista_palabras.txt", "w") as f:
            for i in self.lista_palabras:
                f.write(i + "\n")
    
    def llenar_lista_impares(self):
        for i in self.lista:
            if type(i) == int:
                if i % 2 != 0:
                    self.lista_impares.append("reemplazo")
                else:
                    self.lista_impares.append(i)
            else:
                self.lista_impares.append(i)

    def guardar_lista_impares(self):
        with open("lista_impares.txt", "w") as f:
            for i in self.lista_impares:
                f.write(str(i) + "\n")
        
    def imprimir_media_lista(self):
        self.mitad = len(self.lista) // 2
        for i in range(self.mitad):
            print(self.lista[i])
        
    

    


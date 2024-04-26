class Auto:
    def __init__(self,pepe_color,marca,modelo):
        self.color=pepe_color
        self.marca=marca
        self.modelo=modelo
        self.km_recorridos=0
    def pintar(self,nuevo_color):
        self.color=nuevo_color
    def obtener_color(self):
        return self.color
if __name__=="__main__":
    auto1= Auto("Amarillo","Chevrolet","Camaro")
    auto2= Auto("Gris","Tesla","Model x")

    print(auto1.color)
    auto1.pintar("Rojo")
    auto2.pintar("Azul")
    print(auto1.obtener_color())


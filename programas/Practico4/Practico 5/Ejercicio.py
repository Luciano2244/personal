class Casa:
    def __init__(self,casa_color,cuartos,pisos,banios):
        self.color=casa_color
        self.cuartos=cuartos
        self.pisos=pisos
        self.banios=banios
        
    def pintar(self,nuevo_color):
        self.color=nuevo_color
    def obtener_info(self):
        return self.color,self.cuartos,self.pisos,self.banios
if __name__=="__main__":
    casa1= Casa("Amarillo",("cuartos",2),("pisos",1),("banios",1))
    casa2= Casa("Blanca",4,2,3)

    print(casa1.color)
    casa1.pintar("Rojo")
    casa2.pintar("Azul")
    print(casa1.obtener_info())

"""Escriba una clase que represente un círculo; el círculo queda perfectamente definido
si se conoce su radio.
a. Defina además, para esta clase, dos métodos que permitan calcular el área
del círculo y el perímetro de la circunferencia que delimita el círculo.
b. Para probar la funcionalidad antes definida, escriba un método que cree un
círculo con un radio dado, y que calcule (y muestre por pantalla) el área y el
perímetro de su circunferencia.""" 

class Circulo:
    def __init__(self,radio):
        self.radio=radio #defino el radio
    
    def perimetro(self):
        return (self.radio*2)*3.14 #return para calcular el perimetro con self.radio
    
    def area(self):
        return 3.14*self.radio #lo mismo que el perimetro
    
if __name__=="__main__":
    C1=Circulo(3) #defino una circunferencia de radio 3 con nombre C1
    C2=Circulo(2) #defino una circunferencia de radio 2 con nombre C2
    C1.area() #calculo el area en C1
    C2.perimetro() #calculo el area en C2
    print(C1.area(),C2.perimetro()) #imprimo los calculos
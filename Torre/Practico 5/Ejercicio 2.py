import math

class Circle:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def calcular(self):
        # Calcular área y perímetro
        area = self.area()
        perimetero = self.perimetro()

        # Mostrar por pantalla los resultados
        print(f"El área del círculo es: {area:.2f}")
        print(f"El perímetro de la circunferencia es: {perimetero:.2f}")

# Crear un círculo con un radio dado y calcular sus propiedades
def test_circle(radio):
    circle = Circle(radio)
    circle.calcular()

if __name__ == "__main__":
    # Crear un círculo con radio=5
    test_circle(5)
"""Se quiere definir una clase que permita controlar un sintonizador digital de emisoras
FM; concretamente, lo que se desea es dotar al controlador de una interfaz que
permita subir (up) o bajar (down) la frecuencia (en saltos de 0.5 MHz) y mostrar la
frecuencia sintonizada en un momento dado (display).
Supondremos que el rango de frecuencias a manejar oscila entre los 80 Mhz y los
108 MHz y que al inicio, el controlador sintoniza a 80 MHz.
Si durante una operación de subida o bajada se sobrepasa uno de los dos límites, la
frecuencia sintonizada debe pasar a ser la del extremo contrario."""

class Sintonizador:
    def __init__(self,frecuencia):
        self.frecuencia=frecuencia 
    
    def reducir(self):  
        self.frecuencia -= 0.5
        if self.frecuencia < 80:
            self.frecuencia = 108
        return self.frecuencia
    
    def subir(self):
        self.frecuencia += 0.5
        if self.frecuencia > 108:
            self.frecuencia = 80
        return self.frecuencia
    
    def display(self):
        return self.frecuencia
    
if __name__=="__main__":
    sz=Sintonizador(80)
    for i in range (56):
        sz.subir()
    print(sz.display())
    
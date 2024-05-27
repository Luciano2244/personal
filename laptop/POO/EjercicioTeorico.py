from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
    def obtener_nombre_completo(self):
        return self.nombre + " " + self.apellido
    @abstractmethod
    def deducir_edad(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, apellido, cedula, numero):
        super().__init__(nombre, apellido, cedula)
        self.numero = numero
    def obtener_nombre_completo(self):
        return super().obtener_nombre_completo() + " " + self.numero
    def deducir_edad(self):
        pass

class Programador(Persona):
    def __init__(self,nombre,apellido,cedula,actividad):
        super().__init__(nombre,apellido,cedula)
        self.actividad=actividad
    def realizar_actividad(self):
        return self.actividad
    def deducir_edad(self):
        pass
    
class Tester(Persona):
    def __init__(self,nombre,apellido,actividad):
        super().__init__(nombre,apellido)
        self.actividad=actividad 
    def realizar_actividad(self):
        return self.actividad
    def deducir_edad(self):
        pass
    
if __name__ == "__main__":
    estudiante = Estudiante("Daniel", "Pereda", "445213", "876")
    print(estudiante.obtener_nombre_completo())
    p1 = Programador("Daniel", "Pereda","445213","programando")
    print(p1.realizar_actividad())
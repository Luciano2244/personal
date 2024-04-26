import random

def crear_array(tamano):
    array = []
    for i in range(tamano):
        array.append(random.randint(0,10))
    return array

def sumar_elementos_array(array):
    suma = 0
    a=2
    print("Indice posicion a=",a)
    b=4
    print("Indice posicion b=", b)
    for i in range(a,b):
        suma = suma + array[i]
    print("Esta es la suma entre los sectores: ")
    return suma


if __name__ == "__main__":
    print("Este es el array: ")
    array = crear_array(5)
    print(array)
    print(sumar_elementos_array(array))
#Tenemos que realizar un conjunto de operaciones de utilidad para trabajar con
#listas de enteros. Las operaciones son:
#a. def desplegar(vecEnteros)
#i. Despliega en salida estándar el contenido de la lista
#b. def maximo(vecEnteros)
#i. Retorna el número máximo que está contenido en la lista.
#c. def suma(vecEnteros)
#i. Retorna el valor de sumar todos los números enteros contenido
#en la lista.
#d. def suma(vecEnteros, a, b);
#i. Retorna la suma de todos los enteros que están desde el índice
#a hasta el índ#ce b.
#e. def veces(vecEnteros, n)
#i. Retorna la cantidad de ocurrencias del número n dentro de la
#lista.
#f. def lugares(vecEnteros, n)
#i. Retorna una lista conteniendo las posiciones dentro de la lisa
#vecEnternos que se encuentra el número “n”. La lista resultante
#no tiene que tener espacios vacíos. 


import random
   
def veces(vecEnteros, n):
   sam=0
   for i in range(len(vecEnteros)):
        if n==vecEnteros[i]:
                sem=0
                sam = sam + 1
                sem = sem + i
                print("posicion:",sem)
   print(sam,"veces")
    
                
def lugares(vecEnteros, n):
        for i in range(len(vecEnteros)):
            if n==vecEnteros[i]:
                print("se encontro n:")
                break

def crear_lista(tamano):
    vecEnteros = []
    for i in range(tamano):
        vecEnteros.append(random.randint(0,10))
    return vecEnteros

def desplegar(vecEnteros):
    print(vecEnteros)

def suma(vecEnteros):
    suma = 0
    for i in range(len(vecEnteros)):
        suma = suma + vecEnteros[i]
    return suma

def maximo(vecEnteros):
    max = vecEnteros[0];
    for x in vecEnteros:
        if x > max:
            max = x
    print('Este es maximo de lista:', max)

def sumaAB(vecEnteros, a, b):
    suma2 = 0
    print(a,b)
    for i in range(a,b):
        suma2 = suma2 + vecEnteros[i]
    print("Esta es la suma entre los sectores: ")
    return suma2

if __name__ == "__main__":
    print("Esta es la lista: ")
    vecEnteros = crear_lista(5)
    a=0
    b=4
    n=5
    print(desplegar(vecEnteros))
    print("Esta es la suma de todo el array: ")
    print(suma(vecEnteros))
    print("estos son los valores de A, B:")
    print(sumaAB(vecEnteros,a,b))
    print("este es el digito maximo:")
    print(maximo(vecEnteros))
    lugares(vecEnteros,n)
    veces(vecEnteros,n)
    
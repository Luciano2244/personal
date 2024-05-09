import random

def crear_matriz(cant_filas, cant_columnas):
    matriz=[
    [1,2,3],
    [4,5,6], 
    [7,8,9]]
    return matriz
def Lista(tamano):
    array = []
    for i in range(tamano):
        array.append(random.randint(0,1000))
    return array
#Funcion para que imprima la matriz linda
def imprimir_matriz(matriz):
    for i in range(0,3):
        for j in range(0,3):
            print(matriz[i][j], end=" ")
        print("")

if __name__ == "__main__":
    matriz_random = crear_matriz(3,3)
    print("Esta es la matriz")
    imprimir_matriz(matriz_random)
    print("--------------------")
    b=Lista(20)
    print('esta es la lista B:',b)
    a=b[2::3]
    print('esta es la lista A:',a)
    x=b[6::7]
    print('Mostrando 7x7 digitos:',x)
        
        
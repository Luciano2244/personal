import random

def t(cant_filas, cant_columnas):
    matriz = []
    for i in range(cant_filas):
        fila = []
        for j in range(cant_columnas):
            valor = random.randint(0, 9)
            fila.append(valor) 
        matriz.append(fila)
    return matriz

def cant_filas(matriz):
   x=0
   suma=1
   while x < len(matriz):
       suma = suma + x
       x += 1
       print(suma)
     
def cant_columnas(matriz):
   x=1
   suma=0
   while x <= len(matriz[0]):
       n = 1
       suma = suma + n
       x = x + 1
       print(suma)   
   

def imprimir_matriz(matriz):
    for i in range(0,2):
        for j in range(0,5):
            print(matriz[i][j], end=" ")
        print(" ")

def imprimir_segunda_fila(matriz):
        print(matriz[len(matriz)-1])
   

if __name__ == "__main__":
    matriz = t(2,5)
    print("Esta es la matriz t")
    imprimir_matriz(matriz)
    print('cantidad de columnas de t')
    cant_filas(matriz)
    print('cantidad de filas de t')
    cant_columnas(matriz)
    print('sintaxis segunda fila de t')
    imprimir_segunda_fila(matriz)

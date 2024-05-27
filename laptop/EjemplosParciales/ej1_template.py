def ingresar_datos():
    print("...")

def consultar_cantidad_vendida_en_rango(matriz):
    print("...")

def consultar_maximo(matriz):
    print("...")

if __name__ == '__main__':
    matriz = ingresar_datos()
    programa_funcionando = True
    while programa_funcionando == True:
        print("Menú:")
        print("1. Consultar la cantidad de unidades vendidas de un producto en un rango de días específico")
        print("2. Consultar el día en que se vendió la mayor cantidad de unidades de un producto")
        print("3. Salir")
        opcion = int(input("Ingrese una opción: "))

        #Se verifica la opción seleccionada por el usuario y se realiza la consulta correspondiente
        if opcion == 1:
            consultar_cantidad_vendida_en_rango(matriz)
        elif opcion == 2:
            consultar_maximo(matriz)
        elif opcion == 3:
            programa_funcionando = False
        else:
            print("Opción inválida")

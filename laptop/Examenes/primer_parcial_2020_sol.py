def poner_alimento_heladera(heladera, alimento, cantidad):
    esta = False
    for alimento_en_heladera in heladera:
        if alimento_en_heladera[0] == alimento:
            esta = True
            alimento_en_heladera[0] += cantidad
        
    if not esta:
        alimento_a_agregar = [alimento, cantidad]
        heladera.append(alimento_a_agregar)

def sacar_alimento_heladera(heladera, alimento, cantidad):
    pude_sacar = False

    for alimento_en_heladera in heladera:
        if alimento_en_heladera[0] == alimento and alimento_en_heladera[1] >= cantidad:
            pude_sacar = True
            alimento_en_heladera[1] -= cantidad

    return pude_sacar

def sacar_alimentos_para_receta(heladera, receta):
    pude_sacar = True

    # primero verifico que todos los ingredientes estan en la heladera
    hay_stock = True
    encontre = True
    i = 0
    while hay_stock and encontre and i < len(receta):
        alimento_en_receta = receta[i]
        encontre = False
        for alimento_en_heladera in heladera:
            if alimento_en_heladera[0] == alimento_en_receta[0]:
                encontre = True
                if alimento_en_heladera[1] < alimento_en_receta[1]:
                    hay_stock = False
        i += 1
 
    if not hay_stock or not encontre:
        pude_sacar = False
    else:
        # si encontre todos los productos con su respectivo stock
        # los saco de la heladera
        for alimento_en_receta in receta:
            sacar_alimento_heladera(heladera, alimento_en_receta[0], alimento_en_receta[1])

    return pude_sacar

def alimentos_a_comprar_para_receta (heladera, receta, tabla_conversion_unidad):
    resultado = []
    
    for alimento_en_receta in receta:
        encontre = False
        for alimento_en_heladera in heladera:
            if alimento_en_heladera[0] == alimento_en_receta[0]:
                encontre = True
                if alimento_en_heladera[1] < alimento_en_receta[1]:
                    cantidad_a_agregar = alimento_en_receta[1] - alimento_en_heladera[1]
                    unidades_a_agregar = convertir_producto_a_unidades(alimento_en_receta[0], cantidad_a_agregar, tabla_conversion_unidad)
                    alimento_a_comprar = [alimento_en_receta[0], unidades_a_agregar]
                    resultado.append(alimento_a_comprar)
        if not encontre:
            unidades_a_agregar = convertir_producto_a_unidades(alimento_en_receta[0], alimento_en_receta[1], tabla_conversion_unidad)
            alimento_a_comprar = [alimento_en_receta[0], unidades_a_agregar]
            resultado.append(alimento_a_comprar)
                    
    return resultado

def convertir_producto_a_unidades(alimento, cantidad, tabla_conversion_unidad):
    unidades = cantidad

    for alimento_en_tabla in tabla_conversion_unidad:
        if alimento_en_tabla[0] == alimento:
            # Me quedo con el resultado de la division entera
            unidades = cantidad // alimento_en_tabla[1]
            # Si el modulo es mayor que cero (hay resto) agrego una unidad mas
            if cantidad % alimento_en_tabla[1] > 0:
                unidades += 1

    return unidades

if __name__ == "__main__":
    # Pruebas
    
    # Prueba 1, agregar alimentos
    heladera = []
    poner_alimento_heladera(heladera, "Leche", 1000)
    poner_alimento_heladera(heladera, "Manteca", 400)
    poner_alimento_heladera(heladera, "Huevos", 12)

    if len(heladera) == 3:
        if (heladera[0][0] == "Leche" and heladera[0][1] == 1000 and 
                heladera[1][0] == "Manteca" and heladera[1][1] == 400 and
                heladera[2][0] == "Huevos" and heladera[2][1] == 12):
                print("Prueba 1 ok")
        else:
            print("Prueba 1 incorrecta")
    else:
        print("Prueba 1 incorrecta")

    # Prueba 2, sacar alimentos
    temp_resu = sacar_alimento_heladera(heladera, "Leche", 400)
    temp_resu2 = sacar_alimento_heladera(heladera, "Leche", 200)
    temp_resu3 = sacar_alimento_heladera(heladera, "Tomate", 1000)

    if temp_resu and temp_resu2 and not temp_resu3:
        if len(heladera) == 3:
            if (heladera[0][0] == "Leche" and heladera[0][1] == 400 and 
                    heladera[1][0] == "Manteca" and heladera[1][1] == 400 and
                    heladera[2][0] == "Huevos" and heladera[2][1] == 12):
                    print("Prueba 2 ok")
            else:
                print("Prueba 2 incorrecta")
        else:
            print("Prueba 2 incorrecta")
    else:
        print("Prueba 2 incorrecta")
    
    # prueba 3, sacar alimentos para receta

    receta = [["Leche", 300], ["Huevos", 6], ["Manteca", 200]]
    receta2 = [["Leche", 300], ["Huevos", 2], ["Tomates", 300]]

    temp_resu = sacar_alimentos_para_receta(heladera, receta)
    temp_resu2 = sacar_alimentos_para_receta(heladera, receta2)

    if temp_resu and not temp_resu2:
        if len(heladera) == 3:
            if (heladera[0][0] == "Leche" and heladera[0][1] == 100 and 
                    heladera[1][0] == "Manteca" and heladera[1][1] == 200 and
                    heladera[2][0] == "Huevos" and heladera[2][1] == 6):
                    print("Prueba 3 ok")
            else:
                print("Prueba 3 incorrecta")
        else:
            print("Prueba 3 incorrecta")
    else: 
        print("Prueba 3 incorrecta")

    # prueba 4, sacar alimentos para comprar de una receta
    receta = [["Leche", 300], ["Huevos", 2], ["Tomates", 300]]
    tabla_conversion_unidad = [["Leche", 1000], ["Huevos", 1], ["Tomates", 200]]

    compras = alimentos_a_comprar_para_receta(heladera, receta, tabla_conversion_unidad)
    
    if (len(compras) == 2 and compras[0][0] == "Leche" and compras[0][1] == 1 and 
            compras[1][0] == "Tomates" and compras[1][1] == 2):
        print("Prueba 4 ok")
    else:
        print("Prueba 4 incorrecta")
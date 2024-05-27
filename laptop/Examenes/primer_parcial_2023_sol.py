def registrar_venta(tipos_abonos, mat_ventas, persona, tipo, mes_compra, anio_compra):
    registro_ok= False
    
    # controlo validez de los parámetros de entrada
    if persona=="" or tipo not in range(len(tipos_abonos)) or mes_compra < 0 or mes_compra > 12:
        return registro_ok
    
    if tipos_abonos[tipo][2] > 0: # quedan abonos para vender
        mat_ventas.append([persona, tipo, tipos_abonos[tipo][3], mes_compra, anio_compra]) # agrego la venta
        tipos_abonos[tipo][2]-=1 # resto uno a los abonos disponibles para la venta
        registro_ok=True
    
    return registro_ok


def monto_ventas(tipos_abonos, mat_ventas, mes, anio):
    if mes < 0 or mes > 12: #si el mes esta fuera de rango retorna -1
        return -1
    monto=0
    for abono in range(len(mat_ventas)):
        if mat_ventas[abono][3] == mes and mat_ventas[abono][4]== anio:
            tipo=mat_ventas[abono][1] # el tipo del abono vendido esta en la 2a posicion de la fila
            monto+=tipos_abonos[tipo][1] # el precio del abono esta en la fila con ese numero de abono y 2a posicion 
    return monto

#defino funcion auxilar
def esta_vencido(mes, anio, mes_actual, anio_actual): 
    aamm=anio_actual*12*30 + mes_actual*30 # suponemos para simplificar que todos los meses tienen 30 dias
    if aamm - 90 > anio*12*30 + mes*30:
        return False
    else:
        return True

def cantidad_vencida(mat_ventas, tipo, mes_actual, anio_actual):
   cantidad = 0
   
   for abono in mat_ventas:
       if abono[1]==tipo: #busco los abonos vendidos que sean de ese tipo
            if not esta_vencido(abono[3], abono[4], mes_actual, anio_actual):
                    cantidad+=1           

   return cantidad

def registrar_uso(mat_ventas, persona, tipo, mes_actual, anio_actual):
    registro_ok= False

    if persona != "" and tipo > 0 and mes_actual > 0 and mes_actual <= 12: #controlo datos de entrada
    
        for abono in mat_ventas:
            if abono[0]== persona and abono[1]== tipo: # busco la persona y el tipo de abono 
                if abono[2] > 0 and not esta_vencido(abono[3], abono[4], mes_actual, anio_actual):
                    abono[2]-=1
                    registro_ok = True
                    break # no necesita seguir recorriendo la matriz pues ya encontre la persona y el tipo de abono

    return registro_ok

if __name__ == "__main__":

    tipos_abonos = [["Música clásica", 1000, 2, 4], ["Ballet nacional", 1000, 5, 3], ["Artistas del exterior", 3000, 8, 3], ["Obras de teatro", 3, 2, 3], ["Combi", 5000, 100, 7]]

    mat_ventas=[["Juan Pereiro", 1, 4, 4, 2023], ["Majo Landi", 2, 1, 12, 2022], ["Ana Acevedo", 3, 1, 4, 2023]]


    if not registrar_venta(tipos_abonos, mat_ventas, "Juan Pérez", 0,  4, 2023):
        print("Prueba 1 Error")
    else:
        print("Prueba 1 OK")

    if not registrar_venta(tipos_abonos, mat_ventas, "Alicia Maravilla", 0, 5, 2023):
        print("Prueba 1 Error")
    else:
        print("Prueba 1 OK")

    if registrar_venta(tipos_abonos, mat_ventas, "Schrek Dos", 0,  5, 2023):
        print("Prueba 1 Error")
    else:
        print("Prueba 1 OK")

    if cantidad_vencida(mat_ventas,0, 5, 2023) == 0:
        print("Prueba 2 Ok")
    else: 
        print("Prueba 2 Error")

    if cantidad_vencida(mat_ventas, 2, 5, 2023) == 1:
        print("Prueba 2 Ok")
    else: 
        print("Prueba 2 Error")

    if monto_ventas(tipos_abonos, mat_ventas, 1, 2023) != 0:
        print("Prueba 3 Error")    
    else:
        print("Prueba 3 OK")
    
    if monto_ventas(tipos_abonos, mat_ventas, 5, 2023) != 1000:
        print("Prueba 3 Error")    
    else:
        print("Prueba 3 OK")
    
    if monto_ventas(tipos_abonos, mat_ventas, 14, 2023) != -1:
        print("Prueba 3 Error")    
    else:
        print("Prueba 3 OK")

    if registrar_uso(mat_ventas, "Juan Pérez", 1, 5, 2023) == True:
        print("Prueba 4 Error")    
    else:
        print("Prueba 4 OK")

    if registrar_uso(mat_ventas, "Majo Landi", 1, 5, 2023) == True:
        print("Prueba 4 Error")    
    else:
        print("Prueba 4 OK")

    if registrar_uso(mat_ventas, "Ana Acevedo", 2, 5, 2023) == True:
        print("Prueba 4 Error")    
    else:
        print("Prueba 4 OK")

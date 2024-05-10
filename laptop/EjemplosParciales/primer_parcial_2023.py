def registrar_venta(tipos_abonos, mat_ventas, persona, tipo, mes_compra, anio_compra):
    registro_ok= False
    if 1 <=mes_compra <=12 and 0<=tipo <(len(tipos_abonos)):
        cant_restante_abonos=tipos_abonos[tipo][2]
        if cant_restante_abonos > 0:
            cantidad_espetaculos=tipos_abonos[tipo][3] 
            mat_ventas.append([persona,tipo,cantidad_espetaculos,mes_compra,anio_compra])
            tipos_abonos[tipo][2]=tipos_abonos[tipo][2]-1
            registro_ok=True
    return registro_ok


def monto_ventas(tipos_abonos, mat_ventas, mes, anio):
    monto=-1
    if 0<=mes<=12:
        for i in range(0,len(mat_ventas)):
            if mat_ventas[i][3] == mes and mat_ventas[1][4] == anio:
                tipo_abono_vendido=mat_ventas[i][1]
                monto+=tipos_abonos[tipo_abono_vendido][1]
    return monto


def cantidad_vencida(mat_ventas, tipo, mes_actual, anio_actual):
   cantidad = 0

   return cantidad

def registrar_uso(mat_ventas, persona, tipo, mes_actual, anio_actual):
    registro_ok= False

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

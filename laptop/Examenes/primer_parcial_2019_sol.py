def calcular_consumo_dia_franja(consumo_dia_esp, hora_inicio, hora_fin):
    consumo_franja = 0

    for i in range(hora_inicio, hora_fin):
        consumo_franja += consumo_dia_esp[i]

    return consumo_franja

def calcular_gasto_dia(consumo_dia_esp, tipo_tarifa):
    gasto_dia = 0

    if tipo_tarifa == 1: #residencial simple

        gasto_dia = calcular_consumo_dia_franja(consumo_dia_esp, 0, 24) * 6.47
    
    elif tipo_tarifa == 2: # residencial doble horario
        
        # horario punta
        gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 17, 23) * 8.623

        # horario fuera de punta
        gasto_dia += (calcular_consumo_dia_franja(consumo_dia_esp, 0, 17) +
                calcular_consumo_dia_franja(consumo_dia_esp, 23, 24)) * 3.453

    else: # residencial tripe horario

        # horario valle
        gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 0, 7) * 1.803

        # horario llano
        gasto_dia += (calcular_consumo_dia_franja(consumo_dia_esp, 7, 17) +
                calcular_consumo_dia_franja(consumo_dia_esp, 23, 24)) * 4.676

        # horario punta
        gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 17, 23) * 8.623

    return gasto_dia

def calcular_gasto_mensual(consumo_mensual, tipo_tarifa):
    consumo_mes = 0

    for consumo_x_dia in consumo_mensual:
        consumo_mes += calcular_gasto_dia(consumo_x_dia, tipo_tarifa)

    return consumo_mes

def franja_horario_mayor_consumo_mensual(consumo_mensual):
    resultado = []
    acumulado_x_mes = [0 for i in range(24)]
    
    # calculo el consumo acumulado x dia 
    for consumo_x_dia in consumo_mensual:
        for i in range(len(consumo_x_dia)):
            acumulado_x_mes[i] += consumo_x_dia[i]

    # calculo rango de mayor consumo
    rango_mayor_valor = 0
    mayor_valor = 0

    for i in range(0, len(acumulado_x_mes) - 3):
        # Calculo el acumulado del rango
        temp_rango_acumulado = acumulado_x_mes[i]
        temp_rango_acumulado += acumulado_x_mes[i + 1]
        temp_rango_acumulado += acumulado_x_mes[i + 2]
        temp_rango_acumulado += acumulado_x_mes[i + 3]

        # verifico si el acumlado es el nuevo mayor valor        
        if temp_rango_acumulado > mayor_valor:
            mayor_valor = temp_rango_acumulado
            rango_mayor_valor = i

    resultado.append(rango_mayor_valor)
    resultado.append(rango_mayor_valor + 3)
    
    return resultado

if __name__ == "__main__":
    # Set de pruebas básicos
    # Prueba 1 calcular_consumo_franja
    
    consumo_dia = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 15, 10, 10, 1, 1]
    resultado = calcular_consumo_dia_franja(consumo_dia, 19, 22)
    if resultado == 35:
        print("Prueba 1 OK")
    else:
        print(f"Prueba 1 error esperado 35 se obtuvo {resultado}.")

    # Prueba  2 calcular_gasto_dia
    # tarifa 1
    resultado = calcular_gasto_dia(consumo_dia, 1)
    if resultado == 420.55:
        print("Prueba 2 tarifa 1 OK")
    else:
        print(f"Prueba 2 tarifa 1 error esperado 420.55 se obtuvo {resultado}.")

    # tarifa 2
    resultado = round(calcular_gasto_dia(consumo_dia, 2), 3)
    if resultado == 467.435:
        print("Prueba 2 tarifa 2 OK")
    else:
        print(f"Prueba 2 tarifa 2 error esperado 467.435 se obtuvo {resultado}.")

    # tarifa 3
    resultado = round(calcular_gasto_dia(consumo_dia, 3), 3)
    if resultado == 469.338:
        print("Prueba 2 tarifa 3 OK")
    else:
        print(f"Prueba 2 tarifa 3 error esperado 469.338 se obtuvo {resultado}.")

    # Prueba 3 calcular_gasto_mes
    consumo_mes = [[t for t in consumo_dia] for j in range(31)]  
    resultado = round(calcular_gasto_mensual(consumo_mes, 3), 3)
    if resultado == 14549.478:
        print("Prueba 3 OK")
    else:
        print(f"Prueba 2 error esperado 14549,478 se obtuvo {resultado}.")

    # Prueba 4
    franja = franja_horario_mayor_consumo_mensual(consumo_mes)
    if len(franja) == 2 and franja[0] == 18 and franja[1] == 21:
        print("Prueba 4 OK")
    else:
        print(f"Prueba 4 error esperado [18, 21] se obtuvo {franja}.")

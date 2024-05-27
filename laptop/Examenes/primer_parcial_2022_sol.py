def registrar_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta, dia, tipo, importe):
    
    if(dia in range(0, 31)):
        if(tipo == 1):
            gastos_alimentacion[dia - 1] += importe
        elif(tipo == 2):
            gastos_transporte[dia - 1] += importe
        elif(tipo == 3):
            gastos_vestimenta[dia - 1] += importe
        else:
            print("El tipo indicado es INCORRECTO.")
    else:
        print("EL dia indicado es INCORRECTO.")

def calcular_gasto_promedio(gastos):
    contador = 0
    g_acumulado = 0
    for g in gastos:
        if(g != 0):
            g_acumulado = g_acumulado + g
            contador = contador + 1
    return g_acumulado / contador

def obtener_dias_con_gasto_promedio_acumulado_alto(gastos_alimentacion, gastos_transporte, gastos_vestimenta):
    dias_gastos_alto = []
    unicos_dias_gastos_alto = []
    promedio_alimentacion = calcular_gasto_promedio(gastos_alimentacion)
    promedio_transporte = calcular_gasto_promedio(gastos_transporte)
    promedio_vestimenta = calcular_gasto_promedio(gastos_vestimenta)
    for i in range(0, len(gastos_alimentacion)):
        if(gastos_alimentacion[i] > promedio_alimentacion):
            dias_gastos_alto.append(i+1)
    for i in range(0, len(gastos_transporte)):
        if(gastos_transporte[i] > promedio_transporte):
            dias_gastos_alto.append(i+1)
    for i in range(0, len(gastos_vestimenta)):
        if(gastos_vestimenta[i] > promedio_vestimenta):
            dias_gastos_alto.append(i+1)
    for dias in dias_gastos_alto:
        if(dias_gastos_alto.count(dias) == 3 and not dias in unicos_dias_gastos_alto):
            unicos_dias_gastos_alto.append(dias)
    return unicos_dias_gastos_alto

def obtener_dia_de_semana_con_mayor_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta):
    gastos_por_semana_alimentacion = [ gastos_alimentacion[i:i+7] for i in range(0,30,7)]
    gastos_por_semana_transporte = [ gastos_transporte[i:i+7] for i in range(0,30,7)]
    gastos_por_semana_vestimenta = [ gastos_vestimenta[i:i+7] for i in range(0,30,7)]

    gastos_por_dia_alimentacion = [0 for i in range(0,7)] #[sum([g[0] for g in gastos_por_semana_alimentacion])]
    gastos_por_dia_transporte = [0 for i in range(0,7)]
    gastos_por_dia_vestimenta = [0 for i in range(0,7)]
    for dia in range(0,2):
        gastos_por_dia_alimentacion[dia] = sum(g[dia] for g in gastos_por_semana_alimentacion)
        gastos_por_dia_transporte[dia] = sum(g[dia] for g in gastos_por_semana_transporte)
        gastos_por_dia_vestimenta[dia] = sum(g[dia] for g in gastos_por_semana_vestimenta)
    for dia in range(2,7):
        gastos_por_dia_alimentacion[dia] = sum(g[dia] for g in gastos_por_semana_alimentacion[:len(gastos_por_semana_alimentacion)-1])
        gastos_por_dia_transporte[dia] = sum(g[dia] for g in gastos_por_semana_transporte[:len(gastos_por_semana_transporte)-1])
        gastos_por_dia_vestimenta[dia] = sum(g[dia] for g in gastos_por_semana_vestimenta[:len(gastos_por_semana_vestimenta)-1])

    #Alternativa MANUAL: gastos_por_dia_alimentacion[0] = gastos_por_dia_alimentacion[0] + gastos_por_semana_alimentacion[5][0]
    
    gastos_por_dia = [gastos_por_dia_alimentacion[i] + gastos_por_dia_transporte[i] + gastos_por_dia_vestimenta[i] for i in range(0,7)]
    maximo_gasto = max(gastos_por_dia)
    return gastos_por_dia.index(maximo_gasto)

if __name__ == "__main__":

    gastos_alimentacion = [0, 230, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 100]

    gastos_transporte = [0, 230, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 100]

    gastos_vestimenta = [0, 230, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 100]

    registrar_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta, 1, 1, 50)
    registrar_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta, 2, 1, 100)
    registrar_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta, 30, 3, 100)

    if gastos_alimentacion[0] == 50 and gastos_alimentacion[1] == 330 and gastos_vestimenta[29] == 200:
        print("Prueba 1 Ok")
    else: 
        print("Prueba 1 Error")

    gasto_promedio = 69.6

    if calcular_gasto_promedio(gastos_alimentacion) == gasto_promedio:
        print("Prueba 2 Ok")
    else:
        print("Prueba 2 Error")

    dias_gasto_promedio_alto = obtener_dias_con_gasto_promedio_acumulado_alto(gastos_alimentacion, gastos_transporte, gastos_vestimenta)

    if len(dias_gasto_promedio_alto) == 2 and dias_gasto_promedio_alto[0] == 2 and dias_gasto_promedio_alto[1] == 30:
        print("Prueba 3 Ok")
    else:
        print("Prueba 3 Error", dias_gasto_promedio_alto)
   
    dia_mayor_gasto = obtener_dia_de_semana_con_mayor_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta)

    if dia_mayor_gasto == 1:
        print("Prueba 4 Ok")
    else:
        print("Prueba 4 Error")
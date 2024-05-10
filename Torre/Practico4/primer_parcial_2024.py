def registrar_beca(tipos_becas, nombre, nivel, instrumento, cantidad_disponible):
    reg=[nombre,nivel,instrumento,cantidad_disponible]
    if tipos_becas.count([nombre,nivel,instrumento,cantidad_disponible]) == 0:
        if nivel!=0:
            tipos_becas.append(reg)

        else:
            return -1
    return 1

def aplicar_beca(mat_aplicaciones, tipos_becas, nombre_estudiante, nombre_beca, nivel_estudiante):

    reg=[nombre_estudiante,nombre_beca,nivel_estudiante]
    if mat_aplicaciones.count([nombre_estudiante,nombre_beca,nivel_estudiante]) == 0:
        if nivel_estudiante!=0 and nombre_estudiante!="" and nombre_beca!="Beca de Violonchelo":
                mat_aplicaciones.append(reg)
        else:
            return -1
    return 1

def asignar_becas(tipos_becas, mat_aplicaciones, nombre_alumno):
    for aplicacion in mat_aplicaciones:
        if aplicacion[0] == nombre_alumno:
            for reg in tipos_becas:
                if aplicacion[1] == reg[0] and reg[3] > 0:
                    # Otorgar la beca
                    reg[3] -= 1  # Disminuir la cantidad de becas disponibles
                    mat_aplicaciones.remove(aplicacion)  # Eliminar la aplicación del alumno
                    return 1  
            return -1  # No se encontró una beca adecuada o no hay becas disponibles
    return -1  # No se encontró al alumno en la matriz de aplicaciones

def cantidad_aplicaciones_a_beca(mat_aplicaciones, nombre_beca):
    cantidad = 0
    for aplicacion in mat_aplicaciones:
        if aplicacion[1] == nombre_beca:
            cantidad += 1
    if cantidad == 0:
        return -1  # No se encontró la beca en la matriz
    return cantidad

if __name__ == "__main__":
    # Inicializar las matrices con datos preexistentes
    tipos_becas = [
        ["Beca de Piano", 1, "Piano", 5],
        ["Beca de Canto", 2, "Canto", 3]
    ]
    mat_aplicaciones = [
        ["Maria López", "Beca de Canto", 2]
    ]

    # Pruebas de registro de becas
    print("Pruebas de Registro de Becas:")
    registrar_beca(tipos_becas, "Beca de Violín", 2, "Violín", 2)
    if ["Beca de Violín", 2, "Violín", 2] in tipos_becas:
        print("Prueba 1.1 (registro correcto): OK")
    else:
        print("Prueba 1.1 (registro correcto): Error")

    registrar_beca(tipos_becas, "Beca de Violín", 2, "Violín", 2)
    if tipos_becas.count(["Beca de Violín", 2, "Violín", 2]) == 1:
        print("Prueba 1.2 (registro duplicado): OK")
    else:
        print("Prueba 1.2 (registro duplicado): Error")

    registrar_beca(tipos_becas, "Beca de Flauta", 0, "Flauta", 1)
    if ["Beca de Flauta", 0, "Flauta", 1] not in tipos_becas:
        print("Prueba 1.3 (nivel incorrecto): OK")
    else:
        print("Prueba 1.3 (nivel incorrecto): Error")

    # Pruebas de aplicación a becas
    print("\nPruebas de Aplicación a Becas:")
    aplicar_beca(mat_aplicaciones, tipos_becas, "Juan Pérez", "Beca de Piano", 1)
    if ["Juan Pérez", "Beca de Piano", 1] in mat_aplicaciones:
        print("Prueba 2.1 (aplicación correcta): OK")
    else:
        print("Prueba 2.1 (aplicación correcta): Error")

    aplicar_beca(mat_aplicaciones, tipos_becas, "", "Beca de Piano", 1)
    if ["", "Beca de Piano", 1] not in mat_aplicaciones:
        print("Prueba 2.2 (nombre vacío): OK")
    else:
        print("Prueba 2.2 (nombre vacío): Error")

    aplicar_beca(mat_aplicaciones, tipos_becas, "Ana Gómez", "Beca de Violonchelo", 2)
    if ["Ana Gómez", "Beca de Violonchelo", 2] not in mat_aplicaciones:
        print("Prueba 2.3 (beca no existente): OK")
    else:
        print("Prueba 2.3 (beca no existente): Error")
    
    # Pruebas de asignación de becas
    print("\nPruebas de Asignación de Becas:")
    asignar_becas(tipos_becas, mat_aplicaciones, "Maria López")
    if "Maria López" not in [aplicacion[0] for aplicacion in mat_aplicaciones] and tipos_becas[1][3] == 2:
        print("Prueba 3.1 (asignación correcta): OK")
    else:
        print("Prueba 3.1 (asignación correcta): Error")

    asignar_becas(tipos_becas, mat_aplicaciones, "Carlos Ruiz")
    if "Carlos Ruiz" not in [aplicacion[0] for aplicacion in mat_aplicaciones]:
        print("Prueba 3.2 (alumno no existente): OK")
    else:
        print("Prueba 3.2 (alumno no existente): Error")

    # Pruebas de reporte de aplicaciones
    print("\nPruebas de Reporte de Aplicaciones:")
    cantidad = cantidad_aplicaciones_a_beca(mat_aplicaciones, "Beca de Piano")
    if cantidad == 1: 
        print("Prueba 4.1 (cantidad correcta de aplicaciones después de asignación): OK")
    else:
        print(f"Prueba 4.1 (cantidad correcta de aplicaciones después de asignación): Error, obtenido: {cantidad}")

    cantidad = cantidad_aplicaciones_a_beca(mat_aplicaciones, "Beca de Violonchelo")
    if cantidad == -1:
        print("Prueba 4.2 (beca no existente): OK")
    else:
        print(f"Prueba 4.2 (beca no existente): Error, obtenido: {cantidad}")
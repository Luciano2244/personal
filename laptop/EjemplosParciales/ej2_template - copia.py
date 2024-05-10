def cargo_arreglo(arreglo, txt):
    print(f"Ingresar nombres de {txt}s.")
    print()
    seguir="s"
    while seguir=="s" or seguir=="S":
        nombre=input(f"Nombre {txt}:")
        arreglo.append(nombre)
        seguir=input("Desea continuar (s/n):")
        

#def ingresar_calificaciones(estud,mates):
def ingresar_calificaciones():
    # Se definen los nombres de los estudiantes y materias
    # Se crea una matriz de ceros para almacenar las calificaciones
    # Se le pide al usuario ingresar las calificaciones

    estud=[]    
    cargo_arreglo(estud,"Estudiante")
    print(estud)
    
    mates=[]
    cargo_arreglo(mates,"Materia")
    print(mates)

     
    calif=[[0 for i in range(len(mates))] for j in range(len(estud))]   #matriz de calificaciones de todos los alumnos, 1 por fila
    for i in range(len(estud)):
        for j in range(len(mates)):
             nota=int(input(f"Ingrese nota para {estud[i]}, materia {mates[j]}:"))
             calif[i][j]=nota #agrego nota al vector
    return(estud, mates, calif)






def consultar_calificacion_estudiante_materia(estudiantes, materias, calificaciones):
    print("...")    



def consultar_promedio_estudiante(estudiantes, materias, calificaciones):
    print("...")


def consultar_promedio_materia(estudiantes, materias, calificaciones):
    print("...")

if __name__ == '__main__':
    # Se ingresan las calificaciones
    estudiantes, materias, calificaciones=ingresar_calificaciones()
    
    programa_funcionando = True
    # Se muestra un menú con las opciones disponibles
    while programa_funcionando == True:
        print("Menú:")
        print("1. Consultar la calificación de un estudiante en una materia específica")
        print("2. Consultar el promedio de un estudiante en todas las materias")
        print("3. Consultar el promedio de todos los estudiantes en una materia específica")
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))

        # Se verifica la opción seleccionada por el usuario y se realiza la consulta correspondiente
        if opcion == 1:
            consultar_calificacion_estudiante_materia(estudiantes, materias, calificaciones)
        elif opcion == 2:
            consultar_promedio_estudiante(estudiantes, materias, calificaciones)
        elif opcion == 3:
            consultar_promedio_materia(estudiantes, materias, calificaciones)
        elif opcion == 4:
            break
        else:
            print("Opción inválida")
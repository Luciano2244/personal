def cargo_arreglo(arreglo, txt):
    print(f"Ingresar nombres de {txt}s.")
    print()
    seguir="s"
    while seguir=="s" or seguir=="S":
        nombre=input(f"Nombre {txt}:")
        arreglo.append(nombre)
        print()
        print("Elemento ingresado ...")
        print()
        seguir=input("Desea continuar (s/n):")
        

#def ingresar_calificaciones(estud,mates):
def ingresar_calificaciones():
    # Se definen los nombres de los estudiantes y materias
    # Se crea una matriz de ceros para almacenar las calificaciones
    # Se le pide al usuario ingresar las calificaciones

    estud=[]    
    cargo_arreglo(estud,"Estudiante")
       
    mates=[]
    cargo_arreglo(mates,"Materia")
         
    calif=[[0 for i in range(len(mates))] for j in range(len(estud))]   #matriz de calificaciones de todos los alumnos, 1 por fila
    for i in range(len(estud)):
        for j in range(len(mates)):
             nota=int(input(f"Ingrese nota para {estud[i]}, materia {mates[j]}:"))
             calif[i][j]=nota #agrego nota al vector
    return(estud, mates, calif)

def encontrar(vector, nom):
    i=0
    encontre=False
    while not encontre and  i < len(vector):
        if vector[i]==nom:
            encontre=True
        else:
            i=i+1
    if not encontre:
       i=-1
    return(i)

def consultar_calificacion_estudiante_materia(estudiantes, materias, calificaciones):
    print("Consultar Nota de Estudiante de una Materia")
    nom=input("Ingrese estudiante:")
    mat=input("Ingrese materia:")       
    ind_alu=encontrar(estudiantes,nom)
    ind_mat=encontrar(materias,mat)
    if ( ind_alu != -1) and ( ind_mat != -1):
        print(f"La nota de  {nom} en {mat} es {calificaciones[ind_alu][ind_mat]}")
    else:
        print("No existe el alumno indicado o la materia indicada.")
       
# otra manera es usando la funcion mean(), prefefinida en python
def nota_promedio(vector):
    cant=len(vector) 
    suma=0
    for i in range(len(vector)):
        suma=suma + vector[i]
    return(suma/cant)

def consultar_promedio_estudiante(estudiantes, materias, calificaciones):
    print("Consultar Nota Promedio de Estudiante")
    nom=input("Ingrese estudiante:")  
    ind_alu=encontrar(estudiantes,nom)
    if ind_alu != -1:
        prom=nota_promedio(calificaciones[ind_alu])
        print(f"La nota Promedio de  {nom}  es {prom}")
    else:
        print("No existe el alumno indicado o la materia indicada.")



def consultar_promedio_materia(estudiantes, materias, calificaciones):
    print("Consultar Nota Promedio de Materia")
    nom=input("Ingrese materia:")  
    ind_mat=encontrar(materias, nom)
    if ind_mat != -1:
        notas_materia =[calificaciones[i][ind_mat] for i in range(len(calificaciones))]
        prom=nota_promedio(notas_materia)
        print(f"La nota Promedio de  {nom}  es {prom}")
    else:
        print("No existe el alumno indicado o la materia indicada.")

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
        
        print()
        input("Presione una tecla para continuar.....")
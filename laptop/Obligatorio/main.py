import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__=="__main__":
     while True:
        choice = input("""\nSeleccione una opción del menú:
1. Dar de alta una especialidad
2. Dar de alta un socio
3. Dar de alta un médico
4. Dar de alta una consulta médica
5. Emitir un ticket de consulta
6. Realizar consultas
7. Salir del programa \n""")
        clear_terminal()
        if choice.lower()=="1":
            seguir=input("desea continuar?S/N")
            especialidad=input("ingrese nombre de especialidad: ")
            precio_aso=int(input("ingrese precio asociado: "))
            especialiadad_check= isinstance(especialidad, str)
            precio_aso_check= isinstance(precio_aso,int)
            print(str(especialiadad_check),int(precio_aso_check))
            if especialiadad_check==True and precio_aso_check==1:
                print("Datos ingresados correctamente.\n")
                continue
            else:
                print("Hubo un error al ingresar los datos.\n")
                continue
        elif choice.lower()=="2":
            continue
        elif choice.lower()=="3":
            continue
        elif choice.lower()=="4":
            continue
        elif choice.lower()=="5":
            continue
        elif choice.lower()=="6":
            continue
        elif choice.lower()=="7":
            print("Saliendo...")
            break
        else:
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")
            continue
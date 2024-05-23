import os
import datetime

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def AltaEspecialidad():
        while True:
            especialidad=input("ingrese nombre de especialidad: ")
            especialiadad_check= isinstance(especialidad, str)
            while especialiadad_check==False:
                print("no es una especialidad valida, ingresela de nuevo.\n")
                especialidad=input("ingrese nombre de especialidad: ")
                especialiadad_check= isinstance(especialidad, str)

            precio_aso=int(input("ingrese precio asociado: "))
            precio_aso_check= isinstance(precio_aso,int)
            while precio_aso_check!=1:
                print("no es un precio valido, ingreselo de nuevo.\n")
                precio_aso=int(input("ingrese precio asociado: "))
                precio_aso_check= isinstance(precio_aso,int)

            if especialiadad_check==True and precio_aso_check==1:
                print("Datos ingresados correctamente.\n")
            else:
                print("Hubo un error al ingresar los datos.\n")
             
            seguir=input("desea continuar? s/n\n")
            if seguir.lower()=="s":
                continue
            elif seguir.lower()=="n":
                print("Volviendo al menu.")
                break
            else:
                print("Opcion invalida, volviendo al menu.")
                break

def AltaSocio():
    while True:
           
        nombre=input("ingrese nombre: ")
        nombre_check= isinstance(nombre,str)
        while nombre_check==False:
            print("no es un nombre valido, ingreselo de nuevo. \n")
            nombre=input("ingrese nombre: ")
            nombre_check= isinstance(nombre,str)
            
        apellido=input("ingrese apellido: ")
        apellido_check= isinstance(apellido,str)
        while apellido_check==False:
            print("no es un apellido valido, ingreselo de nuevo. \n")
            apellido=input("ingrese apellido: ")
            apellido_check= isinstance(apellido,str)

        ci=int(input("ingrese cedula de identidad: (sin puntos ni guiones)"))
        ci_check= isinstance(ci,int)
        while ci_check!=1:
            print("no es una cedula valida, intentelo de nuevo. \n")
            ci=int(input("ingrese cedula de identidad: "))
            ci_check= isinstance(ci,int)

        nacimiento=datetime(input("ingrese fecha de naciemiento aaaa-mm-dd: "))
        try:
            datetime.date.fromisoformat(nacimiento)
        except ValueError:
            while ValueError==True:
                print("Formato de fecha incorrecto, deberia ser aaaa-mm-dd\n")
                nacimiento=datetime(input("ingrese fecha de ingreso aaaa-mm-dd: \n"))
        
        ingreso=datetime(input("ingrese fecha de ingreso aaaa-mm-dd: \n"))
        try:
           datetime.date.fromisoformat(ingreso)
        except ValueError:
            while ValueError==True:
                print("Formato de fecha incorrecto, deberia ser aaaa-mm-dd\n")
                ingreso=datetime(input("ingrese fecha de ingreso aaaa-mm-dd: \n"))
        
        celular=int(input("ingrese telefono: "))
        celular_check=isinstance(celular,int)
        while celular_check!=1:
            print("no es un numero telefino valido, intentelo de nuevo.\n")
            celular=int(input("ingrese telefono: "))
            celular_check=isinstance(celular,int)

        tipo=input("ingrese el tipo de socio:\n1- Bonificado 2- No bonificado")
        if tipo.lower()=="1":
            print("bonificado")
        elif tipo.lower()=="2":
            print("no bofinicado")
        else:
            while tipo!="1"or"2":
                print("opcion invalida, vuelva a ingresar el tipo de socio.\n")
                tipo=input("ingrese el tipo de socio:\n1- Bonificado 2- No bonificado")

        if nombre_check and apellido_check==True and ci_check and celular_check==1 and tipo=="1"or"2":
            if datetime.date.fromisoformat(nacimiento) and datetime.date.fromisoformat(ingreso):
                print("datos ingresados correctamente.\n")
        else:
            print("hubo un error al ingresar los datos.\n")
            break

        seguir=input("desea continuar? s/n\n")
        if seguir.lower()=="s":
            continue
        elif seguir.lower()=="n":
            print("Volviendo al menu")
            break
        else:
            print("Opcion invalida, volviendo al menu")
            break

def AltaMedico():
     while True:
        nombre=input("ingrese nombre: ")
        nombre_check= isinstance(nombre,str)
        while nombre_check==False:
            print("no es un nombre valido, ingreselo de nuevo. \n")
            nombre=input("ingrese nombre: ")
            nombre_check= isinstance(nombre,str)
            
        apellido=input("ingrese apellido: ")
        apellido_check= isinstance(apellido,str)
        while apellido_check==False:
            print("no es un apellido valido, ingreselo de nuevo. \n")
            apellido=input("ingrese apellido: ")
            apellido_check= isinstance(apellido,str)

        ci=int(input("ingrese cedula de identidad (sin puntos ni guiones): "))
        ci_check= isinstance(ci,int)
        while ci_check!=1:
            print("no es una cedula valida, intentelo de nuevo. \n")
            ci=int(input("ingrese cedula de identidad: "))
            ci_check= isinstance(ci,int)

        nacimiento=datetime(input("ingrese fecha de naciemiento aaaa-mm-dd: "))
        try:
            datetime.date.fromisoformat(nacimiento)
        except ValueError:
            while ValueError==True:
                print("Formato de fecha incorrecto, deberia ser aaaa-mm-dd\n")
                nacimiento=datetime(input("ingrese fecha de ingreso aaaa-mm-dd: \n"))
        
        ingreso=datetime(input("ingrese fecha de ingreso aaaa-mm-dd: \n"))
        try:
           datetime.date.fromisoformat(ingreso)
        except ValueError:
            while ValueError==True:
                print("Formato de fecha incorrecto, deberia ser aaaa-mm-dd\n")
                ingreso=datetime(input("ingrese fecha de ingreso aaaa-mm-dd: \n"))
        
        celular=int(input("ingrese telefono: "))
        celular_check=isinstance(celular,int)
        while celular_check!=1:
            print("no es un numero telefino valido, intentelo de nuevo.\n")
            celular=int(input("ingrese telefono: "))
            celular_check=isinstance(celular,int)

        especialidad=input("ingrese la especialidad: ")
        especialidad_check= isinstance(especialidad,str)
        while especialidad_check==False:
            print("no es una especialidad valida, ingreselo de nuevo. \n")
            especialidad=input("ingrese especialidad: ")
            especialidad_check= isinstance(especialidad,str)

        if nombre_check and apellido_check==True and ci_check and celular_check==1:
            if datetime.date.fromisoformat(nacimiento) and datetime.date.fromisoformat(ingreso):
                print("datos ingresados correctamente.\n")
        else:
            print("hubo un error al ingresar los datos.\n")
            break

        seguir=input("desea continuar? s/n\n")
        if seguir.lower()=="s":
            continue
        elif seguir.lower()=="n":
            print("Volviendo al menu")
            break
        else:
            print("Opcion invalida, volviendo al menu")
            break

def AltaConsultaMedica():
     while True:
            especialidad=input("ingrese nombre de especialidad: ")
            especialiadad_check= isinstance(especialidad, str)
            while especialiadad_check==False:
                choice=int(input("""no es una especialidad valida, desea:
                      1-volver a ingresar la especialidad.
                      2-dar de alta la especialidad.\n"""))
                if choice.lower()==1:
                    especialidad=input("ingrese nombre de especialidad: ")
                    especialiadad_check= isinstance(especialidad, str)
                if choice.lower()==2:
                    AltaEspecialidad()

            nombre=input("ingrese nombre de medico: ")
            nombre_check= isinstance(nombre,str)
            while nombre_check==False:
                print("no es un nombre valido, ingreselo de nuevo. \n")
                nombre=input("ingrese nombre: ")
                nombre_check= isinstance(nombre,str)

            consulta=datetime(input("ingrese fecha de consulta aaaa-mm-dd: \n"))
            try:
                datetime.date.fromisoformat(consulta)
            except ValueError:
                while ValueError==True:
                    print("Formato de fecha incorrecto, deberia ser aaaa-mm-dd\n")
                    consulta=datetime(input("ingrese fecha de consulta aaaa-mm-dd: \n"))
            
            cantidad=int(input("cantidad de pacientes que se atenderan: "))
            cantidad_check= isinstance(cantidad,int)
            while cantidad_check!=1:
                print("no es una cedula valida, intentelo de nuevo. \n")
                cantidad=int(input("ingrese cedula de identidad: "))
                cantidad_check= isinstance(cantidad,int)
            

def EmitirTicket():
    return

def RealizarConsulta():
    return

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
            AltaEspecialidad()
        elif choice.lower()=="2":
            AltaSocio()
        elif choice.lower()=="3":
            AltaMedico()
        elif choice.lower()=="4":
            AltaConsultaMedica()
        elif choice.lower()=="5":
            EmitirTicket()
        elif choice.lower()=="6":
            RealizarConsulta()
        elif choice.lower()=="7":
            print("Saliendo...")
            break
        else:
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")
            continue

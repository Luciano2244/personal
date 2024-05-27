import datetime

class Policlínica:
    def __init__(self):
        self.especialidades = {}
        self.medicos = {}
        self.socios = {}
        self.consultas = []

    def alta_especialidad(self):
        while True:
            nombre = input("Ingrese el nombre de la especialidad: ")
            precio = input("Ingrese el precio asociado: ")
            try:
                precio = float(precio)
                if nombre and precio > 0:
                    self.especialidades[nombre] = precio
                    print("La especialidad se ha creado con éxito.")
                    break
                else:
                    print("Por favor, ingrese un nombre válido y un precio mayor que 0.")
            except ValueError:
                print("Por favor, ingrese un precio válido.")

    def alta_socio(self):
        while True:
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            cedula = input("Ingrese la cédula de identidad: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
            fecha_ingreso = input("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
            celular = input("Ingrese el número de celular: ")
            tipo = input("Ingrese el tipo de socio (1- Bonificado, 2- No bonificado): ")

            try:
                cedula = int(cedula)
                celular = int(celular)
                fecha_nacimiento = datetime.fromisoformat(fecha_nacimiento)
                fecha_ingreso = datetime.fromisoformat(fecha_ingreso)

                if tipo == "1":
                    tipo = "Bonificado"
                elif tipo == "2":
                    tipo = "No bonificado"
                else:
                    raise ValueError
                nombre_check= isinstance(nombre, str)
                apellido_check= isinstance(apellido, str)
                cedula_check=isinstance(cedula,int)
                celular_check=isinstance(celular,int)
                if nombre_check==True and apellido_check==True and cedula==1 and celular==1:
                    self.socios[cedula] = {
                        "nombre": nombre, 
                        "apellido": apellido,
                        "fecha_nacimiento": fecha_nacimiento,
                        "fecha_ingreso": fecha_ingreso,
                        "celular": celular,
                        "tipo": tipo,
                        "deuda": 0
                    }
                    print("El socio se ha creado con éxito.")
                    break
                else:
                    print("Por favor, ingrese valores válidos.")
            except ValueError:
                print("Por favor, ingrese valores válidos.")

    def alta_medico(self):
        while True:
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            cedula = int(input("Ingrese la cédula de identidad: "))
            fecha_nacimiento = datetime(input("Ingrese la fecha de nacimiento (YYYY-MM-DD): "))
            fecha_ingreso = datetime(input("Ingrese la fecha de ingreso (YYYY-MM-DD): "))
            celular = int(input("Ingrese el número de celular: "))
            especialidad = input("Ingrese la especialidad: ")

            try:
                cedula = int(cedula)
                celular = int(celular)
                fecha_nacimiento = datetime.fromisoformat(fecha_nacimiento)
                fecha_ingreso = datetime.fromisoformat(fecha_ingreso)

                if nombre and apellido and cedula > 0 and celular > 0 and especialidad:
                    self.medicos[cedula] = {
                        "nombre": nombre,
                        "apellido": apellido,
                        "fecha_nacimiento": fecha_nacimiento,
                        "fecha_ingreso": fecha_ingreso,
                        "celular": celular,
                        "especialidad": especialidad
                    }
                    print("El médico se ha creado con éxito.")
                    break
                else:
                    print("Por favor, ingrese valores válidos.")
            except ValueError:
                print("Por favor, ingrese valores válidos.")

    def alta_consulta_medica(self):
        while True:
            especialidad = input("Ingrese la especialidad: ")
            if especialidad not in self.especialidades:
                print("La especialidad no está dada de alta.")
                opcion = input("¿Desea dar de alta esta especialidad? (s/n): ")
                if opcion.lower() == "s":
                    self.alta_especialidad()
                else:
                    break
            else:
                medico_nombre = input("Ingrese el nombre del médico: ")
                medico_encontrado = False
                for medico in self.medicos.values():
                    if medico["nombre"] == medico_nombre:
                        medico_encontrado = True
                        break
                if not medico_encontrado:
                    print("Este médico no está dado de alta.")
                    opcion = input("¿Desea dar de alta este médico? (s/n): ")
                    if opcion.lower() == "s":
                        self.alta_medico()
                    else:
                        break
                else:
                    fecha = input("Ingrese la fecha de la consulta (YYYY-MM-DD): ")
                    fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
                    cantidad_pacientes = input("Ingrese la cantidad de pacientes que se atenderán: ")
                    try:
                        cantidad_pacientes = int(cantidad_pacientes)
                        self.consultas.append({
                            "especialidad": especialidad,
                            "medico": medico_nombre,
                            "fecha": fecha,
                            "cantidad_pacientes": cantidad_pacientes
                        })
                        print("La consulta se ha creado con éxito.")
                        break
                    except ValueError:
                        print("Por favor, ingrese un valor numérico para la cantidad de pacientes.")

    def emitir_ticket_consulta(self):
        especialidad = input("Ingrese la especialidad: ")
        if especialidad not in self.especialidades:
            print("La especialidad no está dada de alta.")
            opcion = input("¿Desea dar de alta esta especialidad? (s/n): ")
            if opcion.lower() == "s":
                self.alta_especialidad()
            else:
                return

        print("Consultas disponibles para la especialidad", especialidad)
        for i, consulta in enumerate(self.consultas, start=1):
            if consulta["especialidad"] == especialidad:
                print(f"{i}. Médico: {consulta['medico']}, Fecha: {consulta['fecha']}")

        while True:
            opcion = input("Seleccione el número de atención deseado: ")
            try:
                opcion = int(opcion)
                if 1 <= opcion <= len(self.consultas):
                    numero_consulta = opcion - 1
                    consulta = self.consultas[numero_consulta]
                    print(f"Ha seleccionado la consulta del médico {consulta['medico']} el {consulta['fecha']}.")
                    break
                else:
                    print(f"La opción ingresada no es válida. Debe ser un número entre 1 y {len(self.consultas)}.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def menu_principal(self):
        while True:
            print("\nMenú principal:")
            print("Seleccione una opción del menú:")
            print("1. Dar de alta una especialidad")
            print("2. Dar de alta un socio")
            print("3. Dar de alta un médico")
            print("4. Dar de alta una consulta médica")
            print("5. Emitir un ticket de consulta")
            print("6. Salir del programa")

            opcion = input("Opción: ")
            if opcion == "1":
                self.alta_especialidad()
            elif opcion == "2":
                self.alta_socio()
            elif opcion == "3":
                self.alta_medico()
            elif opcion == "4":
                self.alta_consulta_medica()
            elif opcion == "5":
                self.emitir_ticket_consulta()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("La opción seleccionada no es válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    poli = Policlínica()
    poli.menu_principal()
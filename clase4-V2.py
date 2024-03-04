def ValNumInt(x):
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            return ValNumInt(input('Debe ingresar un dato numérico: '))
class Paciente:
    def __init__(self):
        self.__nombre = "juanita"
        self.__cedula = int
        self.__genero = ""
        self.__servicio = ""
        
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema():
    def __init__(self):
        self.__lista_pacientes = []
      
    def eliminarPaciente(self,c):
        if self.verDatosPaciente(c):
            pass
      
    def verificarPac(self,ced):
        encontrado =  False
        for p in self.__lista_pacientes:
            if ced == p.verCedula():
                encontrado = True
                break
        return encontrado

    def ingresarPaciente(self,pac):
        if self.verificarPac(pac.verCedula()):
            return False
        self.__lista_pacientes.append(pac)
        return True

    def verDatosPaciente(self,c):
        if self.verificarPac(c) == False:
            return None
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes")
        return len(self.__lista_pacientes)
    
    def BuscarPaciente(self, key):
        patients_found = []
        if key == "":
            return patients_found  # Retorna una lista vacía si la clave de búsqueda está vacía
        for p in self.__lista_pacientes:
            if str(key).lower() in p.verNombre().lower() or str(key) == str(p.verCedula()):
                patients_found.append(p)
        return patients_found
        
def main():
    sis = Sistema()
    while True:
        #opcion = int(input("Ingrese 0 para volver al menu, 1 para ingresar nuevo paciente, 2 ver paciente: , 3 - ver cantidad de pacientes "))
        #hay que validar el menú?
        #lo hago por si acaso
        opcion = ValNumInt(input("""
                                 Eliga la opción que desea ejecutar:
                                 0. Volver al menu
                                 1. Ingresar nuevo paciente
                                 2. Ver paciente(s)
                                 3. Ver cantidad de pacientes
                                 -> """))
        if opcion == 1:
            print("A continuacion se solicitaran los siguientes datos:")
            # 1 Se solicitaran los datos
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))    
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            # 2 se crea un objeto Paciente
            pac = Paciente()
            # como es paciente esta vacio debo ingresarle la informacion
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            r = sis.ingresarPaciente(pac)
            # 3 se almacena en la lista que esta dentro de la clase sistema

            if r == True:
                print("paciente ingresado")
            else:
                print("paciente ya existe en el sistema")

        elif opcion == 2:
            # solicito la cedula o el nombre que quiero buscar:
            key_busqueda = input('Ingrese la cédula o el nombre del paciente a buscar: ')
            # Buscamos en la bd
            resultado_pacientes = sis.BuscarPaciente(str(key_busqueda))
            if not resultado_pacientes:
                print("El paciente no se encontró")
            else:
                print('Pacientes encontrados: ')
                for paciente in resultado_pacientes:
                    print("Nombre: " + paciente.verNombre())
                    print("Cedula: " + str(paciente.verCedula()))
                    print("Genero: " + paciente.verGenero())
                    print("Servicio: " + paciente.verServicio())
        
        elif opcion == 3:
            print(f"la cantidad de pacientes en el sistema es: {sis.verNumeroPacientes()}")
                    
        elif opcion != 0:
            continue
        else:
            break

if __name__ == '__main__':
    main()
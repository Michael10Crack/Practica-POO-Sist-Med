import re

def validarFecha(fecha):
    #El formato deseado de fecha es dia/mes/año
    patron = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    return patron.match(fecha)
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    def eliminarMedicamento(self, nombre_medicamento):
        m = Mascota
        for medicamento in self.__lista_medicamentos:
            if m.verNombre() == nombre_medicamento:
                self.__lista_medicamentos.remove(medicamento)
                return True
        return False

    
class sistemaV:
    def __init__(self):
        self.__mascotas_caninos = {}
        self.__mascotas_felinos = {}
    
    def verificarExiste(self,historia):
        if historia in self.__mascotas_caninos or historia in self.__mascotas_felinos:
        #solo luego de haber recorrido todo el ciclo se retorna False
            return True
        return False
        
    def verNumeroMascotas(self):
        return len(self.__mascotas_caninos) + len(self.__mascotas_felinos)
    
    def ingresarMascota(self,m = Mascota):  #asigno la variable m la clase Mascota para que se llamen correctamente los métodos
        if m.verTipo() == 'canino':
            self.__mascotas_caninos[m.verHistoria()] = m
        elif m.verTipo() == 'felino':
            self.__mascotas_felinos[m.verHistoria()] = m
   

    def verFechaIngreso(self,historia):
        m = Mascota
        pet = self.__mascotas_caninos.get(historia, None)
        if pet:
            return m.verFecha()
        pet = self.__mascotas_felinos.get(historia, None)
        if pet:
            return m.verFecha()
        return None

    def verMedicamento(self,historia):
        m = Mascota
        pet = self.__mascotas_caninos.get(historia, None)
        if pet:
            return m.verLista_Medicamentos()
        pet = self.__mascotas_felinos.get(historia, None)
        if pet:
            return m.verLista_Medicamentos()
        return None
        
    
    def eliminarMascota(self, historia):
        if historia in self.__mascotas_caninos:
            del self.__mascotas_caninos[historia]
            return True
        elif historia in self.__mascotas_felinos:
            del self.__mascotas_felinos[historia]
            return True
        return False

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento de una mascota 
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (canino o felino): ")
                peso=float(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                if not validarFecha(fecha):
                    print('ERROR- El formato de la fecha es incorrecto. Debe ser dia/mes/año')
                    continue
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha :
                print("La fecha de ingreso de la mascota es: " , fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " , numero)

        elif menu==4: # Ver medicamentos que se están administrando
            m = Mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamentos = servicio_hospitalario.verMedicamento(q) 
            if medicamentos :
                print("Los medicamentos suministrados son: ")
                for medicamento in medicamentos:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu == 6: #Eliminar medicamento de una mascota
            q = int(input('Ingrese la historia clínica de la mascota: '))
            mascota = servicio_hospitalario.__mascotas_caninos.get(q, None)
            if not mascota:
                mascota = servicio_hospitalario.__mascotas_felinos.get(q , None)
            if mascota:
                nombre_medicamento = input('Ingrese el nombre del medicamento que desea eliminar: ')
                if Mascota.eliminarMedicamento(nombre_medicamento):
                    print('Medicamento eliminado correctamente')
                else:
                    print('El medicamento no se encuentra en la lista')
            else:
                print('La historia clínica ingresada no corresponde con ninguna mascota en el sistema')

        elif menu==7: #salir
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                


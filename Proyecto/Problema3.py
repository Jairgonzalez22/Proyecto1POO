class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
class Paciente(Persona):
    def __init__(self, nombre, edad, genero, id_paciente, condicion_medica,habitacion_asignada):
        super().__init__(nombre, edad, genero)
        self.id_paciente = id_paciente
        self.condicion_medica = condicion_medica
        self.habitacion_asignada = habitacion_asignada

    def mostarPaciente(self):
     print(f'NOMBRE: {self.nombre} EDAD: {self.edad} GENERO: {self.genero} ID PACIENTE: {self.id_paciente} CONDICION MEDICA: {self.condicion_medica} HABITACION: {self.habitacion_asignada}')

class Empleado(Persona):
    def __init__(self, nombre, edad, genero, id_empleado, especialidad):
        super().__init__(nombre, edad, genero)
        self.id_empleado = id_empleado
        self.especialidad = especialidad

  

class Medico(Empleado):
    def __init__(self, nombre, edad, genero, id_empleado, especialidad,pacientes):
        super().__init__(nombre, edad, genero, id_empleado, especialidad)
        self.pacientes = pacientes
        self.__especialidad = especialidad

    def CambiarEspecialidad(self):
        cambio = input("ingrese la contraseña IMMS para cambiar la especialidad Dr:")
        if cambio == "Dotor12":
            especialidad= str(input())
            self.__especialidad = especialidad
        else:
            print("VUELVA A INTENTARLO,ERROR")
        

    def mostarMedico(self):
        print(f'NOMBRE: {self.nombre} EDAD: {self.edad} GENERO: {self.genero} ID EMPLEADO: {self.id_empleado} ESPECIALIDAD: {self.__especialidad} PACIENTES {self.pacientes} ')





#pacientes
print("...............................PACIENTES...............................................")
p1 = Paciente("MARIA LOPEZ", 45, "Femenino", "654321", "DIABETES", "101")
p1.mostarPaciente()
p2 = Paciente("EMMANUEL QUEVEDO", 89, "MASCULINO", "651555", "TORCEDURA", "10")
p2.mostarPaciente()
p3 = Paciente("KENIA VALDOVINOS", 25, "Femenino", "21997", "FRACTURA", "1")
p3.mostarPaciente()
print("........................................................................................")

#medicos
print(".................................MEDICOS................................................")
m1 = Medico("Carlos Ramirez", 40, "Masculino", "987654", "Cardiología", "7")
m1.mostarMedico()
m1.CambiarEspecialidad()
m1.mostarMedico()
m2 = Medico("VALDO HURTADO", 48, "Masculino", "8688584", "UROLOGIA", "8")
m2.mostarMedico()
m2.CambiarEspecialidad()
m2.mostarMedico()
print("........................................................................................")





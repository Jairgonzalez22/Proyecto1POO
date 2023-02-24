class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_edad(self, edad):
        self.edad = edad
        
    def get_nombre(self):
        return self.nombre
        
    def get_edad(self):
        return self.edad
    
    def mostrar_persona(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}")
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
    
    def es_mayor_que(self, otra_persona):
        if self.edad > otra_persona.get_edad():
            return True
        else:
            return False

# Personas
pers1 = Persona("valdo", 29)
pers2 = Persona("jenifer", 15)
pers1.mostrar_persona()
pers2.mostrar_persona()

#método para ver si es menor de edad
print(f"{pers1.get_nombre()} es mayor de edad: {pers1.es_mayor_de_edad()}")
print(f"{pers2.get_nombre()} es mayor de edad: {pers2.es_mayor_de_edad()}")

#método para ver quien es mayor
print(f"{pers1.get_nombre()} es mayor que {pers2.get_nombre()}: {pers1.es_mayor_que(pers2)}")
print(f"{pers2.get_nombre()} es mayor que {pers1.get_nombre()}: {pers2.es_mayor_que(pers1)}")

        
    

class persona:
     
    def __init__(self,nombre,edad,DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
    
        
    def mostar(self):
            print(f"Nombre: {self.nombre}, tengo {self.edad} y mi DNI ES {self.DNI}")


    def esMayordeEdad(self):
        if self.edad >= 60:
            return "Es mayor de edad"
        else:
            return "Es menor de edad"

pe1=persona("porfirio",89,767678)
pe1.mostar()
print(pe1.esMayordeEdad())
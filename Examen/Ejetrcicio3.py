class Animal:
    def __init__(self,nombre,raza,desplazar,patas):
        self.nombre=nombre
        self.raza=raza
        self.desplazar=desplazar
        self.patas=patas

    def HacerRuido(self):
        print(f"{self.nombre}  {self.desplazar} y tiene {self.patas} ")

    

class Perro(Animal):
    def __init__(self, nombre, raza, desplazar, patas):
        super().__init__(nombre, raza, desplazar, patas)
    
        

    def HacerRuido(self):
        print(f"El perro de nombre {self.nombre} está ladramndo y tiene {self.patas} patas")
        return super().HacerRuido()
    
class Pajaro(Animal):
    def __init__(self, nombre, raza, desplazar, patas):
        super().__init__(nombre, raza, desplazar, patas)
        self.patas=patas
   

    def HacerRuido(self):
        print(f"El pajaro de nombre {self.nombre} está volando y tiene {self.patas} patas")
        return super().HacerRuido()

can1=Perro("Lau","Aleman","Ladra",4)
can1.HacerRuido()
paj1=Pajaro("Piolin","","Vuela",2)
paj1.HacerRuido()
    

class Vehiculo:
    
    def __init__(self,marca,modelo,fuel_nivel_actual):
        self.marca=marca
        self.modelo=modelo
        self.fuel_nivel_actual=fuel_nivel_actual
        self.fuel_maximo=10
        self.conduzco=False
        self.cras=False
        self.estropeado=False
        self.fuel_minimo=5
    def conducir(self):
        if self.cras==True or self.estropeado==True  :
            print("No puedo conducir")
            
        elif self.fuel_nivel_actual < 5:
            print("Llenar deposito")
            self.llenar_deposito()
        else:
            print("Puedo conducir")
           

    def llenar_deposito(self):
            self.fuel_maximo=10
        
            self.conduzco=True
            print("Echo gasolina y puedo conducir")


    def chocar(self):
        if self.cras()==True:
            self.conduzco=False
            print("No podemos conducir")
        else:
            print("Podemos conducir")
    def averiado(self):
        
        if self.estropeado ==True:
            self.conduzco=False
            print("Vehiculo averiado")
        else:
            print("No averiado")

if __name__=="__main__":
    
    veh1=Vehiculo("Focus","XX4",6)
    veh1.cras=False
    veh1.estropeado=True
    veh1.conducir()
    
    




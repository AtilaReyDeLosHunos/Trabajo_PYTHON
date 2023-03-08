class Vehiculo:
    
    def __init__(self,marca,modelo,fuelnivelactual,ruedas,color):
        self.marca=marca
        self.modelo=modelo
        self.fuelnivelactual=fuelnivelactual
        self.ruedas=ruedas
        self.color=color
        self.fuel_maximo=10
        self.conduzco=False
        self.estropeado=False
        self.fuel_minimo=5
    def conducir(self):
        if  self.estropeado==True  :
            print("No puedo conducir")
            
        elif self.fuel_nivel_actual < 5:
            print("Llenar deposito")
            self.llenar_deposito()


        else:
            print("Puedo conducir")
            self.fuelnivelactual=self.fuelnivelactual -1
            print(self.fuelnivelactual)

    def llenar_deposito(self):
            self.fuel_maximo=10
        
            self.conduzco=True
            print("Echo gasolina y puedo conducir")


    def averiado(self):
        
        if self.estropeado ==True:
            self.conduzco=False
            print("Vehiculo averiado")
        else:
            print("No averiado")
    def numeroderuedas(self):
        print("Este vehiculo tiene un múmero diferente de ruedas")
class Camion(Vehiculo):
    def __init__(self,marca,modelo,fuelnivelactual,ruedas,color,cabina=True):
        super().__init__(marca,modelo,fuelnivelactual,ruedas,color)
        self.cabina=cabina
    def dormir(self):
        
        if self.cabina==True:
            print("Estoy parado y puedo dormir en el camion")
        else:
            print("Estoy conduciendo el camion")
    def numeroderuedas(self):
        #return super().numeroderuedas()
        print(f"el camion tiene {self.ruedas} ruedas")
    
class Moto(Vehiculo):
    def __init__(self,marca,modelo,fuelnivelactual,ruedas,color,cadena,manillar):
        super().__init__(marca,modelo,fuelnivelactual,ruedas,color)
        self.cadena=cadena
        self.manillar=manillar
    def hacer_caballito(self):
        print("Con la moto puedo hacer el caballito")
    def numeroderuedas(self):
        #return super().numeroderuedas()
         print(f"la moto tiene {self.ruedas} ruedas")
def cantidadderuedas(tipovehiculo):
    tipovehiculo.numeroderuedas()



if __name__=="__main__":
    
    veh1=Vehiculo("Focus","XX4",1,4,"Azul")
    veh1.estropeado=False
    veh1.llenar_deposito()
    cantidadderuedas(veh1)
    cam=Camion("Pegaso","cxe4",10,8,"Verde",cabina=True)
    print(cam.dormir())
    cantidadderuedas(cam)
    mot1=Moto("bultaco","fgre",15,2,"Amarillo",8,120)
    cantidadderuedas(mot1)
    print(mot1.hacer_caballito())

    
    
   
    
    




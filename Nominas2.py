class Empleado():
    
    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario
        
    def visualizar_datos(self):
        
        print(f"El empleado {self.nombre} su salario es {self.salario} y el sueldo {self.salario * 1.1}")
    
       
    

class Programador(Empleado):
    def __init__(self, nombre, salario,lenguaje_de_programacion):
        super().__init__(nombre, salario)
        self.lenguaje_de_programacion=lenguaje_de_programacion
    def visualizar_datos(self):
            if self.lenguaje_de_programacion=="Java":
                plus_pro=self.salario * 1.2
                print(f"El Programador {self.nombre} su salario es {self.salario} y el sueldo {plus_pro}")
            else:
                plus_pro=self.salario * 1.1
                print(f"El Programador {self.nombre} su salario es {self.salario} y el sueldo {plus_pro}")

class Analista(Empleado):
    def __init__(self, nombre, salario,plus):
        super().__init__(nombre, salario)
        self.plus=plus
    

    def visualizar_datos(self):
         print(f"El Analista {self.nombre} su salario es {self.salario} y el sueldo {self.salario + self.plus}")

def totalsueldo(tipoempleado):
    tipoempleado.visualizar_datos()

empleados=[]

emp1=Empleado("Peio",1200)
emp2=Empleado("Juan",4500,)
totalsueldo(emp1)
totalsueldo(emp2)
empleados.append(f"El empleado de nombre: {emp1.nombre} y sueldo {str(emp1.salario)}")
empleados.append(f"El empleado de nombre: {emp2.nombre} y sueldo {str(emp2.salario)}")
pro1=Programador("Pepe",1200,"Java")
pro2=Programador("Felipe",2500,"Python")
totalsueldo(pro1)
totalsueldo(pro2)
empleados.append(f"Nombre del programador: {pro1.nombre},con un salario de {str(pro1.salario)} y su lenguaje de programacion es : {pro1.lenguaje_de_programacion}")
empleados.append(f"Nombre del programador: {pro2.nombre},con un salario de {str(pro2.salario)} y su lenguaje de programacion es : {pro2.lenguaje_de_programacion}")

an1=Analista("Paco",1200,200)
an2=Analista("Maria",5400,1200)
totalsueldo(an1)
totalsueldo(an2)
empleados.append(f"Nombre del analista: {an1.nombre}, con un salario de {str(an1.salario)} y un plus de {str(an1.plus)}")
empleados.append(f"Nombre del analista: {an2.nombre}, con un salario de {str(an2.salario)} y un plus de {str(an2.plus)}")

for i in empleados:
    print(i)



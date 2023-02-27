Alumnos=["Arturo","Julio","Dani"]
Contador = 0
print("Consulta de asistencia")
for i in range(len(Alumnos)):

    Asistencia=input(f"El alumno {Alumnos[i]} está en clase (s/n)")
    
    
    if Asistencia =="s":
        print(f"El alumno {Alumnos[i]}  está en clase")
        Contador +=1
   
    elif Asistencia=="n":  
        print(f"El alumno {Alumnos[i]} no está en clase") 
    else:
        print("Tienes que teclear s o n")

print(f"Hay {Contador} alumno/s")
if Contador==0:
    print("Ningun alumno")





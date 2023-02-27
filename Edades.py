Datos={}
numero=0
respuesta="S"
while respuesta=="S":
    Nombre=(input("Teclea tu nombre: "))
    edad=int(input("Teclea tu edad: "))
    if Nombre in Datos:
        print("Nombre repetido")
        print("Error")
        print("Teclea de nuevo el nombre")
 
    elif edad < 18 or edad > 65:
        print("La edad debe estar entre 18 y 65 años")
        print("Teclea de nuevo la edad")      
        
    else:
        Datos[Nombre]=edad
        numero=numero+1
        respuesta=input("Deseas introducir otros datos(S/N)")
print(f"Los datos introducidas son {Datos}, y el número de veces de edades es {numero}" )




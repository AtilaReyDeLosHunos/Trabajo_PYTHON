
respuesta="S"

while respuesta=="S":
    nombre=input("Teclea tu nombre(mayor de 5 letras)")
    mayusculas=nombre.capitalize()
    clave=input("Teclea tu clave")
    if len(nombre) <5 or len(clave)<6 or clave =="123456" or clave=="password" or clave=="contraseña":
        
        print("Error")
        respuesta=input("Deseas cambiar los datos(S/N)")
    else:
        respuesta=input("Deseas introducir otros datos(S/N)")
        print(f"El nombre es: {nombre} y la clave es: {clave}")
        print(f"Bienvenido {mayusculas}")

    






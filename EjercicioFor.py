"""nombre = input("¿Cúal es tu nombre?")

for i in range(50):
    
    print(nombre)"""
accion = input("¿Teclear 'up' para contar en positivo desde cero o teclear 'down' para contar en negativo?")
if accion=="up":
    numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))
    for i in range(numeros_de_veces):
        print(i)
if accion=="down":
    numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))
    for i in range(numeros_de_veces,0,-1):
        print(i)

    


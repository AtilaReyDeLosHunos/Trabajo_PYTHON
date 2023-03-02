invitados=[]
gente=int(input("¿Cuanta gente acudirá a la fiesta?"))
MAX_INVITADOS=5
if gente > MAX_INVITADOS:
    print(f"Lo siento, solo {MAX_INVITADOS} personas pueden acudir a la fiesta ")
else:
    for i in range(gente):
        nombre=input("Tu nombre es: ")
        invitados.append(nombre)   
        print(nombre)
print(invitados)

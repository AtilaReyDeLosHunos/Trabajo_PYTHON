"""sueldo=float(input("Tu sueldo"))
valor=input("soy experto de Python")
if valor=="Si":
    sueldo=sueldo *10
else:
    sueldo
print(sueldo)"""


"""Total=0
Valor1=float(input("Primer número"))
Valor2=float(input("Segundo número"))
Total=Valor1+Valor2
print(Total)"""

"""Accion1=3.1453
Accion2=2.987
Accion3=3.5
print(round(Accion1,0))
print(round(Accion2,0))
print(round(Accion3,0))"""

"""TotalCena=float(input("Total de la cena: "))
NumeroDePersonas=int(input("Numero de personas: "))
PagoIndividual=TotalCena/NumeroDePersonas
print(round(PagoIndividual,2))"""


accion=input("Salir (q)")
while accion !="q":
    valor=input("deseas calcular de kilos a libras(k)o viceversa(l): ")

    if valor=="k":
        pesoKilos=float(input("Teclea tu peso en Kilos: "))
        pesoenlibras=pesoKilos*2.20462
        print(pesoKilos," kilos son ",  round(pesoenlibras)," libras")
    else:
        pesoLibras=float(input("Teclea tu peso en libras: "))
        pesoenKilos=pesoLibras/2.20462
        print(pesoLibras," libras son ", round(pesoenKilos),"kilos")
    accion=input("Salir (q)")


    



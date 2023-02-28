"""def calcular_cuenta(cuenta,propina=12):
    total=cuenta *(1+0.01 *propina)
    total=round(total,2)
    return total
    
if __name__=="__main__":
    total1=calcular_cuenta(100)
    print(f"Hay que pagar: ${total1} ")

    total1=calcular_cuenta(100,10)
    print(f"Hay que pagar: {total1}")"""

def imprimirDiasSemana(*args):
    contador=1
    for i in args:
        print(f" {i} es el {contador} dia de la semana")
        contador +=1

if __name__=="__main__":
    imprimirDiasSemana("Lunes","Martes","Miercoles","Jueves","Viernes")
    print("-" *10)
    imprimirDiasSemana("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
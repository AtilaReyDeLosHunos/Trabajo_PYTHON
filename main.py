from comun.calculo import *

#print (dir())
if __name__=="__main__":
    print(sumar(10,2))
    print(restar(10,2))

from comun.pedir_usuario import *
if __name__=="__main__":
    usuario=get_usuario()
    edad=get_edad()
    password=get_password()
print(f"Mi nombre es: {usuario} mi edad es. {edad} y mi clave es: {password}")
from comun.repetir_numero import *
if __name__=="__main__":
    print("Un programa para repetir un numero")
numero=get_numero()
repetir_numero(numero)

from comun.fun_tiempo import *

import time
DORMIR=10
if __name__=="__main__":
    time.sleep(DORMIR)
    msg()
    time.sleep(DORMIR)
    msg_medio()
    time.sleep(DORMIR)
    msg_final()

from comun.calculo_area import *
if __name__=="__main__":
    ancho=float(input("Teclea la base: "))
    largo=float(input("Teclea la altura: "))
    s=area(base,altura)
    print(s)







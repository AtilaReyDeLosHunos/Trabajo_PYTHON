LISTA_DE_ERRORES=["123456","password","Password","contraseña"]
nombre_valido=False
clave_valida=False

def validar_nombre(nombre):
    entero = int(len(nombre))
    return entero > 5

def validar_clave(clave):
    longitud=int(len(clave))
    if clave not in LISTA_DE_ERRORES and longitud > 6:
        return " "      
        
while not nombre_valido:
    nombre=input("Teclea tu nombre(mayor de 5 letras)")
    nombre_valido=validar_nombre(nombre)
    longitud_nombre=len(nombre)
    if not nombre_valido:
        print('Lo siento, el nombre no es válido, vuelva a intentarlo: ')

while not clave_valida:
    clave=input("Teclea tu clave: ")
    clave_valida=validar_clave(clave)
    longitud_clave=len(clave)
    if not clave_valida:
         print('Lo siento, la clave no es válido, vuelva a intentarlo: ')

print(f'El nombre {nombre} de {longitud_nombre} letras, es válido.', end="\n")
print(f'La clave {clave}  de {longitud_clave} digitos es válida.', end="\n")   

    






texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
texto=texto.replace("Pitón","Python")

texto=texto.replace("Bill Gates","Guido Van Rossum")

texto=texto.replace("1960","1989")

texto=texto.replace("difícil","fácil")
print(texto)
texto5 = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "
valor1=texto5.count("Python")
print(valor1)
valor2=texto5.count("python")
print(valor2)
numero_caracteres=len(texto5)
print(numero_caracteres)
BUSQUEDA="Python"
dato=texto5.find(BUSQUEDA)
print(dato)
dato1=len(BUSQUEDA)
dato2=dato+dato1
otro_dato=texto5.find(BUSQUEDA,dato2,len(texto5))
print(otro_dato)
otro_dato1=otro_dato+dato1
otro_dato2=texto5.find(BUSQUEDA,otro_dato1,len(texto5))
print(otro_dato2)
cambio=texto5.replace("Python","PYTHON")  
print(cambio)                      
if "código" in texto5:
    print("ok")                      
                    
    
    
    
    

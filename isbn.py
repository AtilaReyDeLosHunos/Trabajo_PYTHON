from is_isbn.is_isbn import is_isbn
#print(is_isbn("978-8425-331-42-8"))
lista=[]
#isbn=input("Teclea tu isbn: ")
with open("BaseDeDatos.txt","r")as f:
    
    for x in f:
        lista.append(x)

    print(lista)
    print(lista[0])
   
   
   
    
                 


    
    



    
    
    

    
"""total=0
while total<100:
    num=int(input("Teclea un número"))
    total=total+num

print("El total es: ",total)
i=100
while i>50:
    print(f"i con valor {i} es mayor o igual a 50")
    i =i-1"""
i=0
while i<100:
    for i in range(100):
        if i not in (10,20,30,40,50,60,70,80,90):
            print(i)
    i=i+1
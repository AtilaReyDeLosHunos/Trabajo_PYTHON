numeros = [1, 2, 34, 86, 4, 5, 99, 890, 45]
pares=[num for num in numeros if num % 2==0  ]
print (pares)
palabras = ['casa', 'perro', 'puerta', 'pizza']
cap = [palabra.title() for palabra in palabras]
print(cap)
help("this")
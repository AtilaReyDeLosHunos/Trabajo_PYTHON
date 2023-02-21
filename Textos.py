s="   122,Python,es,64,un,777,lenguaje   "
print(type(s))
s=s.strip()
a=s.split(",")
print(a)
print(type(a))
b=[str(i) for i in a if not i.isnumeric()]
print(b)
texto=" "
texto=" ".join(str(i) for i in b)

print(texto)
print(texto.upper())
#print(texto.lower())
print(texto.capitalize())


"""from urllib.request import urlopen
page=urlopen("http://info.cern.ch/")
content=page.read()
print(content)"""
"""import uuid
print("El UUId uuid1() es : ",end="")
print(uuid.uuid1())"""
import turtle
miTortuga=turtle.Turtle()
miVentana=turtle.Screen()
for i in range(4):
    miTortuga.forward(20)
    miTortuga.right(90)
miVentana.exitonclick()

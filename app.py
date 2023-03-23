from flask import Flask, render_template,redirect,url_for
app=Flask(__name__)

listaCoches=[]
class Coches:
    def __init__(self,id,marca,modelo,precio,imagen):
        self.id=id
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
        self.imagen=imagen

car1=Coches(1,"Ford","Focus",20500,"Ford.jpg")
car2=Coches(2,"Audi","A5",25900,"Audi.jpg")
car3=Coches(3,"Mercedes","VV",25895,"Mercedes.jpg")
car4=Coches(4,"Renault","4L",10254,"Renault.jpg")
car5=Coches(5,"Seat","Marbella",12547,"Seat.jpg")
listaCoches.append(car1)
listaCoches.append(car2)
listaCoches.append(car3)
listaCoches.append(car4)
listaCoches.append(car5)

@app.route("/")
def hola():
    
    return render_template("coches.html",cars=listaCoches)


@app.route("/coche/<int:id>")
def coche(id):
    for c in listaCoches:
        if c.id==id:
            return render_template ("coche.html", coche = c)

@app.route("/coches/")
def coches():
    
    return render_template ("coches.html", coches=listaCoches)
    



if __name__=="__main__":
    app.run()
from flask import Flask, render_template,redirect,url_for
app=Flask(__name__)
#listaPersonas=["Peio","Pedro","Pablo","Juan"]
#listaapellidos=["xx","yy","zz","ww"]
listaEmpleados=[]
class Empleado:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
@app.route("/")
def hola():
    

    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return app.send_static_file("aboutus.html")

@app.route("/adios")
def adios():
    #sHTML="<h1>Pagina añadida al render</h1>"
    #sHTML=sHTML+"<h2>Otra página añadida al render</h2>"
    
    return render_template("index1.html")

@app.route("/otravez")
def volver():
    return "Otra vez Peio"

@app.route("/personas")
def personas():
    emp1=Empleado("Peio","XX",66)
    emp2=Empleado("Pedro","YY",30)
    emp3=Empleado("Pablo","VV",40)
    emp4=Empleado("Juan","WW",50)
    emp5=Empleado("Pepe","HH",20)
    listaEmpleados.append(emp1)
    listaEmpleados.append(emp2)
    listaEmpleados.append(emp3)
    listaEmpleados.append(emp4)
    listaEmpleados.append(emp5)
    return render_template("personas.html",personas=listaEmpleados)

@app.route("/dinamica/<int:id>")
def dinamica(id):
    if id==10:
        return "Selecionada dinámica 10"
    else:
        return redirect(url_for("hola"))


if __name__=="__main__":
    app.run(debug=True)
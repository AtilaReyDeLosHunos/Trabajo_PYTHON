from flask import Flask, request, render_template,redirect
app=Flask(__name__)

@app.route("/")
def principal():
    return "Actividad Formulario Web"
@app.route("/login.html")
def login():
    return "Actividad Formulario Web"


@app.route("/web",methods=["GET","POST"])
def web():
    if request.method == "POST":
        nombre=request.form.get("txtNombre")
        email=request.form["txtEmail"]
        mensaje=request.form["txtMensaje"]
        fecha=request.form["datetime-local"]
        if nombre !="admin" or email !="admin@nz.com":
            
            sText= nombre + " , " + email + " , "+ mensaje + " , " + fecha
            with open("datos.txt","a") as f:
                 f.write(sText)
                 f.write("\n")
        
            return render_template("Actividad_Formulario_Web.html")
        else:
            return redirect("login.html")
        print(nombre)
        print(email)
        return  +nombre + email + mensaje + fecha
    else:
        return render_template("Actividad_Formulario_Web.html")
    


if __name__=="__main__":
    app.run(debug=True)

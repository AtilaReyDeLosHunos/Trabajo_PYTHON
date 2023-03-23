from flask import Flask, request, render_template,redirect,url_for
app=Flask(__name__)


@app.route("/")
def hola():
    
    return "Pagina principal -Indice"

@app.route("/form1", methods=["GET", "POST"])
def form1():
    """if request.method=="GET":
        nombre=request.args.get("txtNombre")
        email=request.args["txtEmail"]
        return render_template("form1.html?txtNombre=")+nombre"""
    if request.method == "POST":
        nombre=request.form.get("txtNombre")
        email=request.form["txtEmail"]
        if nombre == "admin":
            return render_template("admin.html")
        else:
            return redirect("login.html")
        print(nombre)
        print(email)
        return "Datos " +nombre + email
    else:
        return render_template("form1.html")

if __name__=="__main__":
    app.run(debug=True)
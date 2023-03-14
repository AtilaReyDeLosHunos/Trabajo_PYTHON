from flask import Flask,render_template, request
app=Flask(__name__)

@app.route("/")
def index1():
    return render_template("index1.html")

@app.route("/contacto", methods=["POST"])
def contacto():
    nombre=request.form.get("nombre")
    return render_template("contacto.html",nombre=nombre)

@app.route("/")
def index():
    nombre="P"
    return render_template("index.html",name=nombre)


if __name__=="__main__":
    app.run(debug=True)
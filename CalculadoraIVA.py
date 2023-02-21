from tkinter import *

ventana=Tk()
ventana.title("Cálculo del IVA")
#ventana.iconbitmap("numeroaureo.ico")

miFrame=Frame(ventana,width="650",height="350")
miFrame.pack()
miFrame.config(bg="black")


Label(miFrame,text="Calculadora IVA",font=("Arial",25,"bold")).place(x="200",y="10")
Label(miFrame,text="Sumar IVA",fg="red",font=("Arial",15,"bold")).place(x="100",y="100")
Label(miFrame,text="Precio sin IVA",font=("Arial",10,"bold")).place(x="50",y="140")
Label(miFrame,text="Porcentaje de IVA",font=("Arial",10,"bold")).place(x="50",y="200")
mitexto_sin_IVA=Entry(miFrame)
mitexto_sin_IVA.place(x="50",y="170")
mitexto_sin_IVA.config(justify="center")
mitexto_porc_IVA=Entry(miFrame)
mitexto_porc_IVA.place(x="50",y="230")
mitexto_porc_IVA.config(justify="center")

def calculoIVA():
    cantidadBruta=float(mitexto_sin_IVA.get())
    cantidadIVA=float(mitexto_porc_IVA.get())
    calculoIVA=(cantidadBruta*(cantidadIVA/100))
    calculoIVADosDe=round(calculoIVA,2)
    return variable1.set(calculoIVADosDe)
def total():
    cantidadBruta=float(mitexto_sin_IVA.get())
    cantidadIVA=float(mitexto_porc_IVA.get())
    calculoIVA=(cantidadBruta*(cantidadIVA/100))
    calculoIVADosDe=round(calculoIVA,2)
    Total=cantidadBruta+calculoIVADosDe
    return variable2.set(Total)

variable1=StringVar()
resultadoIVA=Entry(miFrame,textvariable=variable1)
variable2=StringVar()
resultadoTotal=Entry(miFrame,textvariable=variable2)
resultadoTotal.place(x="250",y="170")
resultadoTotal.config(justify="center",fg="red",font=("Arial",12,"bold"))
resultadoIVA.place(x="250",y="230")
resultadoIVA.config(justify="center",fg="red",font=("Arial",12,"bold"))



botonOperacion=Button(ventana,fg="red", text="Efectuar cálculo IVA",font=("Arial",12,"bold"),command=calculoIVA)
botonOperacion.pack()
botonOperacion2=Button(ventana,fg="red", text="Efectuar cálculo total",font=("Arial",12,"bold"),command=total)
botonOperacion2.pack()
ventana.mainloop()
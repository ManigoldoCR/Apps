from tkinter import *
from tkinter import ttk

cor1="#000000"
cor2="#13101f"
cor3="#470008"
cor4="#cfff0d"
cor5="#ffffff"

janela=Tk()
janela.title("Calc")
janela.geometry("300x400")
janela.config(bg=cor2)

frame_tela=Frame(janela,width=300,height=50,bg=cor1)
frame_tela.grid(row=0,column=0)

frame_corpo=Frame(janela,width=300,height=350,)

frame_corpo.grid(row=1,column=0)

valores=''
valor=StringVar()

def entrar_valores(event):
    global valores
    
    valores = valores +str(event)
    
    valor.set(valores)


def calcular():
    global valores
    resultado=eval(valores)
    valor.set(str(resultado))

def limpar():
    global valores
    valores=""

    valor.set("")



telaanu=Label(frame_tela,textvariable=valor,width=16,height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT,font="Ivi 22 bold",bg=cor1,fg=cor5)
telaanu.place(x=0,y=0)


b1=Button(frame_corpo,command=limpar,text="Apagar",width=20,height=4,bg=cor3,relief=RAISED,overrelief=RIDGE)
b1.place(x=0,y=0)
b2=Button(frame_corpo,command= lambda: entrar_valores("%"),text="%",width=8,height=4,bg=cor4,relief=RAISED,overrelief=RIDGE)
b2.place(x=160,y=0)
b3=Button(frame_corpo,command= lambda: entrar_valores("/"),text="/",width=8,height=4,bg=cor4,relief=RAISED,overrelief=RIDGE)
b3.place(x=235,y=0)
b4=Button(frame_corpo,command= lambda: entrar_valores("7"),text="7",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b4.place(x=0,y=72)
b5=Button(frame_corpo,command= lambda: entrar_valores("8"),text="8",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b5.place(x=84,y=72)
b5=Button(frame_corpo,command= lambda: entrar_valores("9"),text="9",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b5.place(x=160,y=72)
b6=Button(frame_corpo,command= lambda: entrar_valores("*"),text="*",width=8,height=4,bg=cor4,relief=RAISED,overrelief=RIDGE)
b6.place(x=235,y=72)
b7=Button(frame_corpo,command= lambda: entrar_valores("4"),text="4",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b7.place(x=0,y=144)
b8=Button(frame_corpo,command= lambda: entrar_valores("5"),text="5",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b8.place(x=84,y=144)
b9=Button(frame_corpo,command= lambda: entrar_valores("6"),text="6",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b9.place(x=160,y=144)
b10=Button(frame_corpo,command= lambda: entrar_valores("+"),text="+",width=8,height=4,bg=cor4,relief=RAISED,overrelief=RIDGE)
b10.place(x=235,y=144)
b11=Button(frame_corpo,command= lambda: entrar_valores("1"),text="1",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b11.place(x=0,y=216)
b12=Button(frame_corpo,command= lambda: entrar_valores("2"),text="2",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b12.place(x=84,y=216)
b13=Button(frame_corpo,command= lambda: entrar_valores("3"),text="3",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b13.place(x=160,y=216)
b14=Button(frame_corpo,command= lambda: entrar_valores("-"),text="-",width=8,height=4,bg=cor4,relief=RAISED,overrelief=RIDGE)
b14.place(x=235,y=216)
b15=Button(frame_corpo,command= lambda: entrar_valores("0"),text="0",width=20,height=4,relief=RAISED,overrelief=RIDGE)
b15.place(x=0,y=288)
b16=Button(frame_corpo,command= lambda: entrar_valores("."),text=".",width=8,height=4,relief=RAISED,overrelief=RIDGE)
b16.place(x=160,y=288)
b17=Button(frame_corpo,command=calcular,text="=",width=8,height=4,bg=cor4,relief=RAISED,overrelief=RIDGE)
b17.place(x=235,y=288)





janela.mainloop()

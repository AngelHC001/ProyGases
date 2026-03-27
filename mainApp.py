from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk 
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import tkinter as tkr
from tkinter import ttk

import gas_formula as gf

nombreGas = ""
masaGas = 0
temperatura = 0
        
def sacarFigura():
    if gf.listaGases != []:
        fig1 = gf.figurasPlot()
        
        #dibujar en frame
        canvas = FigureCanvasTkAgg(fig1, master=frame)
        canvas.get_tk_widget().grid(column=0,row=0)
        canvas.draw()
    else:
        reinicia()
    
#%% FUNCIONES

#ADQUIRIR VARIABLES DE LOS TEXTBOX
def adquirir():
    nombreGas = input1.get()
    masaGas = float(input2.get())
    temperatura = float(input3.get())
    
    nuevoGas = gf.Gas(nombreGas, masaGas, temperatura) 
    gf.listaGases.append(nuevoGas)

    sacarFigura()

    
#FUNCION DEL BOTON REINICIAR
def reinicia():
    #Vaciar lista
    gf.listaGases.clear()
    
    #reiniciar graficos
    fig0, ax = plt.subplots(figsize=(4,3))

    #reiniciar canvas
    canvas = FigureCanvasTkAgg(fig0, frame)
    canvas.get_tk_widget().grid(column=0,row=0)
    canvas.draw()
    
#FUNCION DEL BOTON ELIMINA ULTIMO    
def eliminaUltimo():
    if len(gf.listaGases) == 1:
        reinicia()
    elif gf.listaGases != []:
        gf.listaGases.pop() #elimina ultimo
        sacarFigura()
    else:
        print("LISTA VACIA")
    
#FUNCION CAMBIAR VELOCIDAD
def cambiaUnidad():
    velocidad = float(input4.get())
    gf.velocidades = gf.cambiaVel(velocidad)
    if gf.listaGases != []:
        sacarFigura()    
    
    
#FUNCION CAMBIA TEMPERATURA
maxTemp = 200
def cambiaTemperatura(nval):
    if gf.listaGases != []:
        #valor 
        f = float(nval)
        
        #Enlazar con interfaz
        fig = gf.modoTemperatura(f)
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.get_tk_widget().grid(column=0,row=0)
        canvas.draw()
         

#%% CONFIGURACION DE VENTANA
window = tkr.Tk()
window.geometry("800x600")
window.resizable(True,True)
window.title("Temperatura de Gases")

#NSEW = NORTH SOUTH EAST WEST

#Frame como container
frame = tkr.Frame(window,width=400,height=300)
frame.grid(column=0,row=0,sticky='nsew',padx=(10,10),pady=(20,20))

frame2 = tkr.Frame(window)
frame2.grid(column=1,row=0,sticky='nsew', padx=(10,10),pady=(10,10))

#SEGUNDO RENGLON
frame3 = tkr.Frame(window)
frame3.grid(column=0,row=1,sticky='nsew')

frame4 = tkr.Frame(window)
frame4.grid(column=1,row=1,sticky='nsew')


#CANVAS VACIO
fig0, ax = plt.subplots(figsize=(4,3))
canvas = FigureCanvasTkAgg(fig0, frame)
canvas.get_tk_widget().grid(column=0,row=0)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, frame3) 
toolbar.update() 

#AREA DE INPUTS
lbl1 = ttk.Label(frame2, text='Nombre del Gas:')
lbl2 = ttk.Label(frame2, text='Masa:')
lbl3 = ttk.Label(frame2, text='Temperatura:') 

input1 = ttk.Entry(frame2) 
input2 = ttk.Entry(frame2)
input3 = ttk.Entry(frame2)

btn1 = ttk.Button(frame2, text="Agregar Grafico",command=adquirir)
btn2 = ttk.Button(frame2, text="Eliminar Ultimo",command=eliminaUltimo)
btn3 = ttk.Button(frame2, text="Reiniciar",command=reinicia)

#Area de frame3
#Cambio de temperatura
lbl5 = ttk.Label(frame3, text='Cambiar temperatura')
scale1 = tkr.Scale(frame3,orient='horizontal',from_=0,to=1000,length=375,command=cambiaTemperatura)
btn5 = ttk.Button(frame3,text="Modo Normal",command=sacarFigura)

#CAMBIO DE VELOCIDAD
lbl4 = ttk.Label(frame4, text='Unidades de Velocidad (Por defecto: 2000)')
input4 = ttk.Entry(frame4)
btn4 = ttk.Button(frame4, text="Cambiar",command=cambiaUnidad)

#%% AGRUPACIONES Y FORMATOS
labels = [lbl1,lbl2,lbl3,lbl4,lbl5]
inputs= [input1,input2,input3,input4]
buttons = [btn1,btn2,btn3,btn4,btn5]

fonts = ("Segoe UI", 12)

for lb in labels:
    lb['font'] = fonts
    
for ip in inputs:
    ip['width'] = 30
    lb['font'] = fonts


#%% LAYOUT

#FRAME 2
frame2.grid()

lbl1.pack(anchor=tkr.W, pady=5)
input1.pack(anchor=tkr.W, padx=10, pady=5)

lbl2.pack(anchor=tkr.W, pady=5)
input2.pack(anchor=tkr.W, padx=10, pady=5)

lbl3.pack(anchor=tkr.W, pady=5)
input3.pack(anchor=tkr.W, padx=10, pady=5)

btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)

#FRAME 3
toolbar.pack(side=tkr.TOP,fill=tkr.X)

lbl5.pack()
scale1.pack()
btn5.pack()

#FRAME 4
lbl4.pack(anchor=tkr.W, pady=5)
input4.pack(anchor=tkr.W, padx=10, pady=5)
btn4.pack(side=tkr.LEFT, padx=5)
#%% RUN PROGRAM
window.mainloop()

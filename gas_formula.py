import math as ma
import numpy as np
import matplotlib.pyplot as plt

listaGases = []
velocidades = np.linspace(0, 2000, 2000) #inicial default

class Gas():
    def __init__(self):
        self.nombre = ""
        self.masa = 0
        self.temperatura = 0
        #velocidad afecta a todos
    
    def __init__(self,name,mass,temp):
        self.nombre = name
        self.masa = mass
        self.temperatura = temp
        
    def __str__(self):
        return f"{self.nombre} - {self.masa} - {self.temperatura}"
     

def cambiaVel(entrada):
    vel = float(entrada) 
    velocidades = np.linspace(0,vel, 2000) 
    return velocidades

 
#FORMULA DE LA DISTRIBUCION
def MaxwellBoltzmann(mas, vel, temp):
    m = float(mas)              #MASA DE LA PARTICULA
    v = vel                     #UNIDAD DE VELOCIDAD
    t = float(temp) + 273.15    #TEMPERATURA EN KELVIN CONVERTIDO 
    t = abs(t)
    k = 1.38e-23                #Constante de Boltzmann en J/K

    # ORGANIZAR OPERACIONES
    factor1 = (m / ((2 * ma.pi) * (k * t))) ** (3/2)    #factor1
    ex = ma.exp((-m * (v**2)) / (2 * (k * t)))        #Componente de la exponencial
    factor2 = (v**2) * ex                            #factor2

    funcion = (4 * ma.pi) * (factor1 * factor2)
    return funcion



def figurasPlot():
    #CREAR UNA FIGURA
    fig, ax = plt.subplots(figsize=(4,3))
    
    for g in listaGases:
        moleculas = [MaxwellBoltzmann(g.masa, v, g.temperatura) for v in velocidades]
        ax.plot(velocidades, moleculas, label=f"{g.nombre} {g.temperatura} K°")
    
    #legends
    fig.tight_layout()
    ax.set_title('Densidad de los gases por unidades de velocidad')
    ax.set_xlabel("Velocidad v")
    ax.set_ylabel("Numero de Moleculas")   
    ax.legend()
    
    plt.close(fig)
    return fig

def modoTemperatura(tempScale):
    #CREAR UNA FIGURA
    fig, ax = plt.subplots(figsize=(4,3))
    
    for g in listaGases:
        moleculas = [MaxwellBoltzmann(g.masa, v, tempScale) for v in velocidades]
        ax.plot(velocidades, moleculas, label=f"{g.nombre} {tempScale} K°")
    
    #legends
    fig.tight_layout()
    ax.set_title('Densidad de los gases por unidades de velocidad')
    ax.set_xlabel("Velocidad v")
    ax.set_ylabel("Numero de Moleculas")   
    ax.legend()
    
    plt.close(fig)
    return fig

## ProyGases
Un pequeño proyecto de apoyo universitario para termodinamica, se encarga de graficar la densidad de los gases en relación a su velocidad, la grafica esta basada en la formula Maxwell-Boltzmann.

Datos de la Gráfica: 
- Nombre del Gas a graficar
- Masa (ya sea en g. o en kg.)
- Temperatura (en Kelvin)
- Velocidad de las particulas (EJE X)
- Numero de Moleculas (EJE Y)

Si la gráfica es alta en una región dada, significa que hay más moléculas del gas moviéndose a esas velocidades.

#### GASES DE EJEMPLO:
[-23 en g             -26 en kg]

- nitrogeno = 4.65 * (10**-26) --> 4.6500000000000006e-26 (dato a ingresar)
- oxigeno = 5.31 * (10**-26) --> 5.31e-26
- argon = 6.47 * (10**-26) --> 6.47e-26

## Datos del Proyecto
- Lenguaje de Programación: Python
- Bibliotecas Utilizadas: tkinter (GUI), matplotlib, numpy, math

## Estructura
- mainApp.py conforma la ventana de interfaz
- gasFormula.py contiene las clases y funciones de apoyo para las operaciones
- Folder 'dist' tiene la aplicacion .exe basica (exclusivo de Windows)
- Folder 'build' contiene de compilacion para el .exe

## Modo de uso
- Introducir datos del gas (nombre, masa calculada y temperatura en K) y presiona ingresar
- La velocidad esta por defecto en 2000, introducir otra a tu gusto
- Al visualizar puedes controlar la temperatura por medio de una barra (afecta todas), toca el boton Modo normal para reiniciar
- Elimina la ultima grafica creada o bien, reinicia la visualizacion
- Vista Previa en Prev.jpg

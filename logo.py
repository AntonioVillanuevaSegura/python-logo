# -*- coding: utf-8
from turtle import *
from tkinter import *
from tkinter import ttk
from ast import literal_eval

ventana =Tk()
ventana.title("Tkinter & Turtle")

colores =["Green Yellow","Dark orange","Deep pink","Medium Slate Blue",
"Deep Sky Blue","Dark Turquoise","Spring Green","Gold","Orange Red ",
"Violet Red","Dark Violet"]

DIAMETRO =5 #Diametro de los circulos
PANTALLA=500 #Size de la pantalla Canvas 

with open('logo') as f:
	"""Abre el fichero de coordenadas x,y donde se situa el centro de cada circulo"""
	logo1=literal_eval (f.read())

def circulo():
	"""Dibuja un circulo """
	brus.begin_fill()#Rellena con un color
	brus.pendown()#Lapiz abajo
	brus.circle(DIAMETRO) 
	brus.penup()#Lapiz arriba
	brus.end_fill()#Fin de relleno

def ejecutar ():
	"""Recupera color de ComboBOX y crea dibujo"""
	c1=combo1.get()
	brus.penup()
	brus.speed(0)
	brus.clear()

	"""dibuja circulos centro segun coordenadas"""
	for x in range(len(logo1)-1,0,-1):
		brus.color(c1)
		brus.goto(logo1[x])
		circulo()

#ComboBox con la seleccion de colores   
combo1=ttk.Combobox(ventana,width=60, values=colores)
combo1.current(0) #Seleccion de color actual
combo1.grid(column=0,row=0,sticky=E+W)

#Boton ejecutar
boton_ejecutar=Button(ventana,text="Ejecutar",command=  ejecutar,height=3,cursor="hand2",activebackground="Lavender")
boton_ejecutar.grid(column=0,row=2,columnspan=2,sticky=E+W,pady=3)

canvas=Canvas(ventana,width=PANTALLA,height=PANTALLA)
canvas.grid(column=0,row=3,columnspan=2)

pantalla=TurtleScreen(canvas)
pantalla.bgcolor("black")
brus=RawTurtle(pantalla)

ventana.mainloop()


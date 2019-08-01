# -*- coding: utf-8
"""
Antonio Villanueva Segura
Crea un fichero de coordenadas desde una imagen 
"""

import sys
print (sys.version)

ESPACIO=20 #Espaciado entre los futuros circulos

coordenadas=open("logo","w+")#Fichero de coordenadas que vamos a crear

from PIL.Image import *
i=open("logo.png")#Abre la imagen en este caso logo.png
Image.show(i) #La muestra 

ancho , alto = i.size #Recupera la informacion en este caso  489x788

def recupera_pixel(x,y,ii):
	"""recupera el color de un pixel """
	print (str (type (Image.getpixel(ii, (x,y)))) ,str (Image.getpixel(ii, (x,y)))) #debug
	if  type (Image.getpixel(ii, (x,y))) is tuple:
		return Image.getpixel(ii, (x,y))[0] #Tuple solo primer valor R ...
	else:
		return Image.getpixel(ii, (x,y)) #Int


"""Bucle para analizar los pixeles de una imagen"""
for x in range(0,ancho,ESPACIO):
	for y in range (0,alto,ESPACIO):
		if recupera_pixel(x,y,i)>=254: #PIXEL BLANCO 254
			print (" ",end='')#Es blanco ?
			
		else:#OTROS COLORES NO BLANCOS
			#Escribe coordenada del pixel activo
			coordenadas.write(str ((x-(ancho//2),y-(alto//2)))+',' )
			print ("*",end='')#Hay color

	print ("\n")

i.close()
coordenadas.close()



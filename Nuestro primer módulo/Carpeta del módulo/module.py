##print('I like to be a module')
print(__name__)

"""counter = 0

if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to be a module")"""

#Si escribes un módulo lleno de varias funciones complejas,
#puedes usar la variable __name__ para colocar una serie
#de pruebas para verificar si las funciones trabajan correctamente.

##Cada vez que modifiques alguna de estas funciones, simplemente
##puedes ejecutar el módulo para asegurarte de que sus enmiendas
##no estropeen el código. Estas pruebas se omitirán cuando el código se
##importe como un módulo.

# module.py

#!/usr/bin/env python3

###! Para sistemas operativos Unix y similares a Unix (incluido MacOS), dicha línea
##indica al sistema operativo cómo ejecutar el contenido del archivo
##(en otras palabras, qué programa debe lanzarse para interpretar el texto). En algunos entornos
##(especialmente aquellos conectados con servidores web) la ausencia de esa línea causará problemas.

""" module.py - an example of Python module """

__counter = 0  #__ simplemente indica que los usuarios pueden leerla,
               #pero que no deben modificarla bajo ninguna circunstancia.

def suml(list):
	global __counter
	__counter += 1
	sum = 0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __counter	
	__counter += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

if  __name__ == "module":
	print("I prefer to be a module, but I can do some tests for you")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)

##Las funciones definidas dentro del módulo (suml() y prodl()) están disponibles para ser importadas.
##Se ha utilizado la variable __name__ para detectar cuándo se ejecuta el archivo de forma independiente.
##

# main.py

#Nota: main.py "debe" estar en la misma carpeta que module.py 

##import module
##print(module.__counter)

"""
Que ocurre si el script principal (main.py) y el módulo a importar (module.py)
se encuentran en carpetas diferentes ?:
Hay una variable especial (en realidad una lista) que almacena todas las ubicaciones
(carpetas o directorios) que se buscan para encontrar un módulo que ha sido solicitado por la instrucción import.

Python examina estas carpetas en el orden en que aparecen en la lista:
si el módulo no se puede encontrar en ninguno de estos directorios, la importación falla.

De lo contrario, se tomará en cuenta la primera carpeta que contenga un módulo
con el nombre deseado (si alguna de las carpetas restantes contiene un módulo con ese nombre, se ignorará).
"""
from sys import path

#path.append('..\\Carpeta del módulo')  #con una ruta relativa
path.append('C:\\Users\\USUARIO\Documents\\TI\Python\\Cisco\\Carpeta del módulo')#con una ruta absoluta

"""Hemos usado el método append(), la nueva ruta ocupará el último elemento en la lista de rutas;
si no te gusta la idea, puedes usar en lugar de ello el método insert()."""
import module 
#from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

print(module.__counter)

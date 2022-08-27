from sys import path

path.append('C:\\Users\\USUARIO\\Documents\\TI\Python\\Cisco\\Nuestro primer módulo\\Archivo ZIP Módulos y paquetes')
            #esta es la ruta absoluta del paquete extra, el cuál contiene el archivo vacío __init__.py que lo inicializa cuando es importado
            #cualquiera de sus módulos desde el programa. 

#acceder a la función funI() del módulo iota del paquete extra.

#OPCIÓN 1
import extra.iota
print(extra.iota.FunI())
#OPCIÓN 2

##from extra.iota import funI
##print(funI())


#acceder a los módulos sigma y tau.

#OPCIÓN 1
import extra.good.best.sigma
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())


#OPCIÓN 2 (con aliasing)
import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())

"""Supongamos que hemos comprimido todo el subdirectorio, comenzando desde la carpeta extra ( incluyéndola), y se obtuvo
un archivo llamado extrapack.zip. Después, colocamos el archivo dentro de la carpeta packages."""

#Ahora podemos usar el archivo zip en un rol de paquetes:

from sys import path

path.append('..\\Archivo ZIP Módulos y paquetes\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())

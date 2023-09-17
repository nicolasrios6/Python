# Módulos

import my_module #así se importa un modulo completo

# my_module.sum(5, 3, 1)
# my_module.printValue("Hola Python")

from my_module import suma, printValue

suma(5, 3, 1)
printValue("Hola Python")

import math 

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI

print(PI)
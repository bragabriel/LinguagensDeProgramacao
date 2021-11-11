# A função: Platform

# A função platform permite-lhe aceder aos dados da plataforma subjacente, ou seja,
#  hardware, sistema operativo, e informação da versão do intérprete.

#EX: 

from platform import *

#from platform import platform
print(platform())
print(platform(1))
print(platform(0, 1))

#from platform import machine
print(machine())

#from platform import processor
print(processor())

#from platform import system
print(system())

#from platform import version
print(version())
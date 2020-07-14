# Módulos

Para tener un mayor control sobre nuestro programa podemos separarlo en diferentes archivos con extensión `.py` y llamarlos desde un archivo, para ello se utiliza:

~~~python
import my_file #importa todo el archivo
from my_file import my_fuction_one, my_fuction_two #Importa las funciones
from my_file import my_fuction as new_fuction #Cambia el nombre a la función
from my_file import * #Importa todas las funciones
~~~

Cuando importamos sólo el archivo y queremos utilizar una función:

~~~python
my_file.my_function()
~~~

## Documentar un módulo

Un módulo se puede documentar para dar más información acerca de este.

#### Ejemplo:

~~~python
#!/usr/bin/python3 #Ubicación del archivo

"""
Aquí colocamos todo lo que hace nuestro módulo a que contexto corresponde.
"""

__author__ = "Leonel Iván Fernández Carrillo"
__copyright__ = "Sin Copyright"
__credits__ = "A mi mismo"
__license__ = "Sin licencia"
__version__ = "1.0.0"
__maintainer__ = "Leonel Fernández"
__email__ = "leonel-leonel-1@hotmail.com"
__status__ = "Estudiante"

def suma(num_one, num_two):
  """Regresa un número entero el cual es el resultado de una suma"""
  return num_one + num_two
~~~

Para acceder a la información del archivo dentro del intérprete de Python:

~~~python
help(my_file)
~~~
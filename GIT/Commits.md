## Examinar commits

`git log` muestra todos los commits hechos.

`git log --oneline` muestre todos los commits en una sola línea.

## Recuperar un archivo eliminado

`git checkout <número de commit>` moverse en el tiempo a ese commit.

`git log --oneline --name-status --diff-filter=D` enlista los commits que eliminaron archivos en una línea.

`git checkout <número de commit>^ <nombre del archivo>` recupera el archivo del commit.

## Tag en commit

`git tag <etiqueta>`agrega una etiqueta al commit. Ejemplo: "version 1".

`git tag <etiqueta> <número de commit>` agregar la etiqueta al commit especificado.

`git checkout <etiqueta>` moverse en el tiempo al commit de la etiqueta.

## Ignorar archivos

Para ignorar archivos se crea el archivo .gitignore que especifica las rutas de archivos a ignorar.

`hola.cpp` ignora el archivo.

`taks/` ignora las carpetas.

`*.php` ignora todos los archivos con terminación .php.
## Estados de GIT

- __Working directory:__ área de trabajo local, es por ello que para guardar los cambios hay que pasarlo a Staging area.
- __Staging area:__ es el área de preparación, es acá donde se almacenan todo antes de hacer un commit (confirmar cambios).
- __Git Repository:__ es el repositorio en donde se almacenan los cambios del proyecto.

## Identificarnos

`git config --global user.name "nombre"`

`git config --global user.email "<correo>"`

## Crear un repositorio

`git init`

## Agregar archivos

`git status` para ver el estado de los archivos.

`git add <archivo>` para agregar un archivo al staging area.

`git add .` para agregar todos los archivos al staging area.

`git rm --cached <archivo>` para eliminar el archivo del stating area.

`git commit` para confirmar cambios.

`git commit -m "<mensaje>"` para añadir el mensaje al commit sin abrir el archivo.

## Editar ficheros y agregarlos

`git reset HEAD <archivo>` para eliminar un archivo modificado del stating area.

## Eliminar archivos

`rm -f <archivo>` eliminar un archivo del sistema.

`git rm <archivo>` eliminar el archivo del sistema y/o pasar el archivo eliminado al staging area.

## Diferencias entre git rm --cached y git reset HEAD

`git reste HEAD` elimina el archivo del stating area pero le sigue haciendo un seguimiento a las modificaciones del archivo.

`git rm --cached <archivo>` elimina el seguimiento del archivo.

## Recuperar archivos eliminados

`git checkout -- <archivo>` para regresar los cambios hechos en el archivo.

`git reset HEAD` para regresar el archivo del stating area cuando se utilizar `git rm <archivo>`

## Mover archivos

Cuando se mueven los archivo se deben de eliminar en la carpeta vieja y agregar en la carpeta nueva.

## push y pull

`pull` obtener los cambios del repositorio

`push` agregar los cambios al repositorio.

## Crear ramas, movernos, eliminarlas

`git branch` para ver las ramas. Con el asterisco podemos saber en que rama estamos.

`git branch <nombre de la rama>` crear una nueva rama.

`git checkout <nombre de la rama>` movernos de rama.

`git chekout -b <nombre de la rama>` crear una rama y movernos a ella.

`git branch -d <nombre de la rama>` eliminar una rama.

## Eliminar ramas

`git branch -d <nombre de la rama> <nombre de la rama>` eliminar varias ramas a la vez.

## Fusionar ramas

`git merge <nombre de la rama>` agrega los cambio de la rama especificade en la rama que estamos.

## Examinar commits

`git log` muestra todos los commits hechos.

`git log --oneline` muestre todos los commits en una sola línea.

## Recuperar un archivo eliminado

`git checkout <número de commit>` moverse en el tiempo a ese commit.

`git log --oneline --name-status --diff-filter=D` enlista los commits que eliminaron archivos en una línea.

`git checkout <número de commit>^ <nombre del archivo>` recupera el archivo del commit.

## Tag en commit

`git tag <etiqueta>`agrega una etiqueta al commit. Ejemplo: "version 1".

`git tag <etiqueta> <número de commit>` agregar la etiquta al commit especificado.

`git checkout <etiqueta>` moverse en el tiempo al commit de la etiqueta.

## Ignorar archivos

Para ignorar archivos se crea el archivo .gitignore que especifica las rutas de archivos a ingnorar.

`hola.cpp` ignora el archivo.

`taks/` ignora las carpetas.

`*.php` ignora todos los archivos con terminación .php.

## Crear repositorio en GitHub y subir archivos

`git remote -v` ver si ya existe un repositorio.

`git remote add <nombre del repo> <url del repo>` añadir un repositorio.

`git push -u <nombre del repo> <nobre de la rama>` subir los archivos al repositorio.

`git push ` hace lo mismo que el comando anterior, pero el comando anterior se debe ejecutar al menos una vez.

`git puh <nombre del repo> --all` sube todas las ramas de desarrollo.
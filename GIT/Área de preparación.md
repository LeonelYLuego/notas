## Estados de GIT

- __Working directory:__ área de trabajo local, es por ello que para guardar los cambios hay que pasarlo a Staging area.
- __Staging area:__ es el área de preparación, es acá donde se almacenan todo antes de hacer un commit (confirmar cambios).
- __Git Repository:__ es el repositorio en donde se almacenan los cambios del proyecto.

## Identificarse

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

# Variables super globales

`$GLOBALS['variable']` es una forma de hacer referencia a las variables globales. 

`$_SERVER['value']` es una variable que obtiene información acerca de encabezados, rutas y ubicaciones de scripts. 

| Elemento                           | Descripción                                                  |
| ---------------------------------- | ------------------------------------------------------------ |
| `$_SERVER['PHP_SELF']`             | Devuelve el nombre del archivo del script que se está ejecutando actualmente. |
| `$_SERVER['GATEWAY_INTERFACE´]`    | Devuelve la versión de Common Gateway Interface (CGI) que el servidor está utilizando. |
| `$_SERVER['SERVER_ADDR']`          | Devuelve la dirección IP del servidor host.                  |
| `$_SERVER['SERVER_NAME']`          | Devuelve el nombre del servidor host.                        |
| `$_SERVER['SERVER_SOFTWARE']`      | Devuelve la cadena de identificación del servidor.           |
| `$_SERVER['SERVER_PROTOCOL']`      | Devuelve el nombre y la revisión del protocolo de información. |
| `$_SERVER['REQUEST_METHOD']`       | Devuelve el método de solicitud utilizado para acceder a la página. |
| `$_SERVER['REQUEST_TIME']`         | Devuelve la marca de tiempo del inicio de la solicitud.      |
| `$_SERVER['QUERY_STRING']`         | Devuelve la cadena de consulta si se accede a la página a través de una cadena de consulta. |
| `$_SERVER['HTTP_ACCEPT']`          | Devuelve el encabezado Aceptar de la solicitud actual.       |
| `$_SERVER['HTTP_ACCEPT_CHARSET'] ` | Devuelve el encabezado Accept_Charset de la solicitud actual. |
| `$_SERVER['HTTP_HOST´]`            | Devuelve el encabezado del Host de la solicitud actual.      |
| `$_SERVER['HTTP_REFERER']`         | Devuelve la URL completa de la página actual (no es confiable porque no todos los agentes de usuario lo admiten). |
| `$_SERVER['HTTPS']`                | Se consulta el script a través de un protocolo HTTP seguro.  |
| `$_SERVER['REMOTE_ADDR']`          | Devuelve la dirección IP desde donde el usuario está viendo la página actual. |
| `$_SERVER['REMOTE_HOST']`          | Devuelve el nombre del host desde donde el usuario está viendo la página actual. |
| `$_SERVER['REMOTE_PORT']`          | Devuelve el puerto que se utiliza en la máquina del usuario para comunicarse con el servidor web. |
| `$_SERVER['SCRIPT_FILENAME']`      | Devuelve la ruta absoluta del script que se está ejecutando actualmente. |
| `$_SERVER['SERVER_ADMIN']`         | Devuelve el valor dado a la directiva SERVER_ADMIN en el archivo de configuración del servidor web. |
| `$_SERVER['SERVER_PORT']`          | Devuelve el puesto en la máquina del servidor que utiliza el servidor web para la comunicación. |
| `$_SERVER['SERVER_SIGNATURE']`     | Devuelve la versión del servidor y el nombre de host virtual que se agregan a las páginas generadas por el servidor. |
| `$_SERVER['PATH_TRANSLATED']`      | Devuelve la ruta basada en el sistema de archivos al script actual. |
| `$_SERVER['SCRIPT_NAME']`          | Devuelve la ruta del script actual.                          |
| `$_SERVER['SCRIPT_URI']`           | Devuelve el URI de la página actual.                         |


`$_REQUEST['value']` obtiene el valor enviado por una página web por un form, también se pueden utiliza `$_GET['value']` y `$_POST['value']`. 
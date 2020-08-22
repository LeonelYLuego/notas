# Enlaces

Los enlaces se definen con la etiqueta `<a></a>` y su función es llevar al usuario a otra parte.

## Atributos

`href=""` especifica el destino del enlace.

| Valor                          | Ubicación                                                    |
| ------------------------------ | ------------------------------------------------------------ |
| #id                            | Vínculo a un enlace dentro de la página donde sea declarado en un id. |
| documento.html                 | Vinculo a un archivo con cualquier extensión dentro de la carpeta. |
| documento.html#id              | Vínculo a otro documento que se abre en la etiqueta id.      |
| mailto:leonelyluego@correo.com | Abre en la computadora el gestor de correos para que pueda enviar un correo a la dirección. |
| https://www.google.com         | Abre la ventana con ese link.                                |

`target=""` especifica dónde abrir el documento.

| Valor                   | Efecto                                                 |
| ----------------------- | ------------------------------------------------------ |
| _blank                  | Abre en una nueva pestaña.                             |
| _self                   | Abre en la misma pestaña.                              |
| _parent                 | Abre el documento en el parent frame.                  |
| _top                    | Abre el documento en el cuerpo completo de la ventana. |
| "Nombre de una ventana" | Abre el documento en la ventana con ese nombre.        |
| id del iframe           | Referencia al id del `<iframe>`                        |

`title=""` muestra un texto como consejo al pasar el ratón sobre el enlace.

`rel="nofollow"` indica a los buscadores que no tomen en cuenta el enlace.

## Marcadores 

Los marcadores funcionan para saltar a una parte específica de una página web, estos utilizan los atributos id en otros elementos para saltar al elemento.

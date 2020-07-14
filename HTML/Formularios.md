# Formularios

Un formulario `<form></form>` es una entrada de datos por parte del usuario, este contiene los elementos de formularios definidos por la etiqueta `<input>`. 

 ## Atributos de `<form>`

`action=""` define la acción que debe realizarse cuando se envía el formulario. Normalmente el formulario se envía a una página web. 

`target=""` donde se mostrará el resultado. 

- \_self en la misma página. 

- \_blank en otra página. 

- \_parent, \_top. 

`method=""` especifica el método HTTP para ser utilizado cuando la presentación de los datos de los formularios. 

- `get` los datos serán visible en el campo de dirección de la página. 
  - Anexa forms-datos en la URL en pares de nombre / valor. 
  - La longitud de la URL es limitada (2048 caracteres). 
  - Nunca usar GET para datos sensibles. 
  - Útil para el envió de datos donde el usuario marca el resultado. 

- `post` no muestra los datos en el URL. 
  - No tiene limitaciones de tamaño.
  - No se pueden marcar. 

`autocomplete` el navegador autocompleta los controles del formulario en base a los valores que el usuario ha introducido previamente. 

`novalidate` cuando este atributo está presente indicado que el formulario no se debe validar cuando sea enviado. 

`accept-charset` especifica el tipo de codificación de los caracteres que es aceptado. 

`enctype` especifica la codificación de los datos presentados. 

`name` especifica un nombre usado para identificar el formulario. 

 ## Elementos de un formulario

| Tipo                       | Descripción                                                 | Atributos especiales                                         |
| -------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| `<input type="text">`      | Entrada de texto de una sola línea.                         |                                                              |
| `<input type="radio">`     | Botón de radio que selecciona una de varias opciones.       | name: nombre que enlaza a los botones, checked: el elemento es seleccionado al iniciar. |
| `<input type="submit">`    | Botón de envío.                                             | value: texto que aparece en el botón.                        |
| `<input type="password"> ` | Entrada de texto de una sola línea para una contraseña.     |                                                              |
| `<input type="reset">`     | Borra todo el contenido de los elementos.                   |                                                              |
| `<input type="checkbox"> ` | Botón tipo check que puede elegir varias opciones.          | checked: el elemento es seleccionado al iniciar.             |
| `<input type="color">`     | Paleta de colores.                                          |                                                              |
| `<input type="date">`      | Selector de fecha.                                          | min, max: restricción de fecha tipo(aaaa-mm-dd).             |
| `<input type="datetime"> ` | Selector de fecha y hora.                                   |                                                              |
| `<input type="email">`     | Entrada de texto de una sola línea para correo.             |                                                              |
| `<input type="file">`      | Selección de archivo.                                       |                                                              |
| `<input type="month">`     | Selector de mes y año.                                      |                                                              |
| `<input type="number">`    | Campo de entrada de un número.                              | min, max: restricción de valores.                            |
| `<input type="range">`     | Slider para seleccionar un número.                          | min, max, step: restricciones de valores.                    |
| `<input type="search">`    | Entrada de texto de una sola línea para búsqueda.           |                                                              |
| `<input type="tel">`       | Entrada de texto de una sola línea para teléfono.           | pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}".                        |
| `<input type="time">`      | Selector de una hora.                                       |                                                              |
| `<input type="url">`       | Entrada de texto de una sola línea para una URL.            |                                                              |
| `<input type="week">`      | Permite seleccionar un semana y el año.                     |                                                              |
| `<select>`                 | Lista despegable.                                           | size: número de valores visibles, mutiple: permite selección múltiple. |
| `<option>`                 | Opción de una lista despegable de `<select>` o `<datalist>` | value: texto que se regresa como resultado, selected: opción inicial seleccionada. |
| `<textarea>`               | Campo de entrada de múltiples líneas.                       | rows: número de filas, cols: número de columnas. style="resize: none" |
| `<button>`                 | Botón.                                                      | type: tipo de botón.                                         |
| `<datalist>`               | Lista de opciones predefinidas para un elemento `<input>`.  | id: identificador de la lista para el elemento `<input>`.    |
| `<output>`                 | Resultado de un cálculo de un script.                       | for: nombre de los id de los elementos involucrados en el resultado. |

## Atributos de `<input>` 

- `name=""` nombre de controlo utilizado para identificar el elemento al momento de enviar. 
- `value=""` valor inicial del elemento. 
- `list=""` referencia al atributo id de un elemento <datalist>. 
- `disabled` deshabilita un elemento. 
- `max=""` especifica un valor máximo. 
- `maxlength=""` máximo número de caracteres. 
- `min=""` especifica un valor mínimo. 
- `pattern=""` especifica una expresión regular para verificar el valor de entrada. 
- `readonly` elemento que solo puede ser leído pero no cambiado. 
- `requiered` elemento que es requerido. 
- `size=""` especifica el ancho en caracteres. 
- `step=""` especifia los intervalos legales. 
- `autocomplete=""` un elemento debe autocompletarse. 
  - `on`
  - `off` 
- `novalidate` los datos del formulario no deben de ser validados. 
- `autofocus` elementos que deben tener el foco al cargar la página. 
- `form=""` pertenece al formulario con el id. 
- `formaction=""` especifica la dirección de la URL de un archivo que va a procesar el control de entrada cuando se envíe el formulario. Solo con type="submit" y type="image". 
- `formenctype=""` especifica como deben de ser codificados cuando se somete. Solo con type="submit" y type="image". 
- `formmethod=""` atributo define el método HTTP para enviar form-data a la URL. Solo con type="submit" y type="image". 
- `formnovalidate=""` atributo que anula la validación del formulario. Solo con type="submit". 
- `formtarget=""` especifica donde mostrar la respuesta que se recibe después de enviar el formulario. 
- `height=""` especifica la altura. 
- `width=""` especifica la anchura. 
- `multiple=""` se permite elegir más de una opción. 
- `placeholder=""` especifica una pista que describe el valor esperado. 

## Agrupación

Para agrupar ciertos elementos y clasificarlos se utiliza la etiqueta `<fieldset></fieldset>` que pondrá un borde al rededor de los elementos. Para darles un título se utiliza la etiqueta `<legend></legend>`. 
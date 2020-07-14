# Tablas

Las tablas se definen mediante la etiqueta principal `<table></table>`.

Las celdas se agrupan en filas, que se definen con la etiqueta `<tr></tr>` (table row) 

Una tabla se compone de celdas de datos. Una celda se define usando la etiqueta `<td></td>` (table data). 

Pueden existir celdas que se emplean como encabezados de filas o de columnas; estas celdas se definen con la etiqueta `<th></th>` (table heading). Este tipo de celdas suelen aparecer difinidas de las otras, normalmente con el texto en negrita. 

Las celdas pueden contener cualquier elemento HTML: texto, imágenes, enlaces e incluso otras tablas anidadas. 

## Atributos de `<table>`

`border="0"` el borde de la tabla no se tiene que dibujar y la tabal se emplea para maquetar el contenido. 

`border="1"` el borde de la tabla se tiene que dibujar y la tabla no se emplea para maquetar el contenido, sino para mostrar datos tabulados. 

`cellpadding="n"` modifica la distancia en pixeles existente entre el borde de una celda y su contenido, el valor por defecto es 1 

`cellspacing="n"` modifica la distancia en pixeles existen entre los bordes de dos celdas contiguas, el valor por defecto es 2 

## Atributos de `<td>` `<th>` `<tr>`

`colspan=""` colapsa las columnas en una. 

`rowspan=""` colapsa las filas en una. 

## Otras etiquetas

`<caption></caption>` define el titulo de la tabla. 

`<thead></thead>` agrupa las filas que forma la cabecera de la tabla. 

`<tbody></tbody>` agrupa las filas que forman el cuerpo de la tabla. 

`<tfoot></tfoot>` agrupa las filas que forman el pie de la tabla. 
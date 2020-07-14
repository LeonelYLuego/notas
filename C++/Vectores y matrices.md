# Vectores y matrices

| Código                                                       | Definición                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `vector<tipo> nombre([tamaño, [valor]]);`                    | Crea un nuevo vector                                         |
| `vector<int> nombre;`                                        | Vector con ceros elementos                                   |
| `v = m;`                                                     | Pasar todo el contenido de un vector a otro                  |
| `nombre[i]++;`                                               | Obtener dato sin verificación de rango                       |
| `nombre.at(i)++;`                                            | Obtener dato con verificación de rango                       |
| `nombre.push_back(dato);`                                    | Ingresa un dato al vector                                    |
| `nombre<tipo>::iterator nombre;`                             | Crea un iterador para los vectores (Guarda la dirección de los datos del vector) |
| `nombre.begin();`                                            | Te da la dirección del primer valor del vector               |
| `nombre.end();`                                              | Te da la dirección del valor siguiente al ultimo             |
| `nombre.rbegin();`                                           | Te da la dirección del ultimo valor                          |
| `nombre.rend();`                                             | Te da la dirección del valor antes del primero               |
| `nombre.fornt();`                                            | Te da el primer valor del vector                             |
| `nombre.back();`                                             | Te regresa el ultimo valor del vector                        |
| `nombre.size();`                                             | Conocer el tamaño de un vector                               |
| `nombre.resize(tamaño);`                                     | Modifica el tamaño de un vector                              |
| `nombre.empity();`                                           | Saber si un vector esta vacío, true = vacío, false = tiene algún valor |
| `nombre.pop_back();`                                         | Elimina el ultimo valor del vector                           |
| `nombre.erase(inicio, fin);`                                 | Elimina los datos desde una dirección hasta otra             |
| `nombre.clear();`                                            | Borra todos los elementos de un vector                       |
| `nombre.find(inicio, fin, n);`                               | Encuentra la dirección del un valor que busquemos desde una dirección de inicio hasta una final, incluir `<algorithm>` |
| `nombre.insert(inicio, cantidad, dato);`                     | Ingresa un dato desde una dirección de inicio hasta la cantidad de datos |
| `map<tipo1, tipo2> nombre;`                                  | Con la librería map `<map>` podemos cambiar el topo de dato del subíndice donde primero definimos el tipo de datos del vector |
| `map<tipo1, tipo2>::iterator nombre;`                        | Crear un iterador para un vector tipo map                    |
| `string::iterator nombre;`                                   | Crear un iterador para un vector tipo string                 |
| `string::reverse_iterator`                                   | Crea un iterador inverso para un vector de tipo string       |
| `vector<vector<tipo>> nombre;`                               | Vector bidimensional sin cantidad de datos                   |
| `vector<vector<tipo>> nombre(datos1, vector<tipo> (datos2));` | Vector bidimensional con cantidad de datos                   |
| `for_each(nombre.begin(), nombre.end, nombre_funcion); void nombre_funcion(tipo nombre){ }` | Se debe crear una función con un nombre la cual se repetirá por cada uno de los datos de la matriz que se encuentra en `<algorithm>` |


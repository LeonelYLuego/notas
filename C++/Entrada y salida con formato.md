# Entrada y salida con formato

| Formato             | Definición                                                   |
| ------------------- | ------------------------------------------------------------ |
| `boolalpha`         | Permitir mostrar los valores de tipo bool en formato alfabético; esta operación se desactiva con `noboolalpha` |
| `showbase`          | Permite mostrar las constantes numéricas precedidas por un digito distinto de 0, por 0, o por 0x, según se especifique en base 10, 8 0 16, respectivamente; esta operación se desactiva con `noshowbase` |
| `showpoint`         | Forzar que se muestre el punto decimal y los 0 no significativos en valores expresados con coma flotante; se desactiva con `noshowpoint` |
| `showpos`           | Mostrar el + para los valores positivos; esta operación se desactiva con `noshowpos` |
| `skipws`            | Saltar los espacios en blanco en la entrada, por omisión esta activado); esta operación se desactiva con `noskipws` |
| `uppercase`         | Mostrar en mayúsculas los caracteres hexadecimales A – F y la E en la notación científica; esta operación se desactiva con `nouppercase` |
| `internal`          | Hacer que los caracteres de relleno se añadan después del signo o del indicador de base y antes del valor |
| `left`              | Alineación por la izquierda y relleno por la derecha         |
| `right`             | Alineacion por la derecha y relleno por la izquierda (establecido por omisión) |
| `dec`               | Representación en decimal (base por omisión)                 |
| `oct`               | Representación en octal                                      |
| `hex`               | Representación en hexadecimal                                |
| `fixed`             | Activar el formato de coma flotante (d.ddddddEdd)            |
| `scientific`        | Activar el formato de notación científica                    |
| `endl`              | Escribir `'\n'` y vaciar el búfer del flujo                  |
| `ends`              | Escribir `'\0'`                                              |
| `flush`             | Vaciar el búfer de flujo de salida                           |
| `ws`                | Saltar los espacios en blanco que preceden a un dato en la entrada. Mientas que `skipws` actúa sobre la entada en general, `ws` se aplica solo sobre el siguiente dato a leer, y se utiliza cuando `skipws` no está activado |
| `setiosflags(long)` | Activas opciones por ejemplo fixed, left, etc. (equivalentes a `setf`) Se desactivan con `resetiosflags` (equivalente a `unseft`) |
| `setbase(int)`      | Establecer la base en la que se escribirán los enteros       |
| `setfill(char)`     | Establecer como carácter de relleno especificado             |
| `setprecision(int)` | Establece el numero de decimales para un valor real. La precisión por defecto es 6 |
| `setw(int)`         | Establecer la anchura del campo donde se ca a escribir un dato |

### Ejemplo

~~~c++
#include <iostream> 
#include <iomanip>
#include <string>
#include <conio.h>
using namespace std;

int main() {
    double coef[] = { 5198.0, 3.21, 46.32, 506.5, 2002.38 };
    string prov[] = { "Madrid", "Sevilla", "Valencia", "Cantabria" };
    cout << setiosflags(ios::fixed);
    for (int i = 0; i < (sizeof(coef) / sizeof(double) - 1); i++) {
        cout << setiosflags(ios::left)
            << setw(15)
            << setfill('.')
            << prov[i]
            << resetiosflags(ios::left)
            << setw(10)
            << setprecision(2)
            << coef[i] << endl;
    }
    _getch();
} 
~~~


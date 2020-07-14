# Código ejemplo

Programa que las variables al utilizar las en una función pueden ser modificadas por medio de los apuntadores.

~~~c++
#include <iostream>
#include <conio.h>
using namespace std;

void intercambio(int *x, int *y) {
    cout << "1. a: " << x << " b: " << y << endl;
    int z = *x;
    cout << "z: " << z << endl;
    *x = *y;
    *y = z;
}

int main() {
    int a = 20;
    int b = 30;
    cout << "&. a: " << &a << " b: " << &b << endl;
    intercambio(&a, &b);
    cout << "f. a: " << a << " b: " << b << endl;
    _getch();
    return 0;
}
~~~



Programa que utiliza el final de fichero (Ctrl + z) para finalizar las operaciones con los bits de error.

~~~c++
#include <iostream>
#include <conio.h>
#include <iomanip>
using namespace std;

int main() {
    int dato, suma = 0, n = 10, i = 0;
    bool eof = false;
    bool juanito;
    cout << "Introducir n datos maximo, Finalizar con eof\n\n";
    juanito = cin.eof();
    cout << boolalpha << "\ncin.eof " << juanito << "\n\n";
    do {
        cout << "datos: ";
        cin >> dato;
        juanito = cin.eof();
        cout << boolalpha << "\ncin.eof " << juanito << "\n\n";
        juanito = cin.fail();
        cout << boolalpha << "\ncin.fail " << juanito << "\n\n";
        juanito = cin.good();
        cout << boolalpha << "\ncin.good " << juanito << "\n\n";
        juanito = cin.bad();
        cout << boolalpha << "\ncin.bad " << juanito << "\n\n";
        eof = cin.eof();
        if (!eof && cin.fail()) {
            cerr << '\a' << "\ndato incorrecto\n";
            cin.clear();
            cin.ignore(numeric_limits<int>::max(), '\n');
        }
        else if (cin.good()) {
            suma += dato;
            i++;
        }
    } while (!eof && !cin.bad() && i < n);
    cout << "Suma: " << suma << endl;
    _getch();
    return 0;
}
~~~



Calcular si un año es bisiesto o no y saber cuántos días tiene el mes.

~~~c++
switch (mm){
    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
    	dd = 31;
    break;
    case 4: case 6: case 9: case 11:
    	dd = 30;
    break;
    case 2:
        if ((aa % 4 == 0) && (aa % 100 != 0) || (aa % 400 == 0)){
        	dd = 29;
        }
        else {
        	dd = 28;
        }
    break;
    default:
    	cout << "\nEl mes no es valido\n";
    break;
}
~~~



Utilizar las estructuras de datos.

~~~c++
#include <iostream>
#include <string>
#include <conio.h>
using namespace std;

struct tfecha {
	int dia, mes, anyo;
};

struct tficha {
    string nombre;
    string direccion;
    long telefono;
    tfecha fecha_nacimiento;
};

int main() {
    tficha persona, otra_persona;
    cout << "Nombre: "; getline(cin, persona.nombre);
    cout << "Direccion: "; getline(cin, persona.direccion);
    cout << "Telefono: "; cin >> persona.telefono;
    cout << "Fecha de nacimiento:\n";
    cout << "   Dia: "; cin >> persona.fecha_nacimiento.dia;
    cout << "   Mes: "; cin >> persona.fecha_nacimiento.mes;
    cout << "   Anyo: "; cin >> persona.fecha_nacimiento.anyo;
    otra_persona = persona;
    cout << "\n\n";
    cout << "Nombre: " << otra_persona.nombre << endl;
    cout << "Direccion: " << otra_persona.direccion << endl;
    cout << "Telefono: " << otra_persona.telefono << endl;
    cout << "Fecha de nacimiento:\n";
    cout << "   Dia: " << otra_persona.fecha_nacimiento.dia << endl;
    cout << "   Mes: " << otra_persona.fecha_nacimiento.mes << endl;
    cout << "   Anyo: " << otra_persona.fecha_nacimiento.anyo << endl;
    _getch();
    return 0;
}
~~~



Puntero de punteros.

~~~c++
#include <iostream>
#include <conio.h>
#include <iomanip>
using namespace std;

int main() {
    int i, j;
    int a[5][5];
    int *p[5];
    int **pp;
    for (i = 0; i < 5; i++) {
    	p[i] = a[i];
    }
    pp = p;
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            cout << "[" << i << "][" << j << "] = ";
            cin >> pp[i][j];
        }
    }
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
        	cout << setw(3) << *(*(pp + i) + j);
        }
        cout << endl;
    }
    _getch();
    return 0;
}
~~~



Obtener la fecha del sistema.

~~~c++
void Fecha::agregarFecha() {
    struct tm tiempo;
    time_t fecha_sistema;
    time(&fecha_sistema);
    localtime_s(&tiempo, &fecha_sistema);
    anio = tiempo.tm_year + 1900;
    mes = tiempo.tm_mon + 1;
    dia = tiempo.tm_mday;
}
~~~



Crear un identificador para definir una variable que crea un puntero a una clase. 

~~~c++
typedef void (Cuenta::*puntero)(double);
puntero p1 = Cuenta::reintegro;
~~~


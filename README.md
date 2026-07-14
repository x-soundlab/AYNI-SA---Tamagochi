# AYNI S.A. — Tamagochi en Python

Proyecto realizado como practica de Python para simular una mascota virtual interactiva mediante terminal.

El programa permite cuidar a un **Miawmiaw**, una mascota virtual cuyos niveles de energía, felicidad y hambre cambian según las acciones del usuario y algunos eventos aleatorios.

## Características

* Solicita al usuario el nombre de la mascota.
* Inicializa energía, felicidad y hambre con valores aleatorios entre 3 y 5.
* Muestra el estado actual de la mascota.
* Permite realizar tres acciones:

  * `comer`
  * `dormir`
  * `jugar`
* Incluye un evento aleatorio de aburrimiento con un 20 % de probabilidad.
* Finaliza cuando la mascota:

  * alcanza un nivel de hambre igual o superior a 10;
  * se queda sin energía;
  * llega al límite de 10 acciones.

## Estados de la mascota

| Estado    | Descripción                                                               |
| --------- | ------------------------------------------------------------------------- |
| Energía   | Disminuye al comer o jugar y aumenta al dormir.                           |
| Felicidad | Aumenta al comer, dormir o jugar y disminuye cuando la mascota se aburre. |
| Hambre    | Disminuye al comer y aumenta al jugar.                                    |
| Acciones  | Cuenta las acciones realizadas durante la partida.                        |

## Acciones disponibles

### Comer

Reduce el hambre en 3 puntos, aumenta la felicidad en 1 punto y reduce la energía en 1 punto.

```text
comer
```

### Dormir

Aumenta la energía en 4 puntos y la felicidad en 1 punto. La acción incluye una pausa de tres segundos para representar el descanso.

```text
dormir
```

### Jugar

Aumenta la felicidad en 2 puntos, reduce la energía en 2 puntos y aumenta el hambre en 1 punto.

```text
jugar
```

## Evento aleatorio

En cada vuelta del bucle existe un 20 % de probabilidad de que la mascota se aburra. Cuando ocurre, su felicidad disminuye en 2 puntos.

## Requisitos

* Python 3
* No requiere instalar librerías externas.

El programa utiliza únicamente módulos incluidos en la biblioteca estándar de Python:

* `random`
* `time`

## Ejecución

Abre una terminal dentro de la carpeta del proyecto y ejecuta:

```bash
python tamagochy.py
```

En Windows también puedes utilizar:

```powershell
py tamagochy.py
```

Después, introduce el nombre de la mascota y escribe una de las acciones disponibles cuando el programa lo solicite:

```text
comer
dormir
jugar
```

## Estructura del proyecto

```text
AYNI-SA---Tamagochi/
├── tamagochy.py
├── Ayni's Consultant S.A - Prueba Técnica Tamagochi en Python.md
└── README.md
```

## Conceptos de Python utilizados

* Variables globales
* Funciones
* Diccionarios
* Condicionales
* Bucles `while`
* Entrada de datos con `input()`
* Números y eventos aleatorios
* Pausas mediante `time.sleep()`

## Autoría

Proyecto desarrollado para **AYNI S.A.**

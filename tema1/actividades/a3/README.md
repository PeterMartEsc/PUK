# Actividad 1.3: Vulnerabilidades, lenguajes de bajo nivel.

__Autor:__ Pedro Martín Escuela <br>
__Curso:__ Especialización Ciberseguridad

## Índice

## Ejercicios

Para los siguientes ejemplos, encuentra la vulnerabilidad y explica
cómo corregirla o mitigarla.

### 1. Desbordamiento de Búfer (Buffer Overflow)

Ocurre cuando se copian más datos en un búfer de los que este puede almacenar, sobrescribiendo la memoria contigua en la pila (stack).

```C
// Código vulnerable

#include <stdio.h>
#include <string.h>

void funcion_vulnerable(char *input) {
    char buffer[16];
    strcpy(buffer, input);
    printf("Texto copiado: %s\n", buffer);
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        funcion_vulnerable(argv[1]);
    }
    return 0;
}
```

__Vulnerabilidad Explicada:__

En este ejemplo de código, se está permitiendo explotar la vulnerabilidad de __Buffer Overflow__ mediante el uso de `strcpy(buffer, input)`. Aunque antes se haya especificado que `buffer` tiene un tamaño de __16 caracteres__, la función strcpy no comprueba el tamaño máximo de la variable, asi que si el input es mayor, ocurre un _overflow_ sobrescribiendo asi la memoria contigua en la pila.

Además, un atacante puede diseñar el _input_ de tal manera que reemplace la __dirección de retorno__ (lo que va contiguo en la pila) con la dirección de memoria de un __código malicioso__ (inyectado por él mismo), logrando ejecutar __comandos arbitrarios__ en el sistema.

__Solución:__

Para solucionarlo, se debe cambiar por funciones que sí controlen los límites, como snprintf:

```C
...
snprintf(buffer, sizeof(buffer), "%s", input);
...
```

### 2. Uso Tras Liberación (Use-After-Free - UAF)

Ocurre cuando un programa sigue utilizando un puntero después de que la memoria apuntada por este ha sido liberada con free().

```C
// Código vulnerable

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nombre[20];
    void (*mostrar)(char *);
} Usuario;

void saludar(char *msg) {
    printf("Hola, %s\n", msg);
}

int main() {
    Usuario *usr = (Usuario *)malloc(sizeof(Usuario));
    strcpy(usr->nombre, "Alice");
    usr->mostrar = saludar;

    free(usr);

    printf("El usuario es: %s\n", usr->nombre);
    return 0;
}
```

__Vulnerabilidad Explicada:__

En este ejemplo de código, reserva espacio en memoria para guardar un valor en usr. Luego __marca como libre__ la variable __usr__, pero no la libera automaticamente. Está marcando como liberada, es decir, el valor sigue estando asignado a la variable, solo le estás diciendo al compilador, que puede aprovechar ese espacio en memoria para sobreescribirlo y poner otra información. 

El atacante puede interactuar con el programa (por ejemplo, enviando un comentario, cargando un archivo o creando otro objeto) que reserve exactamente el mismo tamaño de memoria.

__Solución:__

Para evitar un exploit __UAF__, lo mejor es limpiar siempre el puntero, asignándole NULL inmediatamente después de liberarlo. 

```C
...
    free(usr);
    usr=NULL;
...
```

### 3. Doble Liberación (Double Free)

Ocurre cuando se llama a free() dos veces sobre la misma dirección de memoria sin haber sido reasignada.

```C
// Código vulnerable

#include <stdio.h>
#include <stdlib.h>

void liberar_recurso(char *ptr) {
    free(ptr);
}

int main() {

    char *data = (char *)malloc(64);
    liberar_recurso(data);
    // ... lógica intermedia del programa …
    free(data);
    return 0;
}
```

__Vulnerabilidad Explicada:__

Si el programa realiza nuevos malloc más adelante, dos variables de diferentes partes del código podrían recibir exactamente la misma dirección de memoria. Esto permite que una parte del programa modifique sin querer (o de forma maliciosa) los datos confidentes o los punteros de función de otra estructura, derivando a menudo en un ataque de tipo Use-After-Free (UAF) o en la ejecución de código arbitrario.

__Solución:__

Prestar atención y no usar dos veces free sobre una misma variable. Recordemos que en el momento en que usa `free()` en una variable, solo marcamos como disponible el espacio en memoria, no la estamos liberando instantaneamente.

### 4. Cadena de Formato (Format String Vulnerability)

Ocurre cuando se pasa una entrada de usuario sin validar directamente como el primer argumento (format string) de funciones como printf sprintf o fprintf.

```C
// Código vulnerable

#include <stdio.h>

void imprimir_mensaje(char *user_input) {
    printf(user_input);
    printf("\n");
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        imprimir_mensaje(argv[1]);
    }
    return 0;
}
```

__Vulnerabilidad Explicada:__

Al no validar lo introducido por el usuario, se puede usar argumentos que revelen informacón sensible existente en la pila o modifique la memoria. 

Un ejemplo muy claro sería cambiar el valor de una variable como `is_admin = 0` -> `is_admin = 1` para que le de permisos al usuario que está intentando explotar la vulnerabilidad del programa. 

__Solución:__

Siempre se debe dar un formato estático al argumento introducido por el usuario:

```C
...
void imprimir_mensaje(char *user_input) {
    // El primer argumento SIEMPRE es una cadena fija (%s asegura que todo lo demás sea tratado puramente como texto)
    printf("%s", user_input); 
    printf("\n");
}
...
```
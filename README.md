# Prácticas de Evaluación Unidad 1, Python
![image](https://user-images.githubusercontent.com/115977230/204237464-b5ad4850-77ae-456b-9c77-70ad4016c1dc.png)


1. Utilizando la clasificación vista en clase sobre los lenguajes de programación, escoge 5 lenguajes que desees y clasifícalos en una tabla según su nivel de abstracción, su forma de ejecución y los paradigmas de programación que incorpora. No olvides incluir el año de aparición y el autor/autores del mismo como MÍNIMO. Incluye toda esta información en un fichero llamado lenguajes.pdf.

2. Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que introduzca un número binario e imprima por pantalla el número en formato decimal. Para desarrollar el programa, es necesario que desarrolles una función con la siguiente cabecera:
def esBinario(strbinario)

Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado como parámetro contiene una cadena binaria.
Ejemplo de esBinario:

print(esBinario(“1001”))

True

print(esBinario(“Hola”)) 

False

3. Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes cabeceras:
def estaEnRango(valor, minimo, maximo)

Devuelve True o False determinando que valor se encuentra entre el mínimo y el máximo.

def estaEnLista(valor, lista)

Devuelve True o False determinando si el valor está en la lista.

4. Crea una suite de tests mediante UnitTest que comprueben las 3 funciones que has desarrollado en los ejercicios anteriores. Procura que los tests unitarios cubran lo mejor posible la aparición de comportamientos no deseados.

5. Realiza el ejercicio 4 pero utilizando esta vez cualquier otro framework de terceros como por ejemplo pytest.
## Ejercicio 1 

| Lenguaje | Forma de Ejecución | Nivel de Abstracción | Paradigmas de Programación | Año de Aparición | Autor
| --- | --- | :---: | --- | --- | --- |
| JAVA | El entorno de ejecución de Java (JRE) combina el código de Java creado. Para ello, utiliza el kit de desarrollo de Java (JDK) con código adicional incorporado que se denomina bibliotecas | 2 |  Orientado a objetos, imperativo | 1995  |  James Gosling
| JavaScript | El programa se ejecuta desde un formato binario, que se generó a partir del código fuente del programa original. JavaScript es un lenguaje de programación interpretado ligero. El navegador web recibe el código JavaScript en su forma de texto original y ejecuta el script a partir de ahí. | 5 | Puedes escribir JavaScript en el paradigma declarativo o el paradigma imperativo. | 1995 |  Brendan Eich 
| C | Cada programa de C tiene una función principal a la que se debe llamar main. La función main sirve como punto de partida para la ejecución del programa. Normalmente, controla la ejecución del programa dirigiendo las llamadas a otras funciones del programa. | 1 | Paradigma de programación estructurada. | 	1972 | 	Dennis Ritchie
| Python | Puede ejecutar un script Python desde Programas de utilidad > Ejecutar script o desde el editor de scripts Python, que se ha iniciado al abrir un archivo Python (*. py) desde Archivo > Abrir > Script. | 4 | Orientación a objetos, programación imperativa | 1991 | van Rossum
| PHP | Hay dos maneras de ejecutar archivos PHP. La manera preferida de ejecutar archivos PHP es dentro de un servidor web como Apache, Nginx o ISS; esto te permite ejecutar scripts de PHP desde tu navegador. | 3 | PHP es un lenguaje de tipado dinámico, multiparadigma e interpretado | 1994 | Rasmus Lerdorf




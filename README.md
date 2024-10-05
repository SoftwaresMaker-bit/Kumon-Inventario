# Kumon-Inventario
Proyecto para el desarrollo de un software de monitoreo para el inventario del sistema educativo Kumon
Este proyecto consiste en un software de monitoreo de inventario. El objetivo es aligerar la carga al momento de contar inventario y hacer de esta acción una mas fácil, eficiente y rápida. En la cadena educativa Kumon, los ejercicios están divididos en materias(Español, Ingles y matemáticas), niveles( del A hasta el O) y numero de ejercicio(Desde el 1 hasta el 100). A los alumnos se les da libritos de 10 ejercicios de cierto nivel y cierta materia diario. Esta variabilidad en el material integrado hace de contar inventario una tarea tediosa y tardada. El programa busca poder registrar de forma rápida por los asistentes a que niño se le dio que cantidad de series de que nivel y que materia. El programa registrará esta información y restará al total de material en el centro la tarea dada. Al final el programa dará al usuario los nombres de los alumnos, el material que se le dio a cada uno y el material restante en el centro. Con esto restablecer el inventario será una tarea mucho más rápida y eficiente y ademas se llevará registro de las tareas de cada alumno. 

El algoritmo para este proyecto sería el siguiente:

Algoritmo función registro
- entradas: Nombre del Estudiante, numero de materias que cursa, Materias, nivel de cada materia, series de cada materia.

- Proceso: Definir variables iguales a 0 para cada materia y una variable string llamada Reporte del día. Iniciar un While con condición True. Adentro del loop while, Se pide el nombre del estudiante y la cantidad de materias que cursa. Se crea una var string llamada Reporte final. Un for loop con limite en la cantidad de materias cursadas pedira al usuario la materia del estudiante, el nivel de la materia y el numero de serie que se lleva el estudiante. Con condicionales ifs se verifica la materia y se le suma + 1 a la variable de la materia correspondiente. Los inputs dados por el usuario se van almacenando en la variable string Reporte Final y por ultimo en la variable string Reporte del Día. Una vez acabado el loop, se pregunta al usuario si quiere repetir para registrar a otro alumno. Si la respuesta es si, se repite el loop while. Por el contrario, se rompe el loop while con un Break.

- Salida: Nombre los estudiantes con sus respectivas materias, niveles y series. numero de alumnos en cada materia.

Algoritmo Función Imprimir
-Entradas: Matriz, Tipo

proceso: Dependiendo del valor del Tipo es la naturaleza de la matriz. El tipo == 2 es para imprimir reportes. Para esto se forma un for loop con limite en len de el reporte. dentro de este for loop se crea otro for loop con limite en len(1,reporte[i]). Con este loop entramos al expediente del estudiante con su nombre y las listas de cada materia , pero queremos evitar imprimir el nombre muchas veces si este loop es igual a 1 se imprime el nombre. Añadimos dentro otro loop con limite en 3 pues la lista de cada materia solo puede tener 3 valores: Nombre de la materia, El nivel y El librito. En el caso de el Tipo ser 2 ahora es el Reporte del Día donde se contiene todos los reportes. Aqui para imrpimirlo solo se le agrega un loop al inicio del programa para los Reportes. Esto para poder ciclar dicho proceso en todos los reportes. 



Algoritmo función menu
 proceso: se imprime las opciones de funciones

 salida: prints de las opciones

 Algoritmo función main

 entrada: opción del usuario 

 proceso: Se crea un loop while con condición True. se llama la función menu y se le pide al usuario escoger una opción. Utilizando condicionales se verifica la opción del usuario y se llama a la función correspondiente. La opción 2 llama a un break acabando con el while loop y el programa. Si la opción no es valida, se imprime un mensaje y el loop se repite. 

  
    

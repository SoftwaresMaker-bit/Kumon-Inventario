# Kumon-Inventario
Proyecto para el desarrollo de un software de monitoreo para el inventario del sistema educativo Kumon
Este proyecto consiste en un software de monitoreo de inventario. El objetivo es aligerar la carga al momento de contar inventario y hacer de esta acción una mas fácil, eficiente y rápida. En la cadena educativa Kumon, los ejercicios están divididos en materias(Español, Ingles y matemáticas), niveles( del A hasta el O) y numero de ejercicio(Desde el 1 hasta el 100). A los alumnos se les da libritos de 10 ejercicios de cierto nivel y cierta materia diario. Esta variabilidad en el material integrado hace de contar inventario una tarea tediosa y tardada. El programa busca poder registrar de forma rápida por los asistentes a que niño se le dio que cantidad de libritos de que nivel y que materia. El programa registrara esta información y restara al total de material en el centro la tarea dada. Al final el programa dará al usuario los nombres de los alumnos, el material que se le dio a cada uno y el material restante en el centro. Con esto restablecer el inventario será una tarea mucho más rápida y eficiente. 

El algoritmo para este proyecto sería el siguiente:

-Entrada: Nombre, materia, nivel, numero de libros que hizo, Numero de libros que se llevo

-Proceso: 
    . Hacer ua función que haga lo siguiente
      *Pedir el nombre del alumno
      *Pedir la materia que hizo
      *Pedir el nivel en el que esta 
      *Pedir el numero de libros que hizo
      *Pedir el numero de libros que se llevo
      *Vincular y juntar estas variables en una sola, por ejemplo en un Array
    .Con un While o un For loop repetir esta acción hasta que el usuario lo detenga.
    .Usar un for loop o un while para imprimir todos los resultados.

-Salida: 
        .Nombre del alumno, Nivel en el que esta, material que se llevo y que hizo.
        . Nivel donde se dio material y el total de material restante en el centro.
    

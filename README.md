# Kumon-Inventario
Proyecto para el desarrollo de un software de monitoreo de inventario para la franquicia educativa Kumon
Este proyecto consiste en un software de monitoreo de inventario. El objetivo es aligerar la carga al momento de contar inventario y hacer de esta acción una mas fácil, eficiente y rápida. En la cadena educativa Kumon, los ejercicios están divididos en materias(Español, Ingles y matemáticas), niveles( del A hasta el O) y libritos de ejercicios(Desde el 1 hasta el 200). A los alumnos se les da libritos de 10 ejercicios de cierto nivel y cierta materia diario. Esta variabilidad en el material hace de contar inventario una tarea tediosa y tardada. El programa tiene como objetivo poder registrar de forma rápida por los asistentes a que niño se le dio que cantidad de libritos de que nivel y que materia. El programa registrará esta información y hará una sumatoria del material dado. Al final el programa dará al usuario los nombres de los alumnos, el material que se le dio a cada uno y el material dado por materia. Con esto restablecer el inventario será una tarea mucho más rápida y eficiente. Pues se contaran los libritos repetdios y se llevara bitacora de el material dado.

Algoritmo main

1. Se definen variables principales como las matrizes para cada materia(Esp,Ingl,Mate) y la matriz para el reporte del día 
2.  Se inicia un while true con ifs anidados para llamar a cierta función dependiendo de lo que quiera hacer el usuario.
3. Se le pregunta al usuario que función quiere ejectuar.
4. La opción 1 ejecuta la función Registro, donde se registra mediante inputs el expediente del alumno con el material dado con su respecto nivel y materia.
5. En la opción 1, la función Registro regresa las matrices de los estudiantes y las anida al Reporte del día. Ademas regresa el material dado de cada materia y las anida en las matrizes de su materia correspondiente.
6. La opción 2 llama a la función Imprimir pasando como argumentos la matriz Reporte del día y el modo de impresión. Como salida, imprime la matriz en forma de renglones y columnas y escribe en un archivo .txt el reporte final.
7. La opción 3 llama a la función Libritos donde se imprimen de forma lineal las matrices de cada materia.
8. La opción 4 anida las matrices de las 3 materias dentro de 1 sola matriz. Con un for loop con el nombre y la matriz como variables auxiliares y rango en la matriz de materias, llama una por una para pasar por la función Inventario. Dicha función cuenta la cantidad de libritos y libritos repetidos de cada materia e imprime la cantidad.
9. La opción 5 ejecuta todas las funciones excepto Registro con una matriz hardcodeada como argumento. Esta función tiene como objetivo realizar pruebas de funcionamiento. 
10. La opción 6 termina el While loop con un Break
11. En caso de recibir un input diferente, imprime un aviso y se vuelve a ejecturar el loop.

Instrucciones para uso del programa. 

la mayoría de funciones necesitan de variables con datos que salen de la función Registro. No habrá un error en caso de ejecutar alguna función antes de utilizar Registro, sin embargo aparecerá salidas vacías. Por ende es importante empezar por la función Registro. 

La función registro requiere que introduzcas en nombre del alumno, la cantidad de materias que cursa, el nivel en el que va en cada materia y el numero de librito que se lleva. Una vez registrado los alumnos necesarios escribir 'No' al final de la función. En caso de querer registrar nuevos alumnos se puede volver a ejecutar la función sin problema. Los registros anteriror no se borrarán. No es necesario escribir el nivel o la materia con mayúsculas pues el programa convierte la información en mayúsculas por defecto.

La función Imprimir_Reporte generará un archivo tipo .txt donde se escribira el reporte con los expedientes de cada alumno. Como los expedientes se guardan en una matriz y esta función escribe el Reporte completo, No se perderan registros anteriores pues se vuelven a escribir en el archivo.  

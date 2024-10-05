#Limites de función pruebas: Por ahora, el programa no cuenta las series dadas y no le resta al inventario para dar un reporte de este.
#Esto pues se necesitan Listas para dicha tarea.



#Función para imprimir matricez, el argumento tipo señala si vamos a imprimir un reporte o el reporte final
def Imprimir(matriz,tipo): #El reporte final contiene todos los reportes del día. 
    
    if tipo == 2:# For loop para imprimir Reportes
        print("Reporte ")
        for i in range(len(matriz)):# Loop para cada Expediente de estudiante
            print("\n")
            for j in range(1,len(matriz[i])):#Loop para cada materia, limite en cantidad de materias
                if j == 1:
                    print(matriz[i][0], end = " ")#Print solo del nombre
                print()
                for k in range(3):# Loop para el print de la info del curso, constante siempre lim en 3
                    print(matriz[i][j][k], end = " ")           
        print("\n")#Espacio final
        
    elif tipo == 1: #For loop para imprimir Reportes Finales, se agrega un loop mas
         print("Reporte_Final")
         for a in range(len(matriz)): #Loop para cada reporte
             print("Reporte %d \n" % (a+1))
             for i in range(len(matriz[a])):# Loop para cada Expediente en cada reporte
                 print("\n")
                 for j in range(1,len(matriz[a][i])):#Loop para cada materia, limite en cantidad de materias
                     if j == 1:
                         print(matriz[a][i][0], end = " ")#Print solo del nombre
                     print()
                    
                     for k in range(3):# Loop para el print de la info del curso, constante siempre lim en 3
                         print(matriz[a][i][j][k], end = " ")
                        
             print("\n")#Espacio final
        


def libritos(esp,ingl,mate,option):#Función para imprimir los libritos por materia
    if option == 1:
        print("Esp " + str(esp))
        print("Ingl " + str(ingl))
        print("mate " + str(mate))
                   



#Función que recibe del usuario la información de la tarea dada a cada estudiante(materia,niveles,libros) y las registra.
def Registro():
    
    Reporte =[] #Reporte final a imprimir con los estudiantes y sus cursos. 
    
    ingl = []# Variables para separar los inputs en materias, se mandaran al final del programa 
    mate = []# para ser contados en otra función. 
    esp = []  
    
    while True: #While que cicla el registro hasta que el usuario decida finalizar el programa. 
        Materias = ["Esp ","Ingl ","Mate "]
        
        nombre = input("Nombre del estudiante " )
        numero_materias = int(input("¿Cuantas materias curza " + str(nombre) + " ?")) # i del for loop
        
        Estudiante =[] # Matriz donde se añaden listas de cada materia. Expediente de cada estudiante 
        
        Estudiante.append(nombre) #Se agrega nombre del estudiante 
        
        for i in range (numero_materias): # loop para los inputs de cada materia del estudiante
            
            Curso = []# Se crea una lista para la info de la materia, esta lista estará dentro de la matriz del estudiante. 
            materia = input( " ¿materia? " +   str(i+1) + str(Materias))
            
            Curso.append(materia)#se agrega el nombre de la materia en la lista de Materia. 
            
            nivel = input("¿En que nivel va ? ") #Input de nivel
            Curso.append(nivel)
            
            libro = int(input ("¿Qué libro se lleva ? ")) #Input del numero del libro
            Curso.append(libro)
            
            Estudiante.append(Curso)# Se agrega la lista de dicha materia al expediente del alumno
            print(Curso)
            
            # Dependiendo de la materia, se registra los Niveles con su librito.
            #Variables se regresan a la función main y se reinician con cada nuevo reporte
            if materia == "Ingl" or materia == "ingl":
                Materias.remove("Ingl ") #Remueve la materia de a lista de materias 
                ingl.append(Curso[1:3])
                print(ingl)
                
            elif materia == "Esp" or materia == "esp":
                Materias.remove("Esp ")#Remueve la materia de a lista de materias 
                esp.append(Curso[1:3])
                print(esp)
                
            elif materia == "mate" or "Mate":
                Materias.remove("Mate ")#Remueve la materia de a lista de materias 
                mate.append(Curso[1:3])
                print(mate)
            
            
        
      
        Reporte.append(Estudiante)# Se añade el expediente del estudiante al Reporte.
        seguir = input("¿Nuevo Reporte?") # Sigue el while loop para mas estudiantes o finaliza el progrma 
        
        if seguir == "si" or seguir == "Si":
            continue
        
        else:
            print()
            Imprimir(Reporte,2)
            break
        
    return Reporte,esp,ingl,mate
        



# Función que imprime las opciones de funciones a elegir
def menu(): 
    print("1. Registro \n2.Imprimir Reporte Del Día \n3.Imprimir libritos por materia \n4.Salir")


#Función main donde se recibe el input del usuario de que función ejecutar o si acabar el programa    
def main():
    #Variables para contar libritos por materia 
    Esp_total = []
    Mate_total = []
    Ingl_total= []
    
    Reporte_Día = []# Matriz con todos los reportes(Estudiantes y sus cursos)
    while True:
        
        Esp = []
        Ingl = []
        Mate = []
        
        menu()
        option = int(input("¿Qué vamos a hacer hoy? "))
        if option == 1:
            Reporte,Esp,Ingl,Mate = Registro()
            Reporte_Día.append(Reporte)
            
            Esp_total.append(Esp)
            Mate_total.append(Mate)
            Ingl_total.append(Ingl)
            
        elif option == 2:#Imprimir el Reporte del Día
            Imprimir(Reporte_Día,1)
        
        elif option == 3: #Imprimir los libritos dados por cada materia
            libritos(Esp,Ingl,Mate,1)
            
        elif option == 4:
            break
        else:
            print("Esa opción no es valida")



main()

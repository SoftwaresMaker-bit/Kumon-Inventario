#Limites de función pruebas: Por ahora, el programa no cuenta las series dadas y no le resta al inventario para dar un reporte de este.
#Esto pues se necesitan Listas para dicha tarea.




#Función para imprimir matricez, el argumento tipo señala si vamos a imprimir un reporte o el reporte final
def Imprimir_Reporte(matriz,tipo): #El reporte final contiene todos los reportes del día. 
    if tipo == 2:# For loop para imprimir Reportes
        print("Reporte ")
        for i in range(len(matriz)):# Loop para cada Expediente de estudiante
            for j in range(1,len(matriz[i])):#Loop para cada materia, limite en cantidad de materias
                if j == 1:
                    print(matriz[i][0], end = " ")#Print solo del nombre
                    print("\n")
                for k in range(3):# Loop para el print de la info del curso, constante siempre lim en 3
                    print(matriz[i][j][k], end = " ")
            print("\n")    
        
                
    elif tipo == 1: #For loop para imprimir el file.txt. 
        archivo = Escribir_Reporte(matriz)
        archivo.seek(0)
        Contenido = archivo.read()
        print(Contenido)
        archivo.close()
        
        
       
             
def Escribir_Reporte(matriz): #Función para escribir en un archivo .txt el reporte del día.
    archivo = open("Bitacora","w+") # Abrir el archivo
    archivo.write("\n")
    archivo.write("Reporte_Final")
    for a in range(len(matriz)): #Loop para cada reporte
        archivo.write("\n\n")
        archivo.write("Reporte %d \n" % (a+1))
        for i in range(len(matriz[a])):# Loop para cada Expediente en cada reporte
            archivo.write("\n")
            for j in range(1,len(matriz[a][i])):#Loop para cada materia, limite en cantidad de materias
                if j == 1:
                    archivo.write(str(matriz[a][i][0]))#Print solo del nombre
                archivo.write("\n")
                for k in range(3):# Loop para el print de la info del curso, constante siempre lim en 3
                    archivo.write(str(matriz[a][i][j][k]))
                    archivo.write(" ")
            archivo.write("\n")
                        
    
    return archivo
        


def libritos(esp,ingl,mate,):#Función para imprimir los libritos por materia
    print("Esp " + str(esp))
    print("Ingl " + str(ingl))
    print("Mate " + str(mate))
           
        
                     

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
            upper_materia = materia.upper()
            
            Curso.append(upper_materia)#se agrega el nombre de la materia en la lista de Materia. 
            
            nivel = input("¿En que nivel va ? ") #Input de nivel
            Upper_nivel = nivel.upper()
            Curso.append(Upper_nivel)
            
            libro = int(input ("¿Qué libro se lleva ? ")) #Input del numero del libro
            Curso.append(libro)
            
            Estudiante.append(Curso)# Se agrega la lista de dicha materia al expediente del alumno
            
            
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
            Imprimir_Reporte(Reporte,2)
            break
        
    return Reporte,esp,ingl,mate
        

def simplificar_lista(lista,prueba): #Función para simplificar la matriz
    
    if prueba == 1:
        print("Lista Inicial " +str(lista))
        
    Nueva_lista = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            Nueva_lista.append(lista[i][j])
        
    if prueba == 1:       
        print("Lista aplanada" + str(Nueva_lista))
        print("\n")
        
    return Nueva_lista


def Inventario(matriz, nombre_matriz):
    if matriz == [[]] or matriz ==[]:  # Si la matriz está vacía, salta el conteo
        print('La materia' + str(nombre_matriz)+ ' está vacía.')
        return
    matriz = simplificar_lista(matriz,2)  # Aplanamos la matriz
    listas_contadas = []
    print('Conteo en la materia ' + str(nombre_matriz))
    for sublista in matriz:
        if sublista not in listas_contadas:
            cantidad = 0
            for s in matriz:
                if s == sublista:
                    cantidad += 1
            listas_contadas.append(sublista)
            print("El librito "+str(sublista)+" aparece "+str(cantidad)+" veces ")
    print()  # Separador para mejor legibilidad
    





# Función que imprime las opciones de funciones a elegir
def menu(): 
    print("1. Registro \n2.Imprimir Reporte Del Día \n3.Imprimir libritos por materia \n4.Conteo de libritos \n5.Pruebas \n6.Salir")


#Función main donde se recibe el input del usuario de que función ejecutar o si acabar el programa    
def main():

    Reporte_Día = []# Matriz con todos los reportes(Estudiantes y sus cursos)
    Esp_total = []
    Ingl_total = []
    Mate_total = []
    while True:
        
        Esp = []
        Ingl= []
        Mate = []
        
        menu()
        option = int(input("¿Qué vamos a hacer hoy? "))
        if option == 1:
            Reporte,Esp,Ingl,Mate = Registro()
            Reporte_Día.append(Reporte)# Se anida el Reporte al Reporte final del día
            
            #Evitar anidar listas vacías
            if Esp ==[]:
                pass
            else:  
                Esp_total.append(Esp)
                
            if Ingl ==[]:
                pass
            else:  
                Ingl_total.append(Ingl)
                
            if Mate ==[]:
                pass
            else:  
                 Mate_total.append(Mate)
            
            Reporte_Final_Pruebas =Reporte_Día
            
        elif option == 2:#Imprimir el Reporte del Día
            Imprimir_Reporte(Reporte_Día,1)
        
        elif option == 3: #Imprimir los libritos dados por cada materia
            libritos(Esp_total,Ingl_total,Mate_total)
            
        elif option == 4:#Contar libritos repetidos. 
            matrices = [("Esp",Esp_total), ("Ingl",Ingl_total), ("Mate",Mate_total)]
            for nombre,matriz in matrices:
                Inventario(matriz, nombre)
                
        elif option == 5:#Función pruebas con matriz hardcodeada, llama a todas la funciones menos registras pasando esta matriz
            Reporte_pruebas = [[['Guillermo Rodriguez', ['ESP', 'D', 121], ['INGL', 'F', 81], ['MATE', 'E', 61]], ['Julian García', ['ESP', 'G', 71]]], [['Valentina Ruiz', ['ESP', 'G', 71], ['MATE', 'E', 61]]]]
            Esp_pruebas = [[['D', 121], ['G', 71]], [['G', 71]]]
            Ingl_pruebas =  [[['F', 81]]]
            Mate_pruebas= [[['E', 61]], [['E', 61]]]
            
            print("Función Imprimir_Reporte \n",end = "")
            Imprimir_Reporte(Reporte_pruebas,1) 
            
            print("Función libritos \n",end = "")
            libritos(Esp_pruebas,Ingl_pruebas,Mate_pruebas)
            
            
            print("Función simplificar_lista usada en la función Inventario \n")
            matrices_a_aplanar =[[Esp_pruebas],[Ingl_pruebas],[Mate_pruebas]]
            for i in range(len(matrices_a_aplanar)):
                simplificar_lista(matrices_a_aplanar[i],1)
                
            print("Función Inventario \n",end = "")
            matrices_prueba=[("Esp",Esp_pruebas), ("Ingl",Ingl_pruebas), ("Mate",Mate_pruebas)]
            
            matrices_prueba = [("Esp",Esp_pruebas), ("Ingl",Ingl_pruebas), ("Mate",Mate_pruebas)]
            for nombre,matriz in matrices_prueba:
                Inventario(matriz,nombre)
            
            
            
          
            
        elif option == 6:
            print("Finalizando Progama...")
            break
        else:
            print("Esa opción no es valida")

main()






    




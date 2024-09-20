#Limites de función pruebas: Por ahora, el programa no cuenta las series dadas y no le resta al inventario para dar un reporte de este.
#Esto pues se necesitan Listas para dicha tarea.

'''
caso Prueba. Opción 1, Estudiante Sebastian Mansilla Cots, Materias 2 ( Matematicas y Español), nivel de mate F, serie llevada 121, nivel de esp H,
serie llevada 31, no.

Salida:

Reporte del día 


Sebastian Mansilla 
mate nivel F serie 121
esp nivel H serie 31

cantidad de estudiantes en ingles 0
cantidad de estudiantes en español 1
cantidad de estudiantes en mate 1

'''



#Función que recibe la información de la tarea dada a cada estudiante(materia,niveles,series) y las registra.
def pruebas():
    engl = 0
    mate = 0
    esp = 0
    Reporte_del_Día = ""
    
    while True: #While que cicla el registro hasta que el usuario decida finalizar el programa. 
        Reporte_final = ""
        nombre = input("Nombre del estudiante " )
        numero_materias = int(input("¿Cuantas materias curza " + str(nombre) + " ?")) # i del for loop
        
        for i in range (1, numero_materias + 1): # loop para los inputs de cada materia del estudiante
            
            materia = input( " ¿materia? " +   str(i) + " ¿ engl, esp o mate ?")
            
            # Dependiendo de la materia, se registra la cantidad de estuidantes en cada una. 
            if materia == "engl":
                engl += 1
                
            elif materia == "esp":
                esp += 1
                
            elif materia == "mate":
                mate +=1
            
            
            nivel = input("¿En que nivel va ? ")
            
            serie = input ("¿Qué serie se lleva ? ")
            
            if i == 1:
                reporte = nombre + "\n" + materia + " " + "nivel " + nivel + " serie " + serie
            else:
                reporte = materia + " " + "nivel " + nivel + " serie " + serie
            
            Reporte_final = Reporte_final + "\n" + reporte
        Reporte_del_Día = Reporte_del_Día + "\n" + Reporte_final
            

        
        seguir = input("¿Nuevo Reporte?") # Sigue el while loop para mas estudiantes o finaliza el progrma 
        
        if seguir == "si" or seguir == "Si":
            continue
        
        else:
            break
        
    print("Reporte del día " + "\n" + Reporte_del_Día + "\n")
    print("cantidad de estudiantes en ingles " + str(engl))
    print("cantidad de estudiantes en español " + str(esp))
    print("cantidad de estudiantes en mate " + str(mate) + "\n")
    
    print("Reporte finalizado")


# Función que imprime las opciones de funciones a elegir
def menu(): 
    print("1. pruebas \n2.Salir ")


#Función main donde se recibe el input del usuario de que función ejecutar o si acabar el programa    
def main():
    while True:
        menu()
        decision = int(input("¿Qué vamos a hacer hoy? "))
        if decision == 1:
            pruebas()
        elif decision == 2:
            print("Programa Finalizado")
            break
        else:
            print("Esa opción no es valida")
main()
            
    

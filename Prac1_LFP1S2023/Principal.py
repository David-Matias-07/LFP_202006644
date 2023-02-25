

from Pelicula import Pelicula

# ------------------------ Funcion para crear el menu --------------------------------------


listaPeliculas = []

def menu():
        while True:
            res = input('''
    ********************************  
    *         Menú Principal       *
    *                              *      
    * 1. Cargar Archivo de Entrada *
    * 2. Gestionar Peliculas       *
    * 3. Filtrado                  *
    * 4. Grafica                   *
    * 5. Salir                     *
    ********************************   
    Seleccione una opcion: ''')

            if res == '1':
                print("Por favor ingrese la ruta del archivo")

# ------------------------------- Lectura y Carga del Archivo de Entrada -----------------------------------------
                try:
                    ruta = input()
                    filename = ruta
                    file = filename       
                    f = open(file, 'r', encoding='utf-8')
                    for linea in f:
                    
                    #separador = linea.split(";")
                    #separador_comas = separador[1].split(",")
                    #quitando_espacios = separador_comas.strip()

#-- Quitando el punto y coma, la coma y creando un nuevo objeto de la clase Pelicula para guardar la informacion --  
                        separador = linea.split(";")
                        separador_comas = separador[1].upper().strip().split(",")
                        pelicula = Pelicula(separador[0], separador_comas, separador[2], separador[3].upper())
                        listaPeliculas.append(pelicula)  
                    f.close()
                    print("Archivo cargado correctamente")
                except:
                     print("Por favor seleccione una ruta valida")

            elif res == '2':
# --------------------------------------- Gestionar Peliculas  --------------------------------------------------

                print("1. Mostrar peliculas")
                print("2. Mostrar Actores")
                print("Por favor ingrese el numero de opcion a mostrar")
                op_mos = input()
                if op_mos == "1":

#-------- Opcion 1 imprime toda la informacion de las peliculas cargadas en el sistema usando dos ciclos for ------ 
                    for x in listaPeliculas:
                        print("Nombre de la pelicula: "+ x.nombre +":")
                        for i in x.actores:
                            print("Actor: "+i)
                        print("Año: " + x.año + "; Genero: " + x.genero + "\n" )        

                elif op_mos == "2":  
#Opcion 2 imprime el nombre de las peliculas cargadas en el sistema usando un contador para enumerlas y un for para imprimir                     
                    print("")
                    contador = 0 
                    for x in listaPeliculas:  
                        contador += 1
                        print(str(contador)+": "+x.nombre)

#Despues hago uso de una varible para hacer referencia al indice o posicion de la lista peliculas 
#Luego recorre la lista peliculas en la posicon indicada por el indice con la variable actor 
#Por ultimo hago referencia que actor va recorrer los actores de la posicion indicada de la lista peliculas y se imprimen los actores de esta
                    print("\n Por favor ingrese el número de pelicula para mostrar los actores de esta")    
                    opc_ac = int(input())
                    indice = opc_ac - 1
                    mostrar_actores = listaPeliculas[indice]
                    for actor in mostrar_actores.actores:
                         print("Actor: "+ actor)
                elif op_mos != "2":
                   # if str(op_mos) != "1" and "2":
                        print("Por favor seleccione una opcion correcta")    
                
            elif res == '3':
# --------------------------------------------- Filtrado  ----------------------------------------------------------
                print("")
                print("1. Filtrado por actor ")
                print("2. Filtrado por año")
                print("3. Filtrado por género")
                print("Por favor ingrese la opcion a filtrar")
                op_fil = input()
                if op_fil == "1":
#Se pide al usuario que ingrese un nombre de actor cualquiera para que se pueda validar en el sistema si hay algun        
#actor con ese nombre para poder imprimir el nombre de la pelicula mas el genero     
                    print("")
                    print("Por favor ingrese el nombre del actor para conocer las peliculas en las que participa")
                    opc_fil_act = input().upper()
                    #opc_ac = int(input())
                    
                    for npa in listaPeliculas:
                        if opc_fil_act in npa.actores:
                             print("Participa en: "+ npa.nombre)
            
               
               
               
               
                elif op_fil == "2":
                    #for x in listaPeliculas:
                     #   print("Años disponibles: "+ x.año)
#Se pide al usuario que ingrese un año cualquiera para que se pueda validar en el sistema si hay alguna        
#pelicula con ese año de estreno para poder imprimir el nombre de la pelicula mas el genero              
                    print("")
                    print("Por favor ingrese el año para conocer las peliculas que tiene el sistema en dicho año")
                    opc_fil_año = input()
                    
                    for peli in listaPeliculas:
                            if opc_fil_año in peli.año:
                                  print("Pelicula: "+ peli.nombre + "  Genero: " + peli.genero)   
                                  
                            #else: 
                               #  print("No hay peliculas en el año indicado")

    
                elif op_fil == "3":
#Se pide al usuario que ingrese un nombre de genero cualquiera para que se pueda validar en el sistema si hay alguna        
#pelicula con ese genero para poder imprimir el nombre de la pelicula  
                    print("")
                    print("Por favor ingrese el genero para conocer las peliculas que tiene el sistema con dicho genero")
                    opc_fil_gen = input().upper()
                    
                    for peli in listaPeliculas:
                              if opc_fil_gen in peli.genero:
                                  print("Pelicula: "+ peli.nombre )


                elif op_mos != "3":
                 
                        print("Por favor seleccione una opcion correcta")    

               
            elif res == '4':
                pass
            elif res == '5':
                print("Fin")
                break
                
            else:
                print("Por favor seleccione una opcion correcta")

# ----------------------------------------- Pantalla Principal --------------------------------------------------
print("****************************************************")
print("*  Curso: Lenguajes Formales y de Programación B+  *")
print("*        Nombre: David Eduardo Matias Ramirez      *")
print("*                Carnet: 202006644                 *")
print("****************************************************")
print("         Presione una tecla para continuar")
tecla = int(input())
if tecla == 1:
    menu()
elif tecla == 2:
    menu()   
elif tecla == 3:
    menu() 
elif tecla == 4:
    menu() 
elif tecla == 5:
    menu()          


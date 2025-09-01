# LIBRERIAS EMPLEADAS:
import getpass

#Definicion de variables:
global Cod_Novedad_1, Texto_Novedad_1, Fecha_Publicacion_Novedad_1, Fecha_Expiracion_Novedad_1
Cod_Novedad_1, Texto_Novedad_1, Fecha_Publicacion_Novedad_1, Fecha_Expiracion_Novedad_1 = 1, "Primera novedad", "2025-05-01", "2025-05-31"
    
global Cod_Novedad_2, Texto_Novedad_2, Fecha_Publicacion_Novedad_2, Fecha_Expiracion_Novedad_2
Cod_Novedad_2, Texto_Novedad_2, Fecha_Publicacion_Novedad_2, Fecha_Expiracion_Novedad_2 = 2, "Segunda novedad", "2025-05-05", "2025-06-05"
    
global Cod_Novedad_3, Texto_Novedad_3, Fecha_Publicacion_Novedad_3, Fecha_Expiracion_Novedad_3
Cod_Novedad_3, Texto_Novedad_3, Fecha_Publicacion_Novedad_3, Fecha_Expiracion_Novedad_3 = 3, "Tercera novedad", "2025-05-10", "2025-06-10"

global cont_ARG
cont_ARG=0
    
global cont_CHI
cont_CHI=0
    
global cont_BRA
cont_BRA=0

# DEFINICIÓN DE MENUS:
def volver():
    print("\n Volviendo...")
def cartel():
    print("\n ...en construcción...")

def Menu_Inicial():
    print("\n ---- Menu Principal ----")
    print("1. Gestion de Aerolineas")
    print("2. Aprobar/Denegar Pomociones")
    print("3. Gestion de Novedades")
    print("4. Reportes")
    print("5. Salir")

def Menu_1():
    print("\n ---- Gestion de Areolineas ----")
    print("a. Crear Aerolineas")
    print("b. Modificar Aerolinea")
    print("c. Eliminar Aerolinea")
    print("d. Volver")

def Menu_3():
    print("\n ---- Gestion de Novedades ----")
    print("a. Crear Novedades")
    print("b. Modificar Novedades")
    print("c. Eliminar Novedades")
    print("d. Ver Novedades")
    print("e. Volver")

def Menu_4():
    print("\n ---- Reportes ----")
    print("a. Reportes de Ventas (reservas con estado Confirmado)")
    print("b. Reporte de Vuelos")
    print("c. Reportes Usuarios")
    print("d. Volver")


# MANEJO DE NOVEDADES:
def Modificar_Novedades():
    global Cod_Novedad_1, Texto_Novedad_1, Fecha_Publicacion_Novedad_1, Fecha_Expiracion_Novedad_1
    
    global Cod_Novedad_2, Texto_Novedad_2, Fecha_Publicacion_Novedad_2, Fecha_Expiracion_Novedad_2
    
    global Cod_Novedad_3, Texto_Novedad_3, Fecha_Publicacion_Novedad_3, Fecha_Expiracion_Novedad_3
    
    Codigo = input("Ingrese el código de la novedad a modificar (1, 2 o 3): ")
    
    if Codigo == "1":
        Texto_Novedad_1 = input("Ingrese el nuevo texto de la novedad: ")
        Fecha_Publicacion_Novedad_1 = input("Ingrese la nueva fecha de publicación (YYYY-MM-DD): ")
        Fecha_Expiracion_Novedad_1 = input("Ingrese la nueva fecha de expiración (YYYY-MM-DD): ")
        print("Novedad 1 modificada correctamente.")
        
    elif Codigo == "2":
        Texto_Novedad_2 = input("Ingrese el nuevo texto de la novedad: ")
        Fecha_Publicacion_Novedad_2 = input("Ingrese la nueva fecha de publicación (YYYY-MM-DD): ")
        Fecha_Expiracion_Novedad_2 = input("Ingrese la nueva fecha de expiración (YYYY-MM-DD): ")
        print("Novedad 2 modificada correctamente.")
        
    elif Codigo == "3":
        Texto_Novedad_3 = input("Ingrese el nuevo texto de la novedad: ")
        Fecha_Publicacion_Novedad_3 = input("Ingrese la nueva fecha de publicación (YYYY-MM-DD): ")
        Fecha_Expiracion_Novedad_3 = input("Ingrese la nueva fecha de expiración (YYYY-MM-DD): ")
        print("Novedad 3 modificada correctamente.")
        
    else:
        print("Código de novedad inválido. Intente nuevamente.")

def Mostrar_Cambios_Novedades():
    global Cod_Novedad_1, Texto_Novedad_1, Fecha_Publicacion_Novedad_1, Fecha_Expiracion_Novedad_1
    
    global Cod_Novedad_2, Texto_Novedad_2, Fecha_Publicacion_Novedad_2, Fecha_Expiracion_Novedad_2
    
    global Cod_Novedad_3, Texto_Novedad_3, Fecha_Publicacion_Novedad_3, Fecha_Expiracion_Novedad_3

    print("Ver Novedades:")
    print(f"{'Código':<10}{'Texto':<30}{'Fecha Publicación':<20}{'Fecha Expiración':<20}")
    print("-" * 80)
    print(f"{1:<10}{Texto_Novedad_1:<30}{Fecha_Publicacion_Novedad_1:<20}{Fecha_Expiracion_Novedad_1:<20}")
    print(f"{2:<10}{Texto_Novedad_2:<30}{Fecha_Publicacion_Novedad_2:<20}{Fecha_Expiracion_Novedad_2:<20}")
    print(f"{3:<10}{Texto_Novedad_3:<30}{Fecha_Publicacion_Novedad_3:<20}{Fecha_Expiracion_Novedad_3:<20}")


# CREAR AEROLINEAS:
def Crear_Aerolineas():
    global cont_ARG
    
    global cont_CHI
    
    global cont_BRA
    
    print("\n Ingrese aerolinea")
    Nombre_Aerolinea = input ("Ingrese el nombre de la aerolinea ('FIN' para terminar): ")
    while len(Nombre_Aerolinea) > 100:
        print("Nombre de la aerolinea muy largo, vuelva a intentarlo")
        Nombre_Aerolinea = input ("Ingrese el nombre de la aerolinea ('FIN' para terminar): ")
    
    while Nombre_Aerolinea !="FIN":
        codigoIATA= input("Ingrese codigo IATA: ")
        while len(codigoIATA) !=3:
                print("Ingrese un codigo iata de 3 caracteres")
                codigoIATA= input("ingrese codigo IATA: ")
                
        descripcion= input("Descripcion ")
        while len(descripcion) > 200:
            print("Descripcion muy larga, vuelva a intentarlo")
            descripcion = input("Descripcion ")
        
        Codigo_Pais = input("Código de país (ARG, CHI o BRA): ")
        while Codigo_Pais !="ARG" and Codigo_Pais !="CHI" and Codigo_Pais !="BRA":
           print("Error con el codigo de pais")
           Codigo_Pais = input("Código de país (ARG, CHI o BRA): ")
           
        if Codigo_Pais =="ARG":
            cont_ARG += 1
        elif Codigo_Pais =="CHI":
            cont_CHI += 1
        elif Codigo_Pais =="BRA":
            cont_BRA += 1
            
        Nombre_Aerolinea = input ("Ingrese nombre de la aerolinea ('FIN' para terminar): ")
    Promedio_Aerolineas()

def Promedio_Aerolineas():
    if cont_ARG > cont_BRA and cont_ARG > cont_CHI:
        print(f"\n Hay más aerolineas provenientes de Argentina, con un total de {cont_ARG} aerolineas.")
        
    elif cont_CHI > cont_BRA and cont_CHI > cont_ARG:
        print(f"\n Hay más aerolineas provenientes de Chile, con un total de {cont_CHI} aerolineas")
        
    elif cont_BRA > cont_ARG and cont_BRA > cont_CHI:
        print(f"\n Hay más aerolineas provenientes de Brasil, con un total de {cont_BRA} aerolineas.")

    
# MANEJO DE MENUS:
def Primer_Sub_Menu():
    opc1=""
    
    while opc1!="d":
        Menu_1()
        opc1 = input("Seleccione una opcion ")
        
        if opc1 == "a":
            Crear_Aerolineas()
        elif opc1 == "b":
            cartel()
        elif opc1 == "c":
            cartel()
        elif opc1 == "d":
            volver()
        else:
            print("Opcion no valida, vuelva a intentarlo")

def Tercer_Sub_Menu():
    global opc3
    opc3= ""
    
    while opc3!="e":
        Menu_3()
        opc3 = input("Seleccione una opcion ")

        if opc3 == "a":
            cartel()
        elif opc3 == "b": 
            Modificar_Novedades()
        elif opc3 == "c":
            cartel()
        elif opc3 == "d":
            Mostrar_Cambios_Novedades()
        elif opc3 == "e":
            volver()
        else:
            print("Opcion no valida, vuelva a intentarlo")

def ManejoMenus():
    opc="0"
    
    while opc!="5":
        Menu_Inicial()
        opc = input("Seleccione una opcion ")
        
        if opc == "1":
            Primer_Sub_Menu()
        elif opc == "2":
            cartel()
        elif opc == "3":
            Tercer_Sub_Menu()
        elif opc == "4":
            cartel()
        elif opc == "5":
            print("\n Saliendo del programa")
        else:
            print("opcion invalida, intente de nuevo")


# INICIO DE SESION:
acc= ("false")
usuario = "admin@ventaspasajes777.com"
contraseña = ("admin")
i=0
m=3

nuevousuario= input("Ingrese su usuario ")

while nuevousuario !=usuario:
    print("Usuario incorrecto")
    nuevousuario= input("Ingrese su usuario ")  

while i<m:
    nuevacontraseña= getpass.getpass(f"intento{i+1}/{m}-Ingrese su contraseña ")
    if nuevacontraseña==contraseña:
        print("Bienvenido")
        acc="true"
        i=i+4
    else :
        print("Contraseña incorrecta")
        i= i+1 

if acc=="true":
    ManejoMenus()
else:
    print("\n ---- Acceso denegado, deteniendo programa ----")
# INTEGREANTES:
# del Valle, Marcos
# del Puerto, Alfio
# Renk Vivas, Santino
# Casagrande, Lautaro

# librerias empleadas
import getpass
import os
import time
from datetime import datetime

# constantes globales
MAX_USUARIOS = 10
MAX_AEROLINEAS = 5
MAX_VUELOS = 20
FILAS_POR_VUELO = 40
COLUMNAS_ASIENTOS = 6
TOTAL_FILAS_ASIENTOS = MAX_VUELOS * FILAS_POR_VUELO

# Array de usuarios (todos los tipos): [codigo, usuario, clave, tipo]
usuarios = [["" for _ in range(4)] for _ in range(MAX_USUARIOS)]

# Array de aerolineas: [codigo, nombre]
aerolineas = [["" for _ in range(2)] for _ in range(MAX_AEROLINEAS)]

# Array de vuelos: [codigo, aerolinea, origen, destino, fecha, hora, estado]
vuelos = [["" for _ in range(7)] for _ in range(MAX_VUELOS)]

# Array de precios de vuelos
precios_vuelos = [0.0 for _ in range(MAX_VUELOS)]

# Matriz de asientos
matriz_asientos = [["" for _ in range(COLUMNAS_ASIENTOS)] for _ in range(TOTAL_FILAS_ASIENTOS)]

# contadores
cant_usuarios = 0
cant_aerolineas = 0
cant_vuelos = 0

# Fecha actual (global)
fecha_actual = None

# limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# esperar una tecla
def esperar_tecla():
    import msvcrt
    msvcrt.getch()

# obtener una tecla sin enter
def obtener_tecla():
    import msvcrt
    return msvcrt.getch().decode('utf-8')

# Carteles definidos

def CartelEnConstruccion():
    print("================================================")
    print("                En construccion ...               ")
    print("================================================")

# Cartel del menu de logeo/registro
def CartelMenuPrincipal():
    print("\n╔═══════════════════════╗")
    print("║    Menu Principal     ║")
    print("╠═══════════════════════╣")
    print("║    1. Registrarme     ║")
    print("║    2. Iniciar Sesion  ║")
    print("║    3. Salir           ║")
    print("╚═══════════════════════╝")

# Carteles para el Admin
def CartelMenuAdministrador():
    print("\n╔═══════════════════════════════════╗")
    print("║          Menu Administrador       ║")
    print("╠═══════════════════════════════════╣")
    print("║   1. Gestion de Aerolíneas        ║")
    print("║   2. Aprobar/Denegar Promociones  ║")
    print("║   3. Gestion de Novedades         ║")
    print("║   4. Reportes                     ║")
    print("║   5. Salir                        ║")
    print("╚═══════════════════════════════════╝")

def CartelGestionAerolineas():
    print("\n╔════════════════════════════════╗")
    print("║     Gestion de Aerolineas      ║")
    print("╠════════════════════════════════╣")
    print("║     a) Crear Aerolinea         ║")
    print("║     b) Modificar Aerolinea     ║")
    print("║     c) Eliminar Aerolinea      ║")
    print("║     d) Volver                  ║")
    print("╚════════════════════════════════╝")

def CartelGestionNovedades():
    print("\n╔════════════════════════════════╗")
    print("║      Gestión de Novedades      ║")
    print("╠════════════════════════════════╣")
    print("║      a) Crear Novedad          ║")
    print("║      b) Modificar Novedad      ║")
    print("║      c) Eliminar Novedad       ║")
    print("║      d) Ver Novedades          ║")
    print("║      e) Volver                 ║")
    print("╚════════════════════════════════╝")

def CartelReportesAdmin():
    print("\n╔════════════════════════════════╗")
    print("║           Reportes             ║")
    print("╠════════════════════════════════╣")
    print("║     a) Reporte de Ventas       ║")
    print("║     b) Reporte de Vuelos       ║")
    print("║     c) Reporte de Usuarios     ║")
    print("║     d) Volver                  ║")
    print("╚════════════════════════════════╝")

# Carteles para el CEO
def CartelMenuCEO():
    print("\n╔════════════════════════════════╗")
    print("║            Menu CEO            ║")
    print("╠════════════════════════════════╣")
    print("║    1. Gestión de Vuelos        ║")
    print("║    2. Gestión de Promociones   ║")
    print("║    3. Reportes                 ║")
    print("║    4. Cerrar Sesión            ║")
    print("╚════════════════════════════════╝")

def CartelGestionVuelos():
    print("\n╔════════════════════════════════╗")
    print("║       Gestión de Vuelos        ║")
    print("╠════════════════════════════════╣")
    print("║       a) Crear Vuelo           ║")
    print("║       b) Modificar Vuelo       ║")
    print("║       c) Eliminar Vuelo        ║")
    print("║       d) Volver                ║")
    print("╚════════════════════════════════╝")

def CartelGestionPromociones():
    print("\n╔════════════════════════════════╗")
    print("║     Gestion de Promociones     ║")
    print("╠════════════════════════════════╣")
    print("║     a) Crear Promocion         ║")
    print("║     b) Modificar Promocion     ║")
    print("║     c) Eliminar Promocion      ║")
    print("║     d) Volver                  ║")
    print("╚════════════════════════════════╝")

def CartelReportesCEO():
    print("\n╔════════════════════════════════════════════════════════╗")
    print("║                        Reportes                        ║")
    print("╠════════════════════════════════════════════════════════╣")
    print("║    a) Reporte de ventas de mi Aerolinea                ║")
    print("║    b) Reporte de ocupacion de Vuelos de mi Aerolinea   ║")
    print("║    c) Volver                                           ║")
    print("╚════════════════════════════════════════════════════════╝")

# Carteles para el Usuario
def CartelMenuUsuario():
    print("\n╔════════════════════════════════════════════╗")
    print("║                 Menu Usuario               ║")
    print("╠════════════════════════════════════════════╣")
    print("║          1. Buscar Vuelos                  ║")
    print("║          2. Buscar asientos                ║")
    print("║          3. Reservar Vuelos                ║")
    print("║          4. Gestionar Reservas             ║")
    print("║          5. Ver Historial de Compras       ║")
    print("║          6. Ver Novedades                  ║")
    print("║          7. Cerrar Sesion                  ║")
    print("╚════════════════════════════════════════════╝")

def CartelGestionReservas():
    print("\n╔═══════════════════════════════════════════╗")
    print("║            Gestionar Reservas             ║")
    print("╠═══════════════════════════════════════════╣")
    print("║        a) Consultar Reservas              ║")
    print("║        b) Cancelar/Confirmar Reservas     ║")
    print("║        c) Volver                          ║")
    print("╚═══════════════════════════════════════════╝")

# Otros
def CartelRegreso():
    print("\n╔══════════════════╗")
    print("║ ...Regresando... ║")
    print("╚══════════════════╝")

def CartelInicioSesion():
    print("\n╔════════════════════════════════╗")
    print("║        Inicio de Sesion        ║")
    print("╚════════════════════════════════╝")

def CartelRegistroUsuario():
    print("\n╔════════════════════════════════════════════╗")
    print("║            Registro de Usuario             ║")
    print("╚════════════════════════════════════════════╝")

def CartelRegistroCEO():
    print("\n╔════════════════════════════════════════════╗")
    print("║            Registro de CEO                 ║")
    print("╚════════════════════════════════════════════╝")


# cargar usuarios iniciales
def CargaUsuarios():
    global cant_usuarios
    # Administrador
    usuarios[0][0] = "0"
    usuarios[0][1] = "admin@ventaspasajes777.com"
    usuarios[0][2] = "admin123"
    usuarios[0][3] = "administrador"
    
    # 5 CEOs (3 disponibles para registrar)
    usuarios[1][0] = "1"
    usuarios[1][1] = "ceo1@ventaspasajes777.com"
    usuarios[1][2] = "ceo123"
    usuarios[1][3] = "ceo"
    
    usuarios[2][0] = "2"
    usuarios[2][1] = "ceo2@ventaspasajes777.com"
    usuarios[2][2] = "ceo456"
    usuarios[2][3] = "ceo"
    
    # Espacios disponibles para CEOs 
    for i in range(3, 6):
        usuarios[i][0] = str(i)
        usuarios[i][1] = ""
        usuarios[i][2] = ""
        usuarios[i][3] = "ceo"
    
    # 4 Usuarios comunes (2 disponibles para registrar)
    usuarios[6][0] = "6"
    usuarios[6][1] = "usuario1@ventaspasajes777.com"
    usuarios[6][2] = "usuario123"
    usuarios[6][3] = "usuario"
    
    usuarios[7][0] = "7"
    usuarios[7][1] = "Usuario2@ventaspasajes777.com"
    usuarios[7][2] = "usuario456"
    usuarios[7][3] = "usuario"
    
    # Espacios disponibles para usuarios 
    for i in range(8, 10):
        usuarios[i][0] = str(i)
        usuarios[i][1] = ""
        usuarios[i][2] = ""
        usuarios[i][3] = "usuario"
    
    cant_usuarios = 10

# cargar aerolíneas iniciales
def CargaAerolineas():
    global cant_aerolineas
    aerolineas[0][0] = "0"
    aerolineas[0][1] = "Aerolíneas Argentinas"
    
    aerolineas[1][0] = "1"
    aerolineas[1][1] = "LATAM Airlines"
    
    aerolineas[2][0] = "2"
    aerolineas[2][1] = "Flybondi"
    
    aerolineas[3][0] = "3"
    aerolineas[3][1] = "GOL"
    
    aerolineas[4][0] = "4"
    aerolineas[4][1] = "Iberia"
    cant_aerolineas = 5

# buscar usuario 
def BuscarUsuario(usuario_ing, clave_ing, resultado):
  
    i = 0
    encontrado_local = False
    while i < cant_usuarios and not encontrado_local:
        if usuarios[i][1] == usuario_ing and usuarios[i][2] == clave_ing:
            encontrado_local = True
            resultado[0] = True
            resultado[1] = usuarios[i][3]
        else:
            i += 1
    if not encontrado_local:
        resultado[0] = False
        resultado[1] = ""

# buscar aerolínea
def BuscarAerolinea(cod_aero, resultado):
    i = 0
    encontrado_local = False
    while i < cant_aerolineas and not encontrado_local:
        if aerolineas[i][0] == cod_aero:
            encontrado_local = True
            resultado[0] = True
            resultado[1] = i
        else:
            i += 1
    if not encontrado_local:
        resultado[0] = False
        resultado[1] = -1

# buscar vuelo
def BuscarVuelo(cod_vuelo, resultado):
    i = 0
    encontrado_local = False
    while i < cant_vuelos and not encontrado_local:
        if vuelos[i][0] == cod_vuelo:
            encontrado_local = True
            resultado[0] = True
            resultado[1] = i
        else:
            i += 1
    if not encontrado_local:
        resultado[0] = False
        resultado[1] = -1

# comparar fechas
def FechaEsMayor(fecha_str):
    try:
        fecha_vuelo = datetime.strptime(fecha_str, "%d/%m/%Y")
        return fecha_vuelo > fecha_actual
    except ValueError:
        return False

# registrar un nuevo usuario
def Registrarme():
    global cant_usuarios
    
    limpiar_pantalla()
    print("\n--- Registro de Nuevo Usuario ---")
    print("¿Qué tipo de usuario desea registrar?")
    print("1. CEO")
    print("2. Usuario común")
    print("\nPresione la tecla correspondiente:")
    
    tipo_seleccionado = ""
    espacio_encontrado_idx = -1
    
    opcion_valida = False
    while not opcion_valida:
        tecla = obtener_tecla().lower()
        if tecla == '1':
            # Buscar un espacio para CEO
            i = 3
            encontrado = False
            while i <= 5 and not encontrado:
                if usuarios[i][1] == "":
                    encontrado = True
                    espacio_encontrado_idx = i
                else:
                    i += 1
            
            if not encontrado:
                print("\nNo hay espacios disponibles para registrar nuevos CEOs.")
                print("Presione cualquier tecla para continuar...")
                esperar_tecla()
                return
            
            tipo_seleccionado = "ceo"
            CartelRegistroCEO()
            opcion_valida = True
        elif tecla == '2':
            # Buscar un espacio para usuario 
            i = 8
            encontrado = False
            while i <= 9 and not encontrado:
                if usuarios[i][1] == "":
                    encontrado = True
                    espacio_encontrado_idx = i
                else:
                    i += 1
            
            if not encontrado:
                print("\nNo hay espacios disponibles para registrar nuevos usuarios.")
                print("Presione cualquier tecla para continuar...")
                esperar_tecla()
                return
            
            tipo_seleccionado = "usuario"
            CartelRegistroUsuario()
            opcion_valida = True
        else:
            print("\nOpción inválida. Intente nuevamente.")
    
    print("\nIngrese nombre de usuario:")
    nuevo_usuario = input()
    
    # Verificar si existe el usuario
    j = 0
    existe = False
    while j < cant_usuarios and not existe:
        if usuarios[j][1] == nuevo_usuario:
            existe = True
        else:
            j += 1
    
    if existe:
        print("\nEl nombre de usuario ya existe.")
        print("Presione cualquier tecla para continuar...")
        esperar_tecla()
        return
    
    print("Ingrese contraseña:")
    nueva_clave = getpass.getpass()  
    
    # Guardar usuario nuevo
    usuarios[espacio_encontrado_idx][0] = str(espacio_encontrado_idx)
    usuarios[espacio_encontrado_idx][1] = nuevo_usuario
    usuarios[espacio_encontrado_idx][2] = nueva_clave
    usuarios[espacio_encontrado_idx][3] = tipo_seleccionado
    print(f"\nUsuario registrado con éxito. Código asignado: {espacio_encontrado_idx}")
    print("Presione cualquier tecla para continuar...")
    esperar_tecla()

# inicializar asientos de un vuelo
def InicializarAsientosVuelo(indice_vuelo):
    fila_inicio = indice_vuelo * FILAS_POR_VUELO
    fila_fin = fila_inicio + FILAS_POR_VUELO
    
    fila_actual = fila_inicio
    while fila_actual < fila_fin:
        col_actual = 0
        while col_actual < COLUMNAS_ASIENTOS:
            if col_actual == 3:  # Pasillo del avion
                matriz_asientos[fila_actual][col_actual] = "L"
            else:
                if (fila_actual + col_actual) % 3 == 0:
                    matriz_asientos[fila_actual][col_actual] = "L"
                elif (fila_actual + col_actual) % 3 == 1:
                    matriz_asientos[fila_actual][col_actual] = "O"
                else:
                    matriz_asientos[fila_actual][col_actual] = "R"
            col_actual += 1
        fila_actual += 1

# Requerimiento 1
# crear vuelo
def CrearVuelo():
    global cant_vuelos
    if cant_vuelos >= MAX_VUELOS:
        print("\nNo se pueden crear más vuelos.")
        print("Presione cualquier tecla para continuar...")
        esperar_tecla()
        return
    print("\n¿Desea ver los vuelos ya cargados? (s/n)")
    opcion = input().lower()
    if opcion == 's':
        ListarVuelosExistentes()
    # Ingresar datos del vuelo
    print("\nIngrese código de aerolínea:")
    cod_aero = input()
    resultado_aero = [False, -1]
    BuscarAerolinea(cod_aero, resultado_aero)
    if not resultado_aero[0]:
        print("\nAerolínea no encontrada.")
        print("Presione cualquier tecla para continuar...")
        esperar_tecla()
        return
    print("Ingrese origen del vuelo:")
    origen = input()
    print("Ingrese destino del vuelo:")
    destino = input()
    print("Ingrese fecha de salida (dd/mm/yyyy):")
    fecha = input()
    print("Ingrese hora de salida (hh:mm):")
    hora = input()
    print("Ingrese precio:")
    precio = input()
    # Generar código de vuelo
    cod_vuelo = f"V{cant_vuelos+1:03d}"
    
    # Guardar vuelo
    vuelos[cant_vuelos][0] = cod_vuelo
    vuelos[cant_vuelos][1] = cod_aero
    vuelos[cant_vuelos][2] = origen
    vuelos[cant_vuelos][3] = destino
    vuelos[cant_vuelos][4] = fecha
    vuelos[cant_vuelos][5] = hora
    vuelos[cant_vuelos][6] = "A" # Estado activo
    precios_vuelos[cant_vuelos] = float(precio)
    cant_vuelos += 1
    indice_vuelo = cant_vuelos - 1
    InicializarAsientosVuelo(indice_vuelo)
    ReporteVuelosVigentes()

# listar vuelos existentes
def ListarVuelosExistentes():
    i = 0
    while i < cant_vuelos:
        if vuelos[i][6] == "A":  # Solo activos
            print(f"Código: {vuelos[i][0]}, Aerolínea: {vuelos[i][1]}, Origen: {vuelos[i][2]}, Destino: {vuelos[i][3]}")
        i += 1
    
    print("\nPresione cualquier tecla para continuar...")
    esperar_tecla()

# reporte de vuelos vigentes
def ReporteVuelosVigentes():
    # Array auxiliar para conteo
    conteo = [["" for _ in range(2)] for _ in range(MAX_AEROLINEAS)]
    
    i = 0
    while i < cant_aerolineas:
        conteo[i][0] = aerolineas[i][0]
        conteo[i][1] = 0
        i += 1
    # Contar vuelos vigentes
    i = 0
    while i < cant_vuelos:
        if vuelos[i][6] == "A" and FechaEsMayor(vuelos[i][4]):
            j = 0
            while j < cant_aerolineas:
                if vuelos[i][1] == conteo[j][0]:
                    conteo[j][1] += 1
                j += 1
        i += 1
    i = 0
    while i < cant_aerolineas:
        j = i + 1
        while j < cant_aerolineas:
            if conteo[i][1] < conteo[j][1]:
                temp_cod = conteo[i][0]
                temp_cant = conteo[i][1]
                
                conteo[i][0] = conteo[j][0]
                conteo[i][1] = conteo[j][1]
                
                conteo[j][0] = temp_cod
                conteo[j][1] = temp_cant
            j += 1
        i += 1
    # Mostrar reportes
    print("\n===============================================================")
    print("REPORTE DE VUELOS VIGENTES POR AEROLÍNEA")
    print("===============================================================")
    print("POSICIÓN\tAEROLÍNEA\t\t\tCANTIDAD DE VUELOS")
    print("----------------------------------------------------------------------------------------------------------------")
    
    total_vuelos = 0
    i = 0
    while i < cant_aerolineas:
        # Buscar nombre de aerolínea
        nombre = ""
        j = 0
        while j < cant_aerolineas:
            if aerolineas[j][0] == conteo[i][0]:
                nombre = aerolineas[j][1]
            j += 1
        print(f"{i}\t\t{nombre}\t\t\t{conteo[i][1]}")
        total_vuelos += conteo[i][1]
        i += 1
    
    print("----------------------------------------------------------------------------------------------------------------")
    print(f"TOTAL DE VUELOS VIGENTES: {total_vuelos}")
    
    # aerolínea con más vuelos
    if cant_aerolineas > 0:
        nombre_mayor = ""
        j = 0
        while j < cant_aerolineas:
            if aerolineas[j][0] == conteo[0][0]:
                nombre_mayor = aerolineas[j][1]
            j += 1
        print(f"Aerolínea con MAYOR cantidad de vuelos: {nombre_mayor} ({conteo[0][1]})")
        
        # aerolínea con menos vuelos
        nombre_menor = ""
        j = 0
        while j < cant_aerolineas:
            if aerolineas[j][0] == conteo[cant_aerolineas-1][0]:
                nombre_menor = aerolineas[j][1]
            j += 1
        print(f"Aerolínea con MENOR cantidad de vuelos: {nombre_menor} ({conteo[cant_aerolineas-1][1]})")
    
    print("\nPresione cualquier tecla para continuar...")
    esperar_tecla()

# modificar vuelo
def ModificarVuelo():
    print("\nIngrese código de vuelo a modificar:")
    cod_vuelo = input()
    resultado = [False, -1]
    BuscarVuelo(cod_vuelo, resultado)
    
    if not resultado[0]:
        print("\nVuelo no encontrado.")
        print("Presione cualquier tecla para continuar...")
        esperar_tecla()
        return
    
    idx = resultado[1]
    if vuelos[idx][6] == "B":
        print("\nEl vuelo está dado de baja. ¿Desea activarlo? (s/n)")
        opcion = input().lower()
        if opcion == 's':
            vuelos[idx][6] = "A"
        else:
            return
    # Mostrar datos actuales
    print("\nDatos actuales:")
    print(f"Aerolínea: {vuelos[idx][1]}")
    print(f"Origen: {vuelos[idx][2]}")
    print(f"Destino: {vuelos[idx][3]}")
    print(f"Fecha: {vuelos[idx][4]}")
    print(f"Hora: {vuelos[idx][5]}")
    print(f"Precio: ${precios_vuelos[idx]}")
    # Ingresar nuevos datos
    print("\nIngrese nueva aerolínea (dejar vacío para no cambiar):")
    nuevo_cod = input()
    if nuevo_cod != "":
        resultado_aero = [False, -1]
        BuscarAerolinea(nuevo_cod, resultado_aero)
        if resultado_aero[0]:
            vuelos[idx][1] = nuevo_cod
    print("Ingrese nuevo origen (dejar vacío para no cambiar):")
    nuevo_origen = input()
    if nuevo_origen != "":
        vuelos[idx][2] = nuevo_origen
    print("Ingrese nuevo destino (dejar vacío para no cambiar):")
    nuevo_destino = input()
    if nuevo_destino != "":
        vuelos[idx][3] = nuevo_destino
    print("Ingrese nueva fecha (dd/mm/yyyy) (dejar vacío para no cambiar):")
    nueva_fecha = input()
    if nueva_fecha != "":
        vuelos[idx][4] = nueva_fecha
    print("Ingrese nueva hora (hh:mm) (dejar vacío para no cambiar):")
    nueva_hora = input()
    if nueva_hora != "":
        vuelos[idx][5] = nueva_hora
    print("Ingrese nuevo precio (dejar vacío para no cambiar):")
    nuevo_precio = input()
    if nuevo_precio != "":
        precios_vuelos[idx] = float(nuevo_precio)
    print("\nVuelo modificado correctamente.")
    print("Presione cualquier tecla para continuar...")
    esperar_tecla()

# eliminar vuelo
def EliminarVuelo():
    print("\nIngrese código de vuelo a eliminar:")
    cod_vuelo = input()
    resultado = [False, -1]
    BuscarVuelo(cod_vuelo, resultado)
    
    if not resultado[0]:
        print("\nVuelo no encontrado.")
        print("Presione cualquier tecla para continuar...")
        esperar_tecla()
        return
    
    idx = resultado[1]
    if vuelos[idx][6] == "B":
        print("\nEl vuelo ya está dado de baja.")
        print("Presione cualquier tecla para continuar...")
        esperar_tecla()
        return
    print("\n¿Está seguro que desea eliminar el vuelo? (s/n)")
    confirmacion = input().lower()
    if confirmacion == 's':
        vuelos[idx][6] = "B"
        print("\nVuelo eliminado correctamente.")
    else:
        print("\nOperación cancelada.")
    
    print("Presione cualquier tecla para continuar...")
    esperar_tecla()

# Requerimiento 2
# buscar vuelos
def BuscarVuelos():
    print("\nIngrese fecha de salida (dd/mm/yyyy) o presione Enter para ver todos:")
    fecha_busqueda = input().strip()

    print("\n========================================================================================================")
    print("LISTADO DE VUELOS DISPONIBLES EN EL SISTEMA")
    print("========================================================================================================")
    print(f"{'CÓDIGO':<8}{'AEROLÍNEA':<20}{'ORIGEN':<15}{'DESTINO':<15}{'FECHA':<12}{'HORA':<8}{'PRECIO':>10}")
    print("-" * 90)

    total = 0
    i = 0
    while i < cant_vuelos:
        vuelo_activo = vuelos[i][6] == "A"
        vuelo_vigente = FechaEsMayor(vuelos[i][4])

        debe_mostrarse = vuelo_activo and vuelo_vigente

        # El usuario puede buscar por fecha
        if fecha_busqueda != "":
            if vuelos[i][4] != fecha_busqueda:
                debe_mostrarse = False

        if debe_mostrarse:
            # Buscar nombre aerolínea
            nombre_aero = ""
            j = 0
            while j < cant_aerolineas:
                if aerolineas[j][0] == vuelos[i][1]:
                    nombre_aero = aerolineas[j][1]
                j += 1

            print(f"{vuelos[i][0]:<8}{nombre_aero:<20}{vuelos[i][2]:<15}{vuelos[i][3]:<15}"
                  f"{vuelos[i][4]:<12}{vuelos[i][5]:<8}${precios_vuelos[i]:>9.2f}")
            total += 1

        i += 1

    print("-" * 90)
    print(f"Total de vuelos: {total}")
    print("\nPresione cualquier tecla para continuar...")
    esperar_tecla()

    i = 0
    while i < cant_vuelos:
        if vuelos[i][6] == "A" and FechaEsMayor(vuelos[i][4]):
            # Buscar nombre de aerolínea
            nombre_aero = ""
            j = 0
            while j < cant_aerolineas:
                if aerolineas[j][0] == vuelos[i][1]:
                    nombre_aero = aerolineas[j][1]
                j += 1

        print(f"{vuelos[i][0]:<8}{nombre_aero:<20}{vuelos[i][2]:<15}{vuelos[i][3]:<15}"
              f"{vuelos[i][4]:<12}{vuelos[i][5]:<8}${precios_vuelos[i]:>9.2f}")
        total += 1
    i += 1
    
    print("-----------------------------------------------------------------------------------------------------------------")
    print(f"Total de vuelos: {total}")
    print("\nPresione cualquier tecla para continuar...")
    esperar_tecla()

# Requerimiento 3
# buscar asientos
def BuscarAsientos():
    print("\nIngrese código de vuelo:")
    cod_vuelo = input()
    resultado = [False, -1]
    BuscarVuelo(cod_vuelo, resultado)
    
    if not resultado[0]:
        print("\nVuelo no encontrado.")
        print("Presione cualquier tecla para continuar...")
        esperar_tecla()
        return
    
    idx = resultado[1]
    if vuelos[idx][6] != "A":
        print("\nEl vuelo no está activo.")
        print("Presione cualquier tecla para continuar...")
        esperar_tecla()
        return
    
    if not FechaEsMayor(vuelos[idx][4]):
        print("\nEl vuelo no está vigente.")
        print("Presione cualquier tecla para continuar...")
        esperar_tecla()
        return
    # Mostrar mapa de asientos
    fila_inicio = idx * FILAS_POR_VUELO
    fila_fin = fila_inicio + FILAS_POR_VUELO
    
    print(f"\nMapa de asientos para el vuelo {cod_vuelo}:")
    print("Fila  A   B   C   |   D   E   F")
    print("-------------------------------------------")

    i = fila_inicio
    while i < fila_fin:
        num_fila = i - fila_inicio
        print(f"{num_fila:>2}    ", end="")  # fila alineada derecha, 2 espacios

        for j in range(COLUMNAS_ASIENTOS):
            if j == 3:
                print("|   ", end="")  # separador del pasillo
            print(f"{matriz_asientos[i][j]:^3}", end="")  # centrado en 3 espacios

        print()
        i += 1

    print("-------------------------------------------")
    print("L = Libre, O = Ocupado, R = Reservado")
    print("\nPresione cualquier tecla para continuar...")
    esperar_tecla()

# Funcionamiento de los menus
# Menú CEO
def MenuCEO():
    continuar_menu = True
    while continuar_menu:
        limpiar_pantalla()
        CartelMenuCEO()
        print("\nPresione la tecla correspondiente:")
        
        tecla = obtener_tecla().lower()
        if tecla == '1':
            continuar_submenu = True
            while continuar_submenu:
                limpiar_pantalla()
                CartelGestionVuelos()
                print("\nPresione la tecla correspondiente:")
                
                subopcion = obtener_tecla().lower()
                if subopcion == 'a':
                    CrearVuelo()
                elif subopcion == 'b':
                    ModificarVuelo()
                elif subopcion == 'c':
                    EliminarVuelo()
                elif subopcion == 'd':
                    continuar_submenu = False
                    CartelRegreso()
                    time.sleep(1)
                else:
                    print("\nOpción inválida. Intente nuevamente.")
                    time.sleep(1)
        elif tecla == '2':
            continuar_submenu = True
            while continuar_submenu:
                limpiar_pantalla()
                CartelGestionPromociones()
                print("\nPresione la tecla correspondiente:")
                
                subopcion = obtener_tecla().lower()
                if subopcion == 'a' or subopcion == 'b' or subopcion == 'c':
                    CartelEnConstruccion()
                    time.sleep(1)
                elif subopcion == 'd':
                    continuar_submenu = False
                    CartelRegreso()
                    time.sleep(1)
                else:
                    print("\nOpción inválida. Intente nuevamente.")
                    time.sleep(1)
        elif tecla == '3':
            continuar_submenu = True
            while continuar_submenu:
                limpiar_pantalla()
                CartelReportesCEO()
                print("\nPresione la tecla correspondiente:")
                
                subopcion = obtener_tecla().lower()
                if subopcion == 'a' or subopcion == 'b':
                    CartelEnConstruccion()
                    time.sleep(1)
                elif subopcion == 'c':
                    continuar_submenu = False
                    CartelRegreso()
                    time.sleep(1)
                else:
                    print("\nOpción inválida. Intente nuevamente.")
                    time.sleep(1)
        elif tecla == '4':
            continuar_menu = False
        else:
            print("\nOpción inválida. Intente nuevamente.")
            time.sleep(1)

# Menú Usuario
def MenuUsuario():
    continuar_menu = True
    while continuar_menu:
        limpiar_pantalla()
        CartelMenuUsuario()
        print("\nPresione la tecla correspondiente:")
        
        tecla = obtener_tecla().lower()
        if tecla == '1':
            BuscarVuelos()
        elif tecla == '2':
            BuscarAsientos()
        elif tecla == '3':
            CartelEnConstruccion()
            time.sleep(1)
        elif tecla == '4':
            continuar_submenu = True
            while continuar_submenu:
                limpiar_pantalla()
                CartelGestionReservas()
                print("\nPresione la tecla correspondiente:")
                
                subopcion = obtener_tecla().lower()
                if subopcion == 'a' or subopcion == 'b':
                    CartelEnConstruccion()
                    time.sleep(1)
                elif subopcion == 'c':
                    continuar_submenu = False
                    CartelRegreso()
                    time.sleep(1)
                else:
                    print("\nOpción inválida. Intente nuevamente.")
                    time.sleep(1)
        elif tecla == '5':
            CartelEnConstruccion()
            time.sleep(1)
        elif tecla == '6':
            CartelEnConstruccion()
            time.sleep(1)
        elif tecla == '7':
            continuar_menu = False
        else:
            print("\nOpción inválida. Intente nuevamente.")
            time.sleep(1)

# Menú Administrador
def MenuAdministrador():
    continuar_menu = True
    while continuar_menu:
        limpiar_pantalla()
        CartelMenuAdministrador()
        print("\nPresione la tecla correspondiente:")
        
        tecla = obtener_tecla().lower()
        if tecla == '1':
            continuar_submenu = True
            while continuar_submenu:
                limpiar_pantalla()
                CartelGestionAerolineas()
                print("\nPresione la tecla correspondiente:")
                
                subopcion = obtener_tecla().lower()
                if subopcion == 'a' or subopcion == 'b' or subopcion == 'c':
                    CartelEnConstruccion()
                    time.sleep(1)
                elif subopcion == 'd':
                    continuar_submenu = False
                    CartelRegreso()
                    time.sleep(1)
                else:
                    print("\nOpción inválida. Intente nuevamente.")
                    time.sleep(1)
        elif tecla == '2':
            CartelEnConstruccion()
            time.sleep(1)
        elif tecla == '3':
            continuar_submenu = True
            while continuar_submenu:
                limpiar_pantalla()
                CartelGestionNovedades()
                print("\nPresione la tecla correspondiente:")
                
                subopcion = obtener_tecla().lower()
                if subopcion == 'a' or subopcion == 'b' or subopcion == 'c' or subopcion == 'd':
                    CartelEnConstruccion()
                    time.sleep(1)
                elif subopcion == 'e':
                    continuar_submenu = False
                    CartelRegreso()
                    time.sleep(1)
                else:
                    print("\nOpción inválida. Intente nuevamente.")
                    time.sleep(1)
        elif tecla == '4':
            continuar_submenu = True
            while continuar_submenu:
                limpiar_pantalla()
                CartelReportesAdmin()
                print("\nPresione la tecla correspondiente:")
                
                subopcion = obtener_tecla().lower()
                if subopcion == 'a' or subopcion == 'b' or subopcion == 'c':
                    CartelEnConstruccion()
                    time.sleep(1)
                elif subopcion == 'd':
                    continuar_submenu = False
                    CartelRegreso()
                    time.sleep(1)
                else:
                    print("\nOpción inválida. Intente nuevamente.")
                    time.sleep(1)
        elif tecla == '5':
            continuar_menu = False
        else:
            print("\nOpción inválida. Intente nuevamente.")
            time.sleep(1)

# Procedimiento para iniciar sesión
def IniciarSesion():
    intentos = 0
    max_intentos = 3
    continuar_intentos = True
    
    while continuar_intentos and intentos < max_intentos:
        limpiar_pantalla()
        CartelInicioSesion()
        print("\nIngrese nombre de usuario:")
        usuario = input()
        print("Ingrese contraseña:")
        clave = getpass.getpass() 
        
        resultado = [False, ""]
        BuscarUsuario(usuario, clave, resultado)
        
        if resultado[0]:
            tipo = resultado[1]
            limpiar_pantalla()
            print(f"¡Bienvenido, {tipo}!")
            time.sleep(1)
            
            if tipo == "administrador":
                MenuAdministrador()
            elif tipo == "ceo":
                MenuCEO()
            elif tipo == "usuario":
                MenuUsuario()
            continuar_intentos = False  
        else:
            intentos += 1
            if intentos < max_intentos:
                print(f"\nUsuario o contraseña incorrectos. Intentos restantes: {max_intentos - intentos}")
                time.sleep(1)
            else:
                print("\nSe ha excedido el número máximo de intentos.")
                print("El programa se cerrará por seguridad.")
                time.sleep(2)
                continuar_intentos = False # Asegura la salida del bucle
                return False  
    
    return True  

# Menú principal
def MenuPrincipal():
    CargaUsuarios()
    CargaAerolineas()
    
    # Obtener fecha actual
    global fecha_actual
    fecha_actual = datetime.now()
    print(f"\nFecha actual del sistema: {fecha_actual.strftime('%d/%m/%Y')}")
    
    continuar_programa = True
    while continuar_programa:
        limpiar_pantalla()
        CartelMenuPrincipal()
        print("\nPresione la tecla correspondiente:")
        
        tecla = obtener_tecla().lower()
        if tecla == '1':
            Registrarme()
        elif tecla == '2':
            if not IniciarSesion():
                continuar_programa = False  #con IniciarSesion = False, el programa se detiene
        elif tecla == '3':
            print("\nSaliendo del sistema...")
            time.sleep(1)
            continuar_programa = False
        else:
            print("\nOpción inválida. Intente nuevamente.")
            time.sleep(1)

# Programa principal
def IniciarTodo():
    try:
        MenuPrincipal()
        limpiar_pantalla()
        print("Programa finalizado.")
    except KeyboardInterrupt:
        limpiar_pantalla()
        print("\nPrograma interrumpido por el usuario.")

if 1 == 1:
    IniciarTodo()
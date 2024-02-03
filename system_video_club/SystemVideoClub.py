from pathlib import Path
#extraemor el py e importamos una funcion de ese py
# 1 -
from user_system_create import System_Sis
# 2 -
from Rol_System import Syst_Rol
#3-
from Cliente_System import client_Sis
#4-
from Pelicula_System import pelicula_Sis
#5-
from Operadora_System import operadora_movil_sis
#6-
from EstadoCivil_System import Estado_Civil_Sis
#7-
from UsuarioTipo_System import Tipo_user_sis
#8-
from Genero_System import Genero_Sis
#9-
from Estado_system_create import Estado_Sis
#10-
from PelTipo_System import Tipo_Pelicula_Sis
#11-
from PelGenero import Pelicula_Genero_Sis
#12-
from Actores import Actores_Sis
#13-
from Directores_Cine import Directores_Cine_Sis
#14-
from ProductoraCine import Productora_Cine_Sis
#15 -
from Sistema_Alquiler import Sistema_alquiler_sis

import time

# 1 definimos la ruta del file

Fl_ruta_file = Path("C:/system_video_club/userSystem.txt")

Fl_ruta_file_menu = Path("C:/system_video_club/MENU.txt")

#proceso menu

def Pro_Mnu():
    print("╔═══════════════════════════════════════╗")
    print("║    Sistema de video club 2.0          ║")
    print("║═══════════════════════════════════════║")
    print("║ 1~ Ingreso Usuario del sistema        ║")
    print("║ 2~ Ingreso roles de usuario           ║")
    print("║ 3~ Ingreso de clientes                ║")
    print("║ 4~ Ingreso de Peliculas               ║")
    print("║ 5~ Mantenimiento-  Operador movil     ║")
    print("║ 6~ Mantemimiento - Estado civil       ║")
    print("║ 7~ Mantenimiento - Tipo de cliente    ║")
    print("║ 8~ Mantenimiento - Genero             ║")
    print("║ 9~ Mantenimento  - Estado             ║")
    print("║10~ Mantemimiento - Tipo de Pelicula   ║")
    print("║11~ Mantenimiento - Genero de pelicula ║")
    print("║12~ Mantenimiento - Actores de Cine    ║")
    print("║13~ Mantenimiento - Directores de Cine ║")
    print("║14~ Mantenimiento - Productora de cine ║")
    print("║15~ Alquile de peliculas               ║")
    print("║16~ Salir                              ║")
    print("║══════════════════════════╦════════════║")
    print("║                          ║            ║")
    print("║ Elija una opcion (1-16)  ║            ║")
    print("╚══════════════════════════╩════════════╝")


def Prc_Menu_Select(modulos):
    with open(Fl_ruta_file_menu, "r") as menu_file :
        print("╔═══════════════════════════════════════╗")
        print("║    Sistema de video club 2.0          ║")
        print("║═══════════════════════════════════════║")
        conta = 1
        for menufor in menu_file:
            if (str(conta) in modulos):
                lv_linea = "║" + menufor.rstrip("\n").ljust(39) + "║"
                print(lv_linea)
            conta += 1
           #print(lv_linea)
        print("║ 16~ Salir                             ║")
        print("║══════════════════════════╦════════════║")
        print("║                          ║            ║")
        print("║ Elija una opcion (1-16)  ║            ║")
        print("╚══════════════════════════╩════════════╝")

def loader():
    print("CARGANDO", end="")
    for _ in range(4):
        time.sleep(0.5)
        print(" ■ ", end="", flush=True)
    print()


def Obtener_modulos():
    Modulos = []
    # Preguntamos cuántos módulos desea adquirir
    print("EL LISTADO DE LOS MODULOS DISPONIBLES SON:")
    loader()
    #imprimir todo el menu, para que el usuario pueda escojer
    Pro_Mnu()
    while (True):
        Lv_respuesta = input("¿Cuántos módulos desea adquirir?(escriba 'todos' para obtener el modulo completo): ").strip().lstrip()
        if(Lv_respuesta.lower() == "todos"):
            #defino la cantidad de modulos disponilbles
            ln_cantidad_modulos = 15
            for num in range(1, ln_cantidad_modulos+1):
                Modulos.append(str(num))
            print("!Felicidades usted adquirio todo el  modulo del sistema de video club 2.0!")
            loader()
            print()
            #presento el modulo completo
            Prc_Menu_Select(Modulos)
            #Modulos = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",]
            break
        elif Lv_respuesta.isdigit():
            print("Ingrese la numeracion del módulo que desea adquirir...")
            Lv_respuesta = int(Lv_respuesta)
            if 1 <= Lv_respuesta <= 15:
                for _ in range(Lv_respuesta):
                    lv_modulo = input("MODULO =>").strip().lstrip()
                    if (lv_modulo.isdigit() and  1 <= int(lv_modulo) <= 15):
                        Modulos.append(lv_modulo)
                    else:
                        print("El valor que ingreso es incorrecto, no se tendra en cuenta esta respuesta")
                        print()
                print()
                Prc_Menu_Select(Modulos)
                break
            else:
                print("ERROR")
                print("Tenemos modulos disponibles del 1 hasta el 15")
                print()
        else:
            print("ERRROR 404: valor registrado no es valido, vuelva a intentarlo")
            print()

    return(Modulos)


try:
    #1 presentamos el ingreso del sistema
    print("Hola bienvenido al sistema de video club -- UNEMI")
    Lb_Existe = Fl_ruta_file.exists()
    if (Lb_Existe):
        Seleccion_modulos = Obtener_modulos()

        #si existe lo abro y leo el usuario y la contraseña
        #Pro_Mnu()
        #Prc_Menu_Select()
        #print("file pendiente")
        while(True):
            #lv_opcion_menu= input("Digite opcion(1-16)")
            lv_opcion_menu= input("Digite opcion(1-16):").lstrip().rstrip()
            if (lv_opcion_menu == "16"):
                print("Cerrando programa...")
                break
            elif lv_opcion_menu in Seleccion_modulos:
                if lv_opcion_menu == "1":
                    System_Sis()
                    print("***********************************************")
                    loader()
                    print()

                elif lv_opcion_menu == "2":
                    Syst_Rol()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "3":
                    client_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "4":
                    pelicula_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "5":
                    operadora_movil_sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "6":
                    Estado_Civil_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "7":
                    Tipo_user_sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "8":
                    Genero_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "9":
                    Estado_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "10":
                    Tipo_Pelicula_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "11":
                    Pelicula_Genero_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "12":
                    Actores_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "13":
                    Directores_Cine_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "14":
                    Productora_Cine_Sis()
                    print("***********************************************")
                    loader()
                    print()
                elif lv_opcion_menu == "15":
                    Sistema_alquiler_sis()
                    print("***********************************************")
                    loader()
                    print()
                Prc_Menu_Select(Seleccion_modulos)

            else:
                print("***********************************************")
                print("El modulo seleccionado no se encuetra disponible para usted, comuniquese con soporte tecnico al 180293832")
                print()
                #Limpiar pantalla
                Prc_Menu_Select(Seleccion_modulos)
                #Pro_Mnu();

    else:
        print("El sistema no se encuentra instalado de forma correcta, informe a sistemas")
        print("horario de atencion de lunes a viernes de 9 am a 17pm")
        print("cedula +59301548451")
except FileNotFoundError  as Err:
    print(print(f"no existe de arranque : {str(Err)}"))
    #fue un error en la escritura
except Exception as Err:
    print(f"Error del sistema solicite soporte {Err}")

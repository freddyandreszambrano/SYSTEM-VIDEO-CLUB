#Diccionario de datos del usuario

#importamos las librerias / bibliotecas
import json
from pathlib import Path
# libreria para obtener fecha y hora
from datetime import datetime
#modulo en python para crear conexiones de red y enviar mensajes a traves de la red
import socket

fl_ruta_file = Path("C:/system_video_club/PelClasifica.txt")
fl_ruta_secc = Path("C:/system_video_club/PelClasifica.txt")
fl_ruta_json = Path("C:/system_video_club/PelClasifica.json")

#estructura del diccionario de usuario

dcc_PelClasifica_system ={
    "Id_PelClasifica":"",
    "Clasificacion":"",
    "Observacion":""
}


def Prc_contrSecuencia(iv_registro):
    on_secuencia = 0;
    #accedemos al file.txt y recuperamos el registro
    with open("C:/system_video_club/control_secuencia.txt","r") as archivo_secuencia:
        #recorremos dicho archivo
        for registro in archivo_secuencia:
            #control = valor a recuperar
            #secuencia = la secuencia/ cantidad de registro
            control,secuencia = registro.strip().split(":");
            if (control == iv_registro):
                on_secuencia = int(secuencia)+1;
                break;
        return on_secuencia;







def Prc_updatesecuencia(Iv_registro,in_secuencia):
    ov_mensaje= "";
    linea = ""
    #accedemos al file de secuencia en modo lectura,
    with open("C:/system_video_club/control_secuencia.txt","r") as archivoSecuencia:
        for registro in archivoSecuencia:
            #control = valor a recuperar
            #secuencia = la secuencia / cantidad de registro
            control, secuencia = registro.strip().split(":");
            if (control == Iv_registro):
                secuencia = in_secuencia

            linea = linea + control +":"+str(secuencia)+"\n";
    #accedemos al file de secuencia en forma de escritura y agregamos el nuevo valor
    with open("C:/system_video_club/control_secuencia.txt","w") as archivo_secuencia:
        archivo_secuencia.write(linea)
        ov_mensaje = "SI"

    return ov_mensaje;












def pelclasifica_sis():
    # primer paso
    #arranca el sistema
    #pedimos al usuario del sistema ingresar los datos del nuevo usuario del sistema.
    print("ingrese los datos de clasificacion de pelicula")

    #PROCESO DE AUDITORIA
    #obtenemos  la fecha actual y hora actual
    fecha_actual = datetime.now()
    #obtenemos la ip del pc
    ip_pc = socket.gethostbyname(socket.gethostname())

    #recorremos el diccionario
    for clave in dcc_PelClasifica_system:
        #valor = input("{}:".format(clave));
        #dcc_PelClasifica_system[clave]=valor
        if (format(clave) == "Id_PelClasifica"):
            print(f"{clave}:....")
            valor = ""
        elif (format(clave) == "Clasificacion"):
            print("-----------------")
            print("Opciones de respuesta:")
            print("MPAA (Motion Picture Association of America)")
            print("G (General Audience)")
            print("PG (Parental Guidance)")
            print("PG-13 (Parents Strongly Cautioned)")
            print("R (Restricted)")
            print("NC-17 (No One 17 and Under Admitted)")
            print("U (Universal)")
            print("PG-7")
            print("PG-12")
            print("PG-16")
            print("PG-18")
            print()
            valor = input("{}:".format(clave))
        else:
            valor = input("{}:".format(clave))
        dcc_PelClasifica_system[clave]=valor
    #dcc_PelClasifica_system["Aud_Fech_Ingreso"]= fecha_actual
    #dcc_PelClasifica_system["Aud_Pc_Ingreso"] = ip_pc


    while (True):
        lv_guardar = input(str("Desea guardar los datos de la nueva clasificacion de pelicula S/N").upper());
        if (lv_guardar.upper() == "S"):
            #proceso de almacenamiento
            #recuperamos la secuencia de los registros guardados
            ln_sencc_registro = 0
            ln_sencc_registro = Prc_contrSecuencia("PelClasifica")
            with open(fl_ruta_file, "a")as archivo_generoPel:
                linea = "Id_PelClasifica"+str(ln_sencc_registro)+":";
                for clave, valor in dcc_PelClasifica_system.items():
                    if (format(clave) == "Id_PelClasifica"):
                        valor = "P.clas"+str(ln_sencc_registro)
                    linea += f"{clave} = {valor},";
                linea = linea.rstrip(",")+"\n";
                archivo_generoPel.write(linea)
            #actualizar la secuencia de registro
            lv_guardar=Prc_updatesecuencia("PelClasifica", ln_sencc_registro);
            if (lv_guardar.upper() == "SI"):
                print("la secuencia de los registros de la nueva clasificacion de pelicula fue ACTUALIZADO");
            else:
                print("la secuencia no fue actualizada, notifique al sistema");
            break
        elif(lv_guardar.upper() == "N"):
            #cancelamos el almacenamiento
            print("proceso cancelado");
            break
        else:
            print("opcion no valida");




















#Diccionario de datos del usuario

#importamos las librerias / bibliotecas
import json
from pathlib import Path
# libreria para obtener fecha y hora
from datetime import datetime
#modulo en python para crear conexiones de red y enviar mensajes a traves de la red
import socket

fl_ruta_file = Path("C:/system_video_club/SystemAlquiler.txt")
fl_ruta_secc = Path("C:/system_video_club/SystemAlquiler.txt")
fl_ruta_json = Path("C:/system_video_club/UsuarioTipoSystem.json")

#estructura del diccionario de usuario

dcc_UsuarioTipo_system ={
    "Id_Alquiler":"",
    "Id_Cliente":"",
    "Id_Pelicula":"",
    "Costo_de_alquiler":"",
    "Tiempo de alquiler":"",
    "Fecha_Alquiler":"",
    "Fecha_Devolucion":"",
    "Fecha_Regreso":"",
    "Genera-multa":"",
    "Observaciones":""
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












def Sistema_alquiler_sis():
    # primer paso
    #arranca el sistema
    #pedimos al usuario del sistema ingresar los datos del nuevo usuario del sistema.
    print("ingrese los datos del nuevo tipo de usuario")

    #PROCESO DE AUDITORIA
    #obtenemos  la fecha actual y hora actual
    fecha_actual = datetime.now()
    #obtenemos la ip del pc
    ip_pc = socket.gethostbyname(socket.gethostname())

    #recorremos el diccionario
    for clave in dcc_UsuarioTipo_system:
        #valor = input("{}:".format(clave));
        #dcc_UsuarioTipo_system[clave]=valor
        if (format(clave) == "Id_Alquiler"):
            print(f"{clave}: ...")
            valor = ""
        else:
            valor = input("{}:".format(clave))
        dcc_UsuarioTipo_system[clave]=valor
    #Proceso de auditoria
    #dcc_UsuarioTipo_system["Aud_Fech_Ingreso"]= fecha_actual
    #dcc_UsuarioTipo_system["Aud_Pc_Ingreso"] = ip_pc



    while (True):
        lv_guardar = input(str("Desea guardar los datos del nuevo tipo de usuario S/N").upper());
        if (lv_guardar.upper() == "S"):
            #proceso de almacenamiento
            #recuperamos la secuencia de los registros guardados
            ln_sencc_registro = 0
            ln_sencc_registro = Prc_contrSecuencia("PeliculaSystem")
            with open(fl_ruta_file, "a")as archivo_tipo_user:
                linea = "Sistema_ALQ"+str(ln_sencc_registro)+":";
                for clave, valor in dcc_UsuarioTipo_system.items():
                    if (format(clave) == "Id_Alquiler"):
                        valor = "Alq" + str(ln_sencc_registro)
                    linea += f"{clave} = {valor},";
                linea = linea.rstrip(",")+"\n";
                archivo_tipo_user.write(linea)
            #actualizar la secuencia de registro
            lv_guardar=Prc_updatesecuencia("PeliculaSystem", ln_sencc_registro);
            if (lv_guardar.upper() == "SI"):
                print("la secuencia de los registros del tipo de usuario fue ACTUALIZADA");
            else:
                print("la secuencia no fue actualizada, notifique al sistema");
            break
        elif(lv_guardar.upper() == "N"):
            #cancelamos el almacenamiento
            print("proceso cancelado");
            break
        else:
            print("opcion no valida");

#Sistema_alquiler_sis()


















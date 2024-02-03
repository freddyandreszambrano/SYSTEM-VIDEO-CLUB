#Diccionario de datos del usuario

#importamos las librerias / bibliotecas
import json
from pathlib import Path
# libreria para obtener fecha y hora
from datetime import datetime
#modulo en python para crear conexiones de red y enviar mensajes a traves de la red
import socket

fl_ruta_file = Path("C:/system_video_club/GeneroSystem.txt")
fl_ruta_secc = Path("C:/system_video_club/GeneroSystem.txt")
fl_ruta_json = Path("C:/system_video_club/GeneroSystem.json")

#estructura del diccionario de usuario

Dcc_genero_System ={
    "Id_Genero":"",
    "Nombre":"",
    "Genero":""
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












def Genero_Sis():
    # primer paso
    #arranca el sistema
    #pedimos al usuario del sistema ingresar los datos del nuevo usuario del sistema.
    print("ingrese los datos del Genero al que pertenece:")



    #PROCESO DE AUDITORIA
    #obtenemos  la fecha actual y hora actual
    fecha_actual = datetime.now()
    #obtenemos la ip del pc
    ip_pc = socket.gethostbyname(socket.gethostname())


    #recorremos el diccionario
    for clave in Dcc_genero_System:
        #valor = input("{}:".format(clave));
        #Dcc_genero_System[clave]=valor
        if (format(clave) == "Id_Genero"):
            print(f"{clave}:...")
            valor = ""
        elif(format(clave) == "Nombre"):
            print("--------------------")
            while (True):
                valor = input("{}:".format(clave))
                if valor.replace(" ", "").isalpha():
                    break
                else:
                    print("el valor ingresado es incorrecto")
        elif (format(clave) == "Genero"):
            print("------------")
            print("Ocpciones de respuesta:")
            print('1- Masculino')
            print("2- Femenino")
            while (True):
                valor = input("{}:".format(clave))
                if valor == "1":
                    valor = "Masculino"
                    break
                elif valor =="2":
                    valor = "Femenino"
                    break
                else:
                    print("opcion incorrecta, por favor valores correctos")
        else:
            valor = input("{}:".format(clave))
        Dcc_genero_System[clave]=valor
    #Dcc_genero_System["Aud_Fech_Ingreso"]= fecha_actual
    #Dcc_genero_System["Aud_Pc_Ingreso"] = ip_pc


    while (True):
        lv_guardar = input(str("Desea guardar los datos del usuario S/N").upper());
        if (lv_guardar.upper() == "S"):
            #proceso de almacenamiento
            #recuperamos la secuencia de los registros guardados
            ln_sencc_registro = 0
            ln_sencc_registro = Prc_contrSecuencia("GeneroPersonSystem")
            with open(fl_ruta_file, "a")as archivouser:
                linea = "GeneroPersonSystem"+str(ln_sencc_registro)+":";
                for clave, valor in Dcc_genero_System.items():
                    if (format(clave) == "Id_Genero"):
                        valor = "Gen"+str(ln_sencc_registro)
                    linea += f"{clave} = {valor},";
                linea = linea.rstrip(",")+"\n";
                archivouser.write(linea)
            #actualizar la secuencia de registro
            lv_guardar=Prc_updatesecuencia("GeneroPersonSystem", ln_sencc_registro);
            if (lv_guardar.upper() == "SI"):
                print("la secuencia de los generos de usuario fue ACTUALIZADA");
            else:
                print("la secuencia no fue actualizada, notifique al sistema");
            break
        elif(lv_guardar.upper() == "N"):
            #cancelamos el almacenamiento
            print("proceso cancelado");
            break
        else:
            print("opcion no valida");

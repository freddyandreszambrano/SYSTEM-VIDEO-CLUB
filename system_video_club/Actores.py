#Diccionario de datos del usuario

#importamos las librerias / bibliotecas
import json
from pathlib import Path
# libreria para obtener fecha y hora
from datetime import datetime
#modulo en python para crear conexiones de red y enviar mensajes a traves de la red
import socket

fl_ruta_file = Path("C:/system_video_club/Actores.txt")
fl_ruta_secc = Path("C:/system_video_club/Actores.txt")
fl_ruta_json = Path("C:/system_video_club/Actores.json")

#estructura del diccionario de usuario
dcc_actor_system ={
    "Id_Actor": "",
    "Nombre":"",
    "Apellido":"",
    "Genero":"",
    "Fecha de nacimiento":"",
    "Galardonada":"",
    "Oscar":""
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











def Actores_Sis():

    # primer paso
    #arranca el sistema
    #pedimos al usuario del sistema ingresar los datos del nuevo usuario del sistema.
    print("ingrese los datos de la nueva actor o actriz")

    #PROCESO DE AUDITORIA
    #obtenemos  la fecha actual y hora actual
    fecha_actual = datetime.now()
    #obtenemos la ip del pc
    ip_pc = socket.gethostbyname(socket.gethostname())


    #recorremos el diccionario
    for clave in dcc_actor_system:
        #valor = input("{}:".format(clave));
        #dcc_user_system[clave]=valor
        if (format(clave)=="Id_Actor"):
            print(f"{clave}: ......")
            valor=""
        elif(format(clave) == "Nombre"):
            print("--------------------")
            while (True):
                valor = input("{}:".format(clave))
                if valor.replace(" ", "").isalpha():
                    break
                else:
                    print("el valor ingresado es incorrecto")
        elif (format(clave) =="Genero"):
            print("-------------")
            print("¿A qué género pertenece el actor o actriz?")
            print("- Maculino")
            print("- Femenino")
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

        elif (format(clave)=="Galardonada"):
            print("-------------------")
            print("¿El actor o actriz ha sido galardonado?")
            valor = input("{}:".format(clave))
        elif(format(clave)=="Oscar"):
            print("-------------------")
            print("¿Ha ganado el actor o actriz un premio Oscar?")
            valor = input("{}:".format(clave))
        else:
            valor = input("{}:".format(clave));
        dcc_actor_system[clave]=valor
    #Proceso de auditoria
    #dcc_actor_system["Aud_Fech_Ingreso"]= fecha_actual
    #dcc_actor_system["Aud_Pc_Ingreso"] = ip_pc


    while (True):
        lv_guardar = input(str("Desea guardar los datos de la nueva actriz o actor S/N:").upper());
        if (lv_guardar.upper() == "S"):
            #proceso de almacenamiento
            #recuperamos la secuencia de los registros guardados
            ln_sencc_registro = 0
            ln_sencc_registro = Prc_contrSecuencia("ActorCine")
            with open(fl_ruta_file, "a")as archivo_Productora:
                linea = "Actor"+str(ln_sencc_registro)+":";
                for clave, valor in dcc_actor_system.items():
                    if (format(clave)=="Id_Actor"):
                        valor = "Act"+str(ln_sencc_registro)
                    linea += f"{clave} = {valor},";
                linea = linea.rstrip(",")+"\n";
                archivo_Productora.write(linea)
            #actualizar la secuencia de registro
            lv_guardar=Prc_updatesecuencia("ActorCine", ln_sencc_registro);
            if (lv_guardar.upper() == "SI"):
                print("la secuencia de los registros de la nueva actriz o actor fue ACTUALIZADO");
            else:
                print("la secuencia no fue actualizada, notifique al sistema");
            break
        elif(lv_guardar.upper() == "N"):
            #cancelamos el almacenamiento
            print("proceso cancelado");
            break
        else:
            print("opcion no valida");




















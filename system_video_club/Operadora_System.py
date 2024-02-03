#Diccionario de datos del usuario

#importamos las librerias / bibliotecas
import json
from pathlib import Path
# libreria para obtener fecha y hora
from datetime import datetime
#modulo en python para crear conexiones de red y enviar mensajes a traves de la red
import socket


fl_ruta_file = Path("C:/system_video_club/OperadoraSystem.txt")
fl_ruta_secc = Path("C:/system_video_club/OperadoraSystem.txt")
fl_ruta_json = Path("C:/system_video_club/OperadoraSystem.json")

#estructura del diccionario de usuario

dcc_operadora_system ={
    "Id_Operadora":"",
    "Nombre":"",
    "Operadora_movil":""
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












def operadora_movil_sis():
    # primer paso
    #arranca el sistema
    #pedimos al usuario del sistema ingresar los datos del nuevo usuario del sistema.
    print("ingrese los datos del nueva operadora")


    #PROCESO DE AUDITORIA
    #obtenemos  la fecha actual y hora actual
    fecha_actual = datetime.now()
    #obtenemos la ip del pc
    ip_pc = socket.gethostbyname(socket.gethostname())



    #recorremos el diccionario
    for clave in dcc_operadora_system:
        #valor = input("{}:".format(clave));
        #dcc_operadora_system[clave]=valor
        if (format(clave) == "Id_Operadora"):
            print(f"{clave}: ...")
            valor =  ""
        elif(format(clave) == "Nombre"):
            print("--------------------")
            while (True):
                valor = input("{}:".format(clave))
                if valor.replace(" ", "").isalpha():
                    break
                else:
                    print("el valor ingresado es incorrecto")

        elif(format(clave) == "Operadora_movil"):
            print("---------")
            print("las operadora vigentes son:")
            print("Claro")
            print("Movistar")
            print("CNT")
            print("Twenty")
            print("Aki")
            print("Supermaxi")
            print()
            valor = input("{}:".format(clave))
        else:
            valor = input("{}:".format(clave))
        dcc_operadora_system[clave]=valor
    #proceso de auditoria
    #dcc_operadora_system["Aud_Fech_Ingreso"]= fecha_actual
    #dcc_operadora_system["Aud_Pc_Ingreso"] = ip_pc



    while (True):
        lv_guardar = input(str("Desea guardar los datos de la nueva operadora S/N").upper());
        if (lv_guardar.upper() == "S"):
            #proceso de almacenamiento
            #recuperamos la secuencia de los registros guardados
            ln_sencc_registro = 0
            ln_sencc_registro = Prc_contrSecuencia("OperaMovil")
            with open(fl_ruta_file, "a")as archivo_operadora:
                linea = "OperaMovil"+str(ln_sencc_registro)+":";
                for clave, valor in dcc_operadora_system.items():
                    if (format(clave)== "Id_Operadora"):
                        valor = "Opr"+str(ln_sencc_registro)
                    linea += f"{clave} = {valor},";
                linea = linea.rstrip(",")+"\n";
                archivo_operadora.write(linea)
            #actualizar la secuencia de registro
            lv_guardar=Prc_updatesecuencia("OperaMovil", ln_sencc_registro);
            if (lv_guardar.upper() == "SI"):
                print("la secuencia de los registros de la operadora fue ACTUALIZADA");
            else:
                print("la secuencia no fue actualizada, notifique al sistema");
            break
        elif(lv_guardar.upper() == "N"):
            #cancelamos el almacenamiento
            print("proceso cancelado");
            break
        else:
            print("opcion no valida");




















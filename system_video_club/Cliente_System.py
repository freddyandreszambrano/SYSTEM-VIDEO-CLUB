#Diccionario de datos del usuario

#importamos las librerias / bibliotecas
import json
from pathlib import Path
# libreria para obtener fecha y hora
from datetime import datetime
#modulo en python para crear conexiones de red y enviar mensajes a traves de la red
import socket

fl_ruta_file = Path("C:/system_video_club/ClienteSystem.txt")
fl_ruta_secc = Path("C:/system_video_club/ClienteSystem.txt")
fl_ruta_json = Path("C:/system_video_club/ClienteSystem.txt")

#estructura del diccionario de usuario

dcc_cliente_system ={
    "Id_Cliente":"",
    "Nombre":"",
    "Apellido":"",
    "Genero":"",
    "Cedula":"",
    "Fecha de nacimiento":"",
    "Estado civil":"",
    "Direccion":"",
    "Referencia":"",
    "Operadora":"",
    "Celular":"",
    "Correo":"",
    "Tipo_cliente":"",
    "Estado":""
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
                temp_linea = control +":"+str(in_secuencia)+"\n";
            else:
                linea += control +":"+str(secuencia)+"\n";

        #ajuntamos todo los contenidos
        linea_final = linea + temp_linea
    #accedemos al file de secuencia en forma de escritura y agregamos el nuevo valor
    with open("C:/system_video_club/control_secuencia.txt","w") as archivo_secuencia:
        archivo_secuencia.write(linea_final)
        ov_mensaje = "SI"

    return ov_mensaje;


def client_Sis():
    # primer paso
    #arranca el sistema
    #pedimos al usuario del sistema ingresar los datos del nuevo usuario del sistema.
    print("Ingrese los datos del nuevo cliente")

    #PROCESO DE AUDITORIA
    #obtenemos  la fecha actual y hora actual
    fecha_actual = datetime.now()
    #obtenemos la ip del pc
    ip_pc = socket.gethostbyname(socket.gethostname())


    #recorremos el diccionario
    for clave in dcc_cliente_system:
        #valor = input("{}:".format(clave));
        #dcc_user_system[clave]=valor
        if (format(clave)=="Id_Cliente"):
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
        elif (format(clave)=="Genero"):
            print("--------------------------")
            print("¿A qué género pertenece?")
            print("1- Masculino")
            print("2- Femenino")
            while (True):
                valor = input("{}:".format(clave))
                if valor == "1":
                    valor = "Masculino"
                    break
                elif valor == "2":
                    valor = "Femenino"
                    break
                else:
                    print("Ingrese un valor correcto, por favor")
        elif(format(clave)=="Estado civil"):
            print("--------------------------")
            print("Opciones de respuesta:")
            print("- soltero")
            print("- casado")
            print("- divorsiado")
            print("- viudo")
            print("- union libre")
            print("- separado")
            valor = input("{}:".format(clave))
        elif(format(clave)=="Operadora"):
            print("--------------------------")
            print("Indique cuál es su operadora telefonica:")
            print("- Claro")
            print("- Movistar")
            print("- CNT")
            print("- Twenty")
            print("- Aki")
            print("- Supermaxi")
            valor= input("{}:".format(clave))
        elif (format(clave) == "Tipo_cliente"):
            print("--------------------------")
            print("Indique que tipo de cliente es:")
            print("- Normal")
            print("- Premiun")
            valor = input("{}:".format(clave))
        elif(format(clave) == "Estado"):
            print("--------------------------")
            print("Indique el estado del cliente:")
            print("- Activo")
            print("- Inactivo")
            valor = input("{}:".format(clave))
        else:
            valor = input("{}:".format(clave));
        dcc_cliente_system[clave]=valor
    #Proceso de auditoria
    #dcc_cliente_system["Aud_Fech_Ingreso"]= fecha_actual
    #dcc_cliente_system["Aud_Pc_Ingreso"] = ip_pc


    while (True):
        lv_guardar = input(str("Desea guardar los datos del nuevo cliente S/N").upper());
        if (lv_guardar.upper() == "S"):
            #proceso de almacenamiento
            #recuperamos la secuencia de los registros guardados
            ln_sencc_registro = 0
            ln_sencc_registro = Prc_contrSecuencia("ClientSystem")
            with open(fl_ruta_file, "a")as archivo_cliente:
                linea = "ClientSystem"+str(ln_sencc_registro)+":";
                for clave, valor in dcc_cliente_system.items():
                    if (format(clave)=="Id_Cliente"):
                        valor = "clte"+str(ln_sencc_registro)
                    linea += f"{clave} = {valor},";
                linea = linea.rstrip(",")+"\n";
                archivo_cliente.write(linea)
            #actualizar la secuencia de registro
            lv_guardar=Prc_updatesecuencia("ClientSystem", ln_sencc_registro);
            if (lv_guardar.upper() == "SI"):
                print("la secuencia de los registros del nuevo cliente fue ACTUALIZADO");
            else:
                print("la secuencia no fue actualizada, notifique al sistema");
            break
        elif(lv_guardar.upper() == "N"):
            #cancelamos el almacenamiento
            print("proceso cancelado");
            break
        else:
            print("opcion no valida");




















import csv
import sys
import os
import re
from datetime import datetime


def detectar_delimitador(archivo):
    with open(archivo, "r") as f:
        linea = f.readline()
    if ";" in linea:
        return ";"
    else:
        return ","


def procesar_nss(nss, nombre):
    if nss is None or "-" not in nss:
        return "SINRUT" + nombre.replace(" ", "")
    else:
        return nss.split("-")[0].replace(".", "")


def procesar_fecha(fecha):
    fecha_procesada = datetime.strptime(fecha, "%d/%m/%Y %H:%M")
    return fecha_procesada.strftime("%Y%m%d %H%M")


def procesar_estado(estado, nuevo_estado):
    if nuevo_estado in ["Checarse/Entrada", "Checarse/Salida"]:
        estado = nuevo_estado
    if estado == "Checarse/Entrada":
        return "1"
    elif estado == "Checarse/Salida":
        return "0"
    else:
        return "X"


def procesar_csv(archivo):
    delimitador = detectar_delimitador(archivo)
    with open(archivo, "r") as f:
        reader = csv.reader(f, delimiter=delimitador)
        next(reader)  # Saltar la cabecera
        datos = []
        for row in reader:
            nss = procesar_nss(row[1], row[2])
            hora = procesar_fecha(row[3])
            estado = procesar_estado(row[4], row[5])
            datos.append([nss, hora, estado])
        return datos


def generar_nombre_salida(nombre_entrada):
    nombre_entrada = re.sub("[^0-9a-zA-Z.]+", "_", nombre_entrada)
    nombre_entrada = nombre_entrada.replace(".csv", "")
    fecha_actual = datetime.now().strftime("%Y%m%d%H%M")
    return f"SALIDA/{fecha_actual}_{nombre_entrada}.txt"


def guardar_txt(datos, ruta_salida, ruta_salida_errores):
    with open(ruta_salida, "w") as f, open(ruta_salida_errores, "w") as f_errores:
        f.write("rut(9) AAAAMMDD HHMM E/S\n")
        f_errores.write("rut(9) AAAAMMDD HHMM E/S\n")
        for fila in datos:
            if fila[0].startswith("SINRUT") or fila[-1] == "X":
                if fila[-1] == "X":
                    fila[-1] = "VALOR_NO_RECONOCIDO"
                f_errores.write(" ".join(fila) + "\n")
            else:
                f.write(" ".join(fila) + "\n")


ruta_archivo = sys.argv[1]
ruta_salida = generar_nombre_salida(ruta_archivo)
ruta_salida_errores = ruta_salida.replace(".txt", "_ERRORES.txt")

if not os.path.exists("SALIDA"):
    os.makedirs("SALIDA")

datos = procesar_csv(ruta_archivo)
guardar_txt(datos, ruta_salida, ruta_salida_errores)

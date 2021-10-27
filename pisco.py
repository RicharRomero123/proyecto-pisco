#!/usr/bin/python3
# -*- coding: UTF-8

import os
import time
import requests
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict
from colorama import Fore, init
init()

#colores
verde = Fore.GREEN
lverde = Fore.LIGHTGREEN_EX
rojo = Fore.RED
lrojo = Fore.LIGHTRED_EX
amarillo = Fore.YELLOW
blanco = Fore.WHITE
cyan = Fore.CYAN
violeta = Fore.MAGENTA
azul = Fore.BLUE
lazul = Fore.LIGHTBLUE_EX

################### FUNCIONES DE LA HERRAMIENTA
# sistema de numeros de dni
def consultadni():
    dni = input("Escribe el dni: ")
    url = f"https://dniruc.apisperu.com/api/v1/dni/{dni}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImdyYWR5Mzl1X24yOTFpQG5hZnhvLmNvbSJ9.cl5KQzsXaRuLuwEUWNJDLX_Zh2R_HkBsn9_YEP4keio"
    data = requests.get(url)
    respuesta = data.json()
    ndni = respuesta['dni']
    if ndni == '':
        print("NUMERO DE DNI NO ENCONTRADO")
    elif ndni is None:
        print("NUMERO DE DNI NO ENCONTRADO")
    else:
        name = respuesta['nombres']
        apellidop = respuesta['apellidoPaterno']
        apellidom = respuesta['apellidoMaterno']
        codigov = respuesta['codVerifica']
        print(f"{verde}NOMBRE:{blanco} {name}\n{verde}APELLIDO PATERNO:{blanco} {apellidop}\n{verde}APELLIDO MATERNO:{blanco} {apellidom}\n{verde}DNI:{blanco} {dni}\n{verde}CÓDIGO:{blanco} {codigov}\n")

#sistema de verificacion de ruc
def consultaruc():
    token = '?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImdyYWR5Mzl1X24yOTFpQG5hZnhvLmNvbSJ9.cl5KQzsXaRuLuwEUWNJDLX_Zh2R_HkBsn9_YEP4keio'
    rucki = input("RUC >> ")
    response = requests.get("https://dniruc.apisperu.com/api/v1/ruc/" +rucki +token)
    for key, value in response.json().items():
        print("[-] %s: %s" % (key, value))

# sistema de busqueda de direccion de casa
def direccion_casa():
    numero = input("INGRESA DNI: ")
    url = f"http://cpe.facturaperuana.com/cliente/apisutran_dni/{numero}"
    resp = requests.get(url)
    texto = resp.text
    new_dni = texto[3:]
    new_dni2 = new_dni[:-3]
    corte = new_dni2.split(sep=',')
    for i in corte:
        print(">> "+i)

# sistema de busqueda de números telefónicos
def consultaindividual():
    numerotelefonico = input("[+] ESCRIBE EL NÚMERO TELEFÓNICO: ")
    url1 = f"http://apilayer.net/api/validate?access_key=a34d97f03e51e991d6699b9de0b8694c&number={numerotelefonico}&country_code&format=1"
    url2 = f"https://phonevalidation.abstractapi.com/v1/?api_key=49f4fe982a1b4f5cacdde03608161cdd&phone={numerotelefonico}"

    data1 = requests.get(f"{url1}")
    data2 = requests.get(f"{url2}")

    dataJson1 = data1.json()
    dataJson2 = data2.json()

    existeono = dataJson1['local_format']

        # datos url numero 1
    validar = dataJson1['valid']
    prefijo = dataJson1['country_prefix']
    codigo = dataJson1['country_code']
    codigo_pais = dataJson1['country_name']
    localizacion = dataJson1['location']
        #datos url numero 2
    formato_local_pais = dataJson2['format']['local']
    carril = dataJson2['carrier']
    if existeono == '':
        print(f"{lrojo}NO EXISTE ")
    elif existeono is None:
        print(f"{lrojo}NO EXISTE ")
    else:
        print(f"{azul}ES VALIDO ? :{blanco} {validar}\n{azul}PREFIJO :{blanco} {prefijo}\n{azul}FORMATO LOCAL :{blanco} {formato_local_pais}\n{azul}CODIGO DEL PAIS :{blanco} {codigo}\n{azul}PAIS :{blanco} {codigo_pais}\n{azul}LOCALIZACIÓN :{blanco} {localizacion}\n{azul}COMPAÑIA :{blanco} {carril}\n")

# consulta de nombres y apellidos por dni
def consulta_por_nombres():
    name = input("ESCRIBE EL NOMBRE: ")
    apellidop = input("ESCRIBE EL APELLIDO PATERNO: ")
    apellidom = input("ESCRIBE EL APELLIDO MATERNO: ")
    url = "https://buscardni.xyz/buscador/ejemplo_ajax_proceso.php"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = f"APE_PAT={apellidop}&APE_MAT={apellidom}&NOMBRES={name}"
    resp = requests.post(url, headers=headers, data=data)
    text = resp.text
    soup = BeautifulSoup(text, "lxml")
    text2 = soup.get_text()
    new_b = text2[131:]
    characters = "ver"
    string = ''.join( x for x in new_b if x not in characters)
    print(string)


def portada():
    print(f"""{violeta}       .       .        .    .       .     . 
 ██████╗ ██╗███████╗ ██████╗ ██████╗ .  .   .   .  .   . .   .
 ██╔══██╗██║██╔════╝██╔════╝██╔═████╗  ▄▀▀▀▀▀▄{violeta}.  .  .  
 ██████╔╝██║███████╗██║     ██║██╔██║ ▐░▄░░░▄░▌{violeta}.  .   . 
 ██╔═══╝ ██║╚════██║██║     ████╔╝██║ ▐░▀▀░▀▀░▌{violeta}  .   .   . 
 ██║     ██║███████║╚██████╗╚██████╔╝  ▀▄░═░▄▀{violeta} .   .     
 ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═════╝ . ▐░▀▄▀░▌ {violeta}    . .   
 {verde}PROGRAMADO POR D4VID.0                  {cyan}Versión 2.1 .   .
 {lverde}═══════════════════════════════════════════════════════
 {lrojo}INSTAGRAM: {blanco}d4vid.0day
 {blanco}GITHUB:{blanco} https://github.com/Monkey-hk4
 {azul}TELEGRAM:{blanco} mhk4_0
 {lazul}DONACIONES:{blanco} https://www.paypal.com/paypalme/davidhk4
 {lverde}═══════════════════════════════════════════════════════
    """)
    time.sleep(0.5)

def menu_ayuda():
    print("""
 MENU DE OPCIONES - PROYECTO PISC0
 ÚLTIMA ACTUALIZACIÓN 27/10/2021 
 
  COMANDO                  INFORMACIÓN 

 [ dni ] Mostar Nombres y Apellidos de un número de dni.
 [ casa ] dirección de casa donde vive una persona por su n° de dni.
 [ ruc ] Datos de una RUC, titular, razón social, etc.
 [ numero ] Información de un número telefónico. 
 [ buscar ] Buscar número de dni mediente nombres y apellidos.

 El script se va a actualizar todos los meses y se va a añadir más opciones. 
    """)                                    

def eleccion():
    opc = input(f"{verde}[pisco@root]>> ")
    if opc == "dni":
        consultadni()
        eleccion()
    elif opc == "help":
        menu_ayuda()
        eleccion()
    elif opc == "ayuda":
        menu_ayuda()
        eleccion()
    elif opc == "?":
        menu_ayuda()
        eleccion()
    elif opc == "casa":
        direccion_casa()
        eleccion()
    elif opc == "ruc":
        consultaruc()
        eleccion()
    elif opc == "numero":
        consultaindividual()
        eleccion()
    elif opc == "buscar":
        consulta_por_nombres()
        eleccion()
    elif opc == "clear":
        os.system("clear")
        portada()
        eleccion()
    elif opc == "cls":
        os.system("cls")
        portada()
        eleccion()    
    else:
        print(f"""{rojo}
    ERROR 404 OPCIÓN INCORRECTA x_x 
        """)
        eleccion()
    
# inicio de tool
if __name__ == "__main__":
    portada()
    eleccion()
import requests
import json
def consultacorreo():
    correo = input("introduce el correo: ")
    response = requests.get("https://emailvalidation.abstractapi.com/v1/?api_key=26d33d30ce364696b504faefb0e51095&email=" +correo)
    for key, value in response.json().items():

        print("=> %s: %s" % (key, value))

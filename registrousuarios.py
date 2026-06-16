"""
Crear una aplicación que permita:

Registrar usuarios.
Validar información.
Guardar en archivo.
Capturar errores.
Mostrar mensajes amigables.

Deben utilizar validaciones

El formato del archivo es:
Nombre,Carlos 
Edad,25
Ana,30
Pedro,22

Modificar el programa para:

Buscar usuarios
Evitar usuarios duplicados
Validar un archivo el momento de leerlo y en casso de errores mostrarlos
Crear archivo de errores. Meter los datos buenos en un archivo y los malos en otro
Registrar fecha y hora de creación.
Lo quiere en txt
"""

import os
from datetime import datetime

Nombre_Archivo = "usuarios.txt"
Archivos_Validos = "validos.txt"
Archivo_Errores = "errores.txt"

def crear_archivos():
    archivos = [Nombre_Archivo, Archivos_Validos, Archivo_Errores]

    for archivo in archivos:
        if not os.path.exists(archivo):
            with open(archivo, "w", encoding="utf-8") as f:
                pass

def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ").strip() #Solicita nombre

#Validacion nombre
    if not nombre:
        print("El nombre no puede estar vacío")
        return
    
    if not nombre.replace(" ","").isalpha(): # .isalpha → hace que los caracteres sean solo letras
        print("El nombre solo debe contener letras.")
        return

#Validacion edad  
    try:
        edad = int(input("Ingrese la edad: "))

        if edad <= 0:
            print("La edad debe ser mayor que 0")
            return
        
    except ValueError:
        print("La edad debe ser un número entero")
        return
    
    with open(Nombre_Archivo, "r", encoding="utf-8") as archivo:

        for linea in archivo:
            
            if not linea in archivo:
                if not linea.strip():
                    continue
                
            partes = linea.strip().split(",")
            nombre_guardado = partes[0]

            if nombre.lower() == nombre_guardado.lower():
                print("Ese usuario ya está registrado")
                return
            
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(Nombre_Archivo, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{edad},{fecha}\n")
            
def mostrar_usuarios():
    with open(Nombre_Archivo, "r", encoding="utf-8") as archivo:
        print("\n --- USUARIOS REGISTRADOS ---")

        for linea in archivo:
            partes = linea.strip().split(",")

            if len(partes) != 3:
                print(f"Registro invalido: {linea.strip()}")
                continue

            nombre = partes[0]
            edad = partes[1]
            fecha = partes[2]

            try:
                edad = int(edad)
            except ValueError:
                print(f"Edad invalida: {linea.strip()}")
                continue

            print(f"Nombre: {nombre} | Edad: {edad} | Registro: {fecha}")

def buscar_usuario():
    nombre_buscar = input("Ingrese el nombre a buscar: ").strip()
    encontrado = False

    with open(Nombre_Archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            
            if len(partes) != 3:
                print(f"Registro inválido: {linea.strip()}")
                continue
            nombre = partes[0]
            edad = partes[1]
            fecha = partes[2]

            if nombre.lower() == nombre_buscar.lower():
                print("Usuario encontado: ")
                print(f"Nombre: {nombre} | Edad: {edad} | Registro: {fecha}")
                encontrado = True
                break #Tambien funciona como validación ya que aunque existieran duplicados, se quedaría con el primero que encuentre

    if not encontrado:
        print("Usuario no encontrado")

def validar_archivo():

    with open(Nombre_Archivo,"r", encoding="utf-8") as archivo, \
         open(Archivos_Validos, "w", encoding="utf-8") as validos,\
         open(Archivo_Errores, "w", encoding="utf-8") as errores:
        
        for linea in archivo:
            registro_valido = True
            partes = linea.strip().split(",")
            if len(partes) != 3:
                    registro_valido = False

            if len(partes) == 3:
                nombre = partes[0]
                edad = partes[1]
                fecha = partes[2]
            
                if not nombre:
                    registro_valido = False

                if not nombre.replace(" ", "").isalpha():
                    registro_valido = False

                if not fecha:
                    registro_valido = False

                try:
                    edad = int(edad)
                    if edad <= 0:
                        registro_valido = False
                except ValueError:
                    registro_valido = False

                try:
                    datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    registro_valido = False
                    
            if registro_valido:
                validos.write(linea)
            else:
                errores.write(linea)
    

def menu():
    crear_archivos()

    while True:
        print("\n===== MENÚ =====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Validar archivo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            mostrar_usuarios()

        elif opcion == "3":
            buscar_usuario()

        elif opcion == "4":
            validar_archivo()
            print("Archivo validado")

        elif opcion == "5":
            print("Programa finalizado")
            break

        else:
            print("Opción no válida")

menu()

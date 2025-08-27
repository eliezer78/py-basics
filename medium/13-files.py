# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo XML y JSON 
# que guarde los siguientes datos (haciendo uso de la sintaxis 
# correcta en cada caso):
# - Nombre
# - Edad
# - Rol
# - Listado de lenguajes de programación (3 O 4)
# Muestra el contenido de los archivos.
# Borra los archivos.
#
# Utilizando la lógica de creación de los archivos anteriores, 
# crea un programa capaz de leer y transformar en una misma clase 
# PERSONA de tu lenguaje los datos almacenados en el XML y el JSON.

import json
class Persona:
    def __init__(self, nombre, edad, rol, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol
        self.lenguajes = lenguajes

    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, "
                f"Rol: {self.rol}, "
                f"Lenguajes: {'/'.join(self.lenguajes)}")
        
persona1 = Persona("Diego", 25, "Desarrollador",["python","javascript","C++"])

datos = {"nombre" : persona1.nombre, 
         "edad":persona1.edad,
         "rol":persona1.rol,
         "lenguajes":persona1.lenguajes}

# Crear JSON
json_file = "persona.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4, ensure_ascii=False)


# Mostrar contenido JSON
print("Contenido JSON:")
with open(json_file, "r", encoding="utf-8") as f:
    print(f.read())


# Leer JSON y crear objeto Persona
json_file = "persona.json"

with open(json_file, "r", encoding="utf-8") as f:
    datos_json = json.load(f)

persona_json = Persona(
    datos_json["nombre"],
    datos_json["edad"],
    datos_json["rol"],
    datos_json["lenguajes"]
)

print(persona_json)

"""
import xml.etree.ElementTree as ET

# Crear XML
xml_file = "cliente.xml"
root = ET.Element("cliente")

ET.SubElement(root, "nro_orden").text = "50556455"
ET.SubElement(root, "name").text = datos["nombre"]
ET.SubElement(root, "last_name").text = str(datos["edad"])
ET.SubElement(root, "date").text = datos["nacimiento"]

tree = ET.ElementTree(root)
tree.write(xml_file, encoding="utf-8", xml_declaration=False)

# Mostrar contenido XML
print("\nContenido XML:")
with open(xml_file, "r", encoding="utf-8") as f:
    print(f.read())

import os
# Borrar archivos
# os.remove(json_file)
# os.remove(xml_file)
# print("\nArchivos borrados.")
"""
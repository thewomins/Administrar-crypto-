import json

def leer_json(nombre):
        with open(nombre) as file:
            data = json.load(file)
        return data

def guardar_json(diccionario, nombre):
        with open(nombre, 'w') as file:
            json.dump(diccionario, file, indent=4)
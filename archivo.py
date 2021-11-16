import json

def open_json(nombre_archivo):
    nombre=nombre_archivo+".json"
    try:
        file = open(nombre, 'r')
        return file
    except:
        open(nombre, "x")
        print(nombre)
        open_json(nombre_archivo)

def leer_json(nombre_archivo):
    try:
        file = open_json(nombre_archivo)
        data = json.load(file)
    except:
        data=formatea_file()
    return data

def formatea_file():
    data={}
    data["USD"]={}
    data["USD"]['compras']=[]
    data["USD"]['ventas']=[]
    return data

def guardar_json(diccionario, nombre):
    with open(nombre, 'w') as file:
        json.dump(diccionario, file, indent=4)
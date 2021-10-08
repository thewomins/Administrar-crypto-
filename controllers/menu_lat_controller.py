import tkinter as tk
from navegador import navegador

class Lat_controller:
    def __init__(self):
        a=0

    def boton_press(self, param):
        navegador.notify(param)

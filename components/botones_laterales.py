import tkinter as tk
from navegador import navegador

class botones:
    def __init__(self,padre):
        self.padre = padre

    def text_titulos_padre(self, padre, texto2, color):
            textol = tk.Label(padre, text= texto2, bg=color, fg='white', font=("google sans medium", 18))    
            return textol

    def boton_lateral(self, padre, color,texto):
            frame_izquierda = tk.Frame(padre, bg= color)
            frame_izquierda.focus_set()
            frame_izquierda.bind("<Button-1>",lambda _: self.boton_press())
            self.text_titulos_padre(frame_izquierda, texto, color).place(anchor="center", relx=0.5, rely=0.5) 
            return frame_izquierda

    def boton_press(self):
        navegador.notify()
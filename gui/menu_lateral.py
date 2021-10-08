import tkinter as tk
from components.components import Components

class Menu_lateral:
    def __init__(self,padre, controller):
        self.padre = padre
        self.controller=controller
        self.components = Components(self.padre)

    def frame_menu_lateral(self):
        menu_lateral = tk.Frame(self.padre,bg='#102027')
        self.menu_interior(menu_lateral)
        return menu_lateral

    def menu_interior(self, padre):
        frame_interior = self.components.menu_frames(padre,'blue')
        a=self.boton_lateral(frame_interior, 'red', 'Agregar compra dolares', 12)
        a.place(relwidth=1, relheight=0.1)
        b=self.boton_lateral(frame_interior, 'green', 'Agregar compra crypto', 12)
        b.place(rely=0.11, relwidth=1, relheight=0.1)
        c=self.boton_lateral(frame_interior, 'yellow', 'c', 18)
        c.place(rely=0.22, relwidth=1, relheight=0.1)

        h=self.boton_lateral(frame_interior, 'yellow', 'Volver', 18)
        h.place(rely=0.88, relwidth=1, relheight=0.1)

    def boton_lateral(self, padre, color,texto, tamano):
            frame_izquierda = tk.Frame(padre, bg= color)
            frame_izquierda.focus_set()
            text=tk.Label(frame_izquierda, text= texto, bg=color, fg='white', font=("google sans medium", tamano))
            text.place(anchor="center", relx=0.5, rely=0.5) 
            frame_izquierda.bind("<Button-1>",lambda _: self.controller.boton_press(texto))
            return frame_izquierda
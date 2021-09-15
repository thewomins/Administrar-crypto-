import tkinter as tk
from components.components import Components
from components.botones_laterales import botones

class Menu_lateral:
    def __init__(self,padre):
        self.padre = padre
        self.components = Components(self.padre)
        self.botones = botones(self.padre)

    def frame_menu_lateral(self):
        menu_lateral = tk.Frame(self.padre,bg='#102027')
        self.menu_interior(menu_lateral)
        return menu_lateral

    def menu_interior(self, padre):
        frame_interior = self.components.menu_frames(padre,'blue')
        a=self.botones.boton_lateral(frame_interior, 'red', 'a')
        a.place(relwidth=1, relheight=0.1)
        b=self.botones.boton_lateral(frame_interior, 'green', 'b')
        b.place(rely=0.11, relwidth=1, relheight=0.1)
        c=self.botones.boton_lateral(frame_interior, 'yellow', 'c')
        c.place(rely=0.22, relwidth=1, relheight=0.1)
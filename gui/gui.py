import tkinter as tk
import sys
import time
import threading

import navegador.navegador as navegador
from tkinter import messagebox
from controllers.main_view_controller import Controller

class Gui:
    def __init__(self, wallet):
        self.wallet = wallet
        
    def crea_ventana(self):
        ventana = tk.Tk()
        ventana.minsize(750, 500)
        self.vent=ventana

    def ventana_loop(self):
        self.vent.mainloop()

    def home_page(self):
        menu_principal = tk.Frame(self.vent)
        menu_principal.place(relheight=1,relwidth=1)
        controller_main = Controller(menu_principal, self.wallet)
        controller_main.home_view()
        
    def prueba(self):
        pagina= tk.Frame(self.vent)
        pagina.place(relheight=1,relwidth=1)
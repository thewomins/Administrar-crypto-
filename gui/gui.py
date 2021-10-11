import tkinter as tk
import sys
import time
import threading

from tkinter import messagebox
from gui.menu_agregar_dolar import Menu_agregar_dolar
from gui.menu_lateral import Menu_lateral
from gui.menu_principal import Menu_principal
from gui.menu_agregar_crypto import Menu_agregar_crypto
from controllers.main_view_controller import Controller
from controllers.add_dolar_controller import New_dolar
from controllers.menu_lat_controller import Lat_controller
from controllers.add_crypto_controller import New_crypto

class Gui:
    def __init__(self, wallet):
        self.wallet = wallet
        
    def crea_ventana(self):
        ventana = tk.Tk()
        ventana.minsize(750, 500)
        self.vent=ventana
    
    def actualizar_wallet(self):
        self.wallet.actualizar_datos()

    def mostrar_menu_lat(self):
        controller = Lat_controller()
        menu_lat = Menu_lateral(self.vent, controller)
        menu_lat.frame_menu_lateral().place(relheight=1, relwidth=0.32)

    def ventana_loop(self):
        self.vent.mainloop()

    def home_page(self):
        control_menu=Controller(self.wallet)
        self.mostrar_menu_lat()
        menu_principal = Menu_principal(self.vent, control_menu)
        view=menu_principal.menu()
        view.place(relx=0.32, relheight=1, relwidth=0.68)

    def menu_compra_dolar(self):
        control_menu=New_dolar(self.wallet)
        menu=Menu_agregar_dolar(self.vent, control_menu)
        self.mostrar_menu_lat()
        menu.interior().place(relx=0.32, relheight=1, relwidth=0.68)

    def menu_compra_crypto(self):
        control_menu=New_crypto(self.wallet)
        menu = Menu_agregar_crypto(self.vent, control_menu)
        self.mostrar_menu_lat()
        menu.interior().place(relx=0.32, relheight=1, relwidth=0.68)
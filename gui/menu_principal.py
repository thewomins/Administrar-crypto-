import tkinter as tk
from components.components import Components

class Menu_principal:
    def __init__(self, padre, controller):
        self.padre = padre
        self.controller=controller
        self.color_tarjetas='#263238'
        self.components = Components(self.padre)

    def menu(self):
        menu_principal = tk.Frame(self.padre, bg='#37474f')
        frame_interior = self.components.menu_frames(menu_principal, '#37474f')
        self.menu_arriba(frame_interior)
        self.menu_abajo(frame_interior)
        return menu_principal

    def menu_arriba(self, padre):
        frame_balance = tk.Frame(padre, bg= self.color_tarjetas)
        frame_balance.place(relheight=0.3, relwidth=1)
        components_balance = Components(frame_balance)
        components_balance.targeta_principal(self.color_tarjetas, self.controller.view_balance(), self.controller.view_ganado(), self.controller.view_depositado())   

    def menu_abajo(self, padre):
        #arreglar esta funcion para que solo lea las monedas disponibles
        frame_secundario = tk.Frame(padre, bg= '#37474f')
        frame_secundario.place(rely=0.32, relheight=0.7, relwidth=1)
        #editar
        if len(self.controller.view_monedas())<3:
            return
        if len( self.controller.view_monedas())>3:
            print("monedas > 3 editar esto!!!")
        #editar
        a=self.dolar_carta(frame_secundario,  self.controller.view_monedas()[0])
        a.grid(row=0, column=0, padx=5, pady=5, sticky=("N", "S", "E", "W"))
        x,y=0,1
        for i in range(2):
            a=self.crypto_frame(frame_secundario,  self.controller.view_monedas()[i+1])
            a.grid(row=x, column=y, padx=5, pady=5, sticky=("N", "S", "E", "W"))
            y=y+1
            if i == 0:
                y=0
                x=1
        b=self.components.tarjeta_vermas(frame_secundario, self.color_tarjetas)
        b.grid(row=1, column=1, padx=5, pady=5, sticky=("N", "S", "E", "W"))
        frame_secundario.columnconfigure((0,1), weight=1)
        #a=self.menu_abajo_interior(frame_interior_sec)
        #a=self.menu_abajo_interior(frame_interior_sec)
        #b=self.menu_abajo_interior(frame_interior_sec)
        #c=self.menu_abajo_interior(frame_interior_sec)
        #frame_interior_sec.columnconfigure((0,1), weight=1)
        #a.grid(row=0, column=0, padx=10, pady=10, sticky=("N", "S", "E", "W"))
        #b.grid(row=0, column=1, padx=10, pady=10,sticky=("N", "S", "E", "W"))
        #c.grid(row=1, column=0, padx=10, pady=10,sticky=("N", "S", "E", "W"))

    def crypto_frame(self, padre, monedas):
        components_secundario =  Components(padre)
        a=components_secundario.tarjeta_cryptos(self.color_tarjetas,monedas.nombre,monedas.total,round(monedas.total-monedas.depositado,2),monedas.depositado)
        return a

    def dolar_carta(self, padre, monedas):
        components_secundario =  Components(padre)
        a=components_secundario.tarjeta_dolar(self.color_tarjetas,monedas.nombre,monedas.total,round(monedas.retirado-monedas.invertido,2),monedas.invertido)
        return a
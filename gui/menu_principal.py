import tkinter as tk
from components.components import Components

class Menu_principal:
    def __init__(self,padre):
        self.padre = padre
        self.color_tarjetas='#263238'
        self.components = Components(self.padre)

    def menu(self, balance, ganado, depositado, monedas):
        menu_principal = tk.Frame(self.padre, bg='#37474f')
        frame_interior = self.components.menu_frames(menu_principal, '#37474f')
        self.menu_arriba(frame_interior, balance, ganado, depositado)
        self.menu_abajo(frame_interior, monedas)
        return menu_principal


    def menu_arriba(self, padre, balance, ganado, depositado):
        frame_balance = tk.Frame(padre, bg= self.color_tarjetas)
        frame_balance.place(relheight=0.3, relwidth=1)
        components_balance = Components(frame_balance)
        components_balance.targeta_principal(self.color_tarjetas, balance, ganado, depositado)   

    def menu_abajo(self, padre, monedas):
        frame_secundario = tk.Frame(padre, bg= '#37474f')
        frame_secundario.place(rely=0.32, relheight=0.7, relwidth=1)
        
        if len(monedas)>3:
            print("a")
        
        x,y=0,0
        for i in range(3):
            a=self.menu_abajo_interior(frame_secundario, monedas[i])
            a.grid(row=x, column=y, padx=5, pady=5, sticky=("N", "S", "E", "W"))
            y=y+1
            if i == 1:
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

    def menu_abajo_interior(self, padre, monedas):
        components_secundario =  Components(padre)
        a=components_secundario.tarjeta_cryptos(self.color_tarjetas,monedas.nombre,monedas.total,round(monedas.total-monedas.depositado,2),monedas.depositado)
        return a

    
    
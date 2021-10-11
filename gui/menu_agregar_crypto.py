import tkinter as tk
from components.components import Components

class Menu_agregar_crypto:
    def __init__(self, padre, controller):
        self.controller = controller
        self.padre = padre
        self.color_tarjetas='#263238'
        self.components = Components(self.padre)

    def menu(self):
        menu_principal = tk.Frame(self.padre, bg='#37474f')
        return menu_principal
    
    def interior(self):
        menu=self.menu()
        frame_interior = self.components.menu_frames(menu, '#37474f')
        a,b=self.show_formulario(frame_interior, '#263238')
        a.place(relwidth=1, relheight=0.33)

        frame_boton=tk.Frame(frame_interior,bg='#37474f')
        frame_boton.place(relheight=0.1, rely=0.37, relwidth=1)

        var1=tk.IntVar()
        check=tk.Checkbutton(frame_boton, text="Venta", variable=var1, bg="#37474f", activebackground="#37474f", foreground="#fff",selectcolor="#37474f")
        check.place(relx=0.1,relheight=1,relwidth=0.2)

        e=self.boton_lateral(frame_boton,"#263238","Agregar")
        e.bind("<Button-1>",lambda _: self.controller.boton_press(b,var1))
        e.place(relx=0.6, relheight=1,relwidth=0.4) 

        return menu

    def show_formulario(self, padre, color):
        contenedor_texto = tk.Frame(padre,bg=color)
        contenedor_texto.columnconfigure(0, weight=1)
        contenedor_texto.columnconfigure(1, weight=1)
        a=self.components.text(contenedor_texto, "Cuenta origen", color, 14)
        aa=self.components.entry_txt(contenedor_texto)
        a.grid(row=0, column=0, padx=10, pady=5, sticky=("w"))
        aa.grid(row=1, column=0, padx=15, pady=5, sticky=("w"))
        b=self.components.text(contenedor_texto, "Cuenta destino", color, 14)
        bb=self.components.entry_txt(contenedor_texto)
        b.grid(row=0, column=1, padx=10, pady=5, sticky=("w"))
        bb.grid(row=1, column=1, padx=15, pady=5, sticky=("w"))
        c=self.components.text(contenedor_texto, "Cantidad comprada", color, 14)
        cc=self.components.entry_txt(contenedor_texto)
        c.grid(row=2, column=0, padx=10, pady=5, sticky=("w"))
        cc.grid(row=3, column=0, padx=15, pady=5, sticky=("w"))
        d=self.components.text(contenedor_texto, "Precio compra", color, 14)
        dd=self.components.entry_txt(contenedor_texto)
        d.grid(row=2, column=1, padx=10, pady=5, sticky=("w"))
        dd.grid(row=3, column=1, padx=15, pady=5, sticky=("w"))

        datos=aa,bb,cc,dd
        return contenedor_texto , datos

    def boton_lateral(self, padre, color,texto):
        frame_izquierda = tk.Frame(padre, bg= color)
        frame_izquierda.focus_set()
        self.components.text_titulos_padre(frame_izquierda, texto, color).place(anchor="center", relx=0.5, rely=0.5)
        return frame_izquierda


import tkinter as tk

class Components:
    def __init__(self,padre):
        self.padre = padre

    def text_titulos(self, texto2, color):
        textol = tk.Label(self.padre, text= texto2, bg=color, fg='white', font=("google sans medium", 18))    
        return textol

    def text_secundario(self, texto2, color):
        texto = tk.Label(self.padre, text= texto2, bg=color, fg='white', font=("google sans medium", 14))    
        return texto

    def text_titulos_padre(self, padre, texto2, color):
        textol = tk.Label(padre, text= texto2, bg=color, fg='white', font=("google sans medium", 18))    
        return textol

    def text_secundario_padre(self, padre, texto2, color):
        texto = tk.Label(padre, text= texto2, bg=color, fg='white', font=("google sans medium", 14))    
        return texto

    def boton(self, texto):
        boton = tk.Button(self.padre, text=texto)
        return boton

    def menu_frames(self, padre, color):
        frame2 = tk.Frame(padre, bg=color)
        frame2.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
        return frame2
    
    def targeta_principal(self, color, balance, ganado, depositado):
        frame_izquierda = tk.Frame(self.padre, bg= color, pady=30, padx=30)
        frame_izquierda.place(relwidth=0.6)
        self.text_titulos_padre(frame_izquierda, "Balance", color).grid(row=0)
        self.text_titulos_padre(frame_izquierda, balance, color).grid(row=1, sticky='w')

        frame_derecha = tk.Frame(self.padre, bg= color, pady=10)
        frame_derecha.place(relwidth=0.4, relx=0.6)
        self.text_secundario_padre(frame_derecha, "Ganado", color).grid(row=0, sticky='w')
        self.text_secundario_padre(frame_derecha, ganado, color).grid(row=1, sticky='w')
        self.text_secundario_padre(frame_derecha, "Depositado", color).grid(row=2, sticky='w')
        self.text_secundario_padre(frame_derecha, depositado, color).grid(row=3, sticky='w')

    def tarjeta_cryptos(self, color, nombre, balance, ganado, depositado):
        frame_izquierda = tk.Frame(self.padre, bg= color, pady=5)
        frame_izquierda.columnconfigure((0,1), weight=1)
        self.text_titulos_padre(frame_izquierda, nombre, color).grid(row=0, columnspan=2)
        self.text_titulos_padre(frame_izquierda, balance, color).grid(row=1, columnspan=2)
        self.text_secundario_padre(frame_izquierda, "Ganado", color).grid(ipadx = 10,row=2,sticky='w')
        self.text_secundario_padre(frame_izquierda, ganado, color).grid(row=2, column=1, sticky='w')
        self.text_secundario_padre(frame_izquierda, "Depositado", color).grid(ipadx = 10, row=3, sticky='w')
        self.text_secundario_padre(frame_izquierda, depositado, color).grid(row=3, column=1, sticky='w')
        return frame_izquierda

    def tarjeta_vermas(self, padre, color):
        frame_izquierda = tk.Frame(padre, bg= color, pady=5)
        self.text_titulos_padre(frame_izquierda, "ver mas", color).place(anchor="center", relx=0.5, rely=0.4)
        return frame_izquierda

    def a(self):
        print('s')

    def entry_txt(self, padre):
        entry = tk.Entry(padre)
        return entry

    def text(self, padre, texto2, color, tamano):
        textol = tk.Label(padre, text= texto2, bg=color, fg='white', font=("google sans medium", tamano))    
        return textol

    def tarjeta_dolar(self, color, nombre, cantidad, ganado, invertido):
        frame_izquierda = tk.Frame(self.padre, bg= color, pady=5)
        frame_izquierda.columnconfigure((0,1), weight=1)
        self.text_titulos_padre(frame_izquierda, nombre, color).grid(row=0, columnspan=2)
        self.text_titulos_padre(frame_izquierda, cantidad, color).grid(row=1, columnspan=2)
        self.text_secundario_padre(frame_izquierda, "Ganado", color).grid(ipadx = 10,row=2,sticky='w')
        self.text_secundario_padre(frame_izquierda, ganado, color).grid(row=2, column=1, sticky='w')
        self.text_secundario_padre(frame_izquierda, "Invertido", color).grid(ipadx = 10, row=3, sticky='w')
        self.text_secundario_padre(frame_izquierda, invertido, color).grid(row=3, column=1, sticky='w')
        return frame_izquierda
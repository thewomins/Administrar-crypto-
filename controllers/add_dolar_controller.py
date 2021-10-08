
from tkinter.constants import NONE
import archivo

class New_dolar:
    def __init__(self, Wallet):
        self.wallet = Wallet

    def boton_press(self, datos):
        #datos= cuenta origen, cantidad comprada, cantidad en clp 
        for a in datos:
            if not a.get():
                print("Faltan datos")
                return
        try:
            b=datos[0].get().upper(), 'USD', (int)(datos[1].get()), (int)(datos[2].get())
        except:
            print("Datos incorrectos ingrese nuevamente")
            return
        print(b)
        self.wallet.add_compra_usd(b)
        self.wallet.crea_crypto()
        self.wallet.calculo_depositado()
        archivo.guardar_json(self.wallet.transacciones, 'data.json')
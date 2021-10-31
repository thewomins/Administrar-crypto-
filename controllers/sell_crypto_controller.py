import archivo

class Sell_crypto:
    def __init__(self, Wallet):
        self.wallet = Wallet

    def boton_press(self, datos):
        #datos= cuenta origen (crypto), cuenta destino (usd), cantidad vendiad, precio de venta
        print(datos[0].get(), datos[1].get(), datos[2].get(), datos[3].get())
        for a in datos:
            if not a.get():
                print("Faltan datos")
                return
        try:
            b=datos[0].get().upper(), datos[1].get().upper(), float(datos[2].get()), float(datos[3].get())
        except:
            print("Datos incorrectos ingrese nuevamente")
            return
        print(b)
        self.wallet.add_venta(b)
        self.wallet.crea_crypto()
        self.wallet.calculo_depositado()
        archivo.guardar_json(self.wallet.transacciones, 'data.json')
        
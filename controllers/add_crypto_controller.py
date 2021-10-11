import archivo

class New_crypto:
    def __init__(self, Wallet):
        self.wallet = Wallet

    def boton_press(self, datos, check):
        #datos= cuenta origen, cuenta destino, cantidad comprada, precio crypto
        print(datos[0].get(), datos[1].get(), datos[2].get(), datos[3].get(), check.get())
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
        if(check.get()==0):
            self.wallet.add_compra(b)
        else:
            self.wallet.add_venta(b)
        self.wallet.crea_crypto()
        self.wallet.calculo_depositado()
        archivo.guardar_json(self.wallet.transacciones, 'data.json')
        
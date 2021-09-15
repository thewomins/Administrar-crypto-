import requests

class Crypto:
    def __init__(self, nombre, acronimo, transacciones):
        self.nombre = nombre
        self.acronimo = acronimo
        self.cantidad = 0
        self.depositado = 0
        self.total = 0
        self.lista_transacciones = transacciones      

    def precio_actual(self):
        url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(self.acronimo.upper(), 'USD')
        r = requests.get(url)
        data = r.json()
        precio_actual = data['USD']
        return precio_actual

    def calcula_precio(self, cantidad_comprada, precio):
        usd = cantidad_comprada*precio
        return usd

    def calculo_depositado(self):
        for key in self.lista_transacciones:
            valor = self.calcula_precio(key['cantidad comprada'],key['precio crypto'])
            if key["estado"]==1:
                self.cantidad = self.cantidad + key["cantidad comprada"]
                self.depositado = self.depositado + valor
            else:
                self.cantidad = self.cantidad - key["cantidad comprada"]
        self.depositado = round(self.depositado, 2)
        return self.depositado 

    def calculo_total(self):      
        self.total = round(self.calcula_precio(self.cantidad, self.precio_actual()),2)
        #print("b "+str(self.depositado)+" "+str(self.precio_actual())+" "+str(self.total))  
        return self.total
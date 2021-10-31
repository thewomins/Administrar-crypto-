import requests

class Crypto:
    def __init__(self, nombre, acronimo, transacciones):
        self.nombre = nombre
        self.acronimo = acronimo
        self.if_dolar()
        self.cantidad = 0
        self.depositado = 0
        self.total = 0
        self.lista_transacciones = transacciones   

    def if_dolar(self):
        if self.acronimo=="USD":
            self.invertido=0
            self.retirado=0   

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

    def calculo_compra(self):
        cantidad=0
        invertido=0
        if self.acronimo == 'USD':    
            for key in self.lista_transacciones['compras']:
                if key["cuenta origen"] == "CLP":
                    invertido=invertido+key['cantidad comprada']
                else:
                    cantidad= cantidad+key['cantidad comprada']
            cantidad=cantidad+invertido
            self.invertido=invertido
        else:
            for key in self.lista_transacciones['compras']:
                cantidad= cantidad+self.calcula_precio(key['cantidad comprada'], key['precio crypto'])
                self.cantidad=self.cantidad+key['cantidad comprada']
        return cantidad

    def calculo_ventas(self):
        cantidad=0
        retirado=0
        if self.acronimo == 'USD':
            for key in self.lista_transacciones['ventas']:
                if key["cuenta destino"] == "CLP":
                    retirado=retirado+key['cantidad vendida']
                else:
                    cantidad= cantidad+key['cantidad vendida']
            cantidad=cantidad+retirado
            self.retirado=retirado
        else:
            for key in self.lista_transacciones['ventas']:
                cantidad= cantidad+self.calcula_precio(key['cantidad vendida'], key['precio crypto'])
                self.cantidad=self.cantidad-key['cantidad vendida']
        return cantidad

    def calculo_depositado(self):
        self.depositado= self.calculo_compra()-self.calculo_ventas()
        self.depositado = round(self.depositado, 2)
        if(self.depositado<=0):
            self.depositado=0
        return self.depositado 

    def calculo_total(self):      
        if self.acronimo == 'USD':
            self.total=self.depositado
        else:
            self.total = round(self.calcula_precio(self.cantidad, self.precio_actual()),2) 
        return self.total

    def actualizar_crypto(self):
        self.depositado = 0
        self.total = 0 
        self.cantidad = 0

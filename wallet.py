from crypto import Crypto
import components.diccionario_monedas as monedas

class Wallet:
    def __init__(self):
        self.transacciones = {}
        self.list_monedas = []
        self.balance=0
        self.depositado=0
        self.ganado=0

    def add_compra_usd(self, dato):
        if dato[1] in self.transacciones :
            self.transacciones[dato[1]]['compras'].append({
            'cuenta origen' : dato[0].upper(),
            'cuenta destino' : dato[1].upper(),
            'cantidad comprada' : dato[2],
            'cantidad gastada clp' : dato[3],
            }) 
        else:
            self.transacciones[dato[1]]={}
            self.transacciones[dato[1]]['compras']=[]
            self.transacciones[dato[1]]['ventas']=[]
            self.add_compra_usd(dato)

    def add_venta_usd(self, dato):
        self.transacciones[dato[1]]['ventas'].append({
            'cuenta origen' : dato[0].upper(),
            'cuenta destino': dato[1].upper(),
            'cantidad vendida' : dato[2],
            }) 

    def add_compra(self, dato):
        if dato[1] in self.transacciones:
            self.add_venta_usd([dato[1],dato[0],dato[2]*dato[3],0])
            self.transacciones[dato[1]]['compras'].append({
            'cuenta origen' : dato[0].upper(),
            'cuenta destino' : dato[1].upper(),
            'cantidad comprada' : dato[2],
            'precio crypto' :  dato[3]
            }) 
        else:
            self.transacciones[dato[1]]={}
            self.transacciones[dato[1]]['compras']=[]
            self.transacciones[dato[1]]['ventas']=[]
            self.add_compra(dato)       

    def add_venta(self, dato):
        self.add_compra_usd([dato[0],dato[1],dato[2]*dato[3],0,0])
        self.transacciones[dato[0]]['ventas'].append({
        'cuenta origen' : dato[0].upper(),
        'cuenta destino' : dato[1].upper(),
        'cantidad vendida' : dato[2],
        'precio crypto' :  dato[3],
        }) 

    def crea_crypto(self):#crea monedas con sus transacciones
        if self.list_monedas:#si ya existe la lista
            for b in self.list_monedas:
                b.lista_transacciones = self.transacciones[b.acronimo]
        else:
            for a in self.transacciones:
                crypto = Crypto(monedas.crypto[a],a,self.transacciones[a])
                self.list_monedas.append(crypto)
        return self.list_monedas
        
    def calculo_depositado(self):# 
        for i in self.list_monedas:
            i.calculo_depositado()
            i.calculo_total()
            self.depositado= self.depositado+i.depositado
            self.balance = self.balance+i.total
        self.balance = round(self.balance, 2)
        self.depositado = round(self.depositado, 2)
        self.ganado = round(self.balance-self.depositado,2)

    def actualizar_datos(self):
        self.depositado = 0
        self.balance = 0
        self.ganado = 0
        for i in self.list_monedas:
            i.actualizar_crypto()
            i.calculo_depositado()
            i.calculo_total()
            self.depositado= self.depositado+i.depositado
            self.balance = self.balance+i.total
        self.balance = round(self.balance, 2)
        self.depositado = round(self.depositado, 2)
        self.ganado = round(self.balance-self.depositado,2)
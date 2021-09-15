from crypto import Crypto
import components.diccionario_monedas as monedas

class Wallet:
    def __init__(self, lista_transacciones):
        self.transacciones = lista_transacciones  
        self.transacciones_ordenadas = {}
        self.list_monedas = []
        self.balance=0
        self.depositado=0
        self.ganado=0

    def add_compra(self, dato):
        self.transacciones['operaciones'].append({
            'nombre crypto' : dato[0].upper(),
            'cantidad comprada' : dato[1],
            'precio crypto' :  dato[2],
            'cantidad gastada clp' : dato[3],
            'estado' : 1,
            'revisado' : dato[4]
        })   

    def add_venta(self, dato):
        self.transacciones['operaciones'].append({
            'nombre crypto' : dato[0].upper(),
            'nombre moneda' : dato[1].upper(),
            'cantidad comprada' : dato[2],
            'precio crypto' :  dato[3],
            'cantidad gastada clp' : dato[4],
            'estado' : 0,
            'revisado' : dato[5]
        }) 

    def busca_trans_id(self,id): #busca transaccion por posicion y devuelve la transaccion
        usd = self.transacciones['operaciones'][id]['cantidad comprada']*\
                self.transacciones['operaciones'][id]['precio crypto']
        return self.transacciones['operaciones'][id]

    def separa_por_crypto(self):#ordena las crypto
        for key in self.transacciones['operaciones']:
            if(key['revisado']==0):
                key['revisado']=1
                aux=self.transacciones_ordenadas.get(key.get('nombre crypto'))
                if(aux):
                    self.transacciones_ordenadas[key.get('nombre crypto')].append(key)
                else:
                    self.transacciones_ordenadas[key.get('nombre crypto')]=[]
                    self.transacciones_ordenadas[key.get('nombre crypto')].append(key)
        return self.transacciones_ordenadas

    def crea_crypto(self):#crea monedas con sus transacciones
        if self.list_monedas:#si ya existe la lista
            for b in self.list_monedas:
                b.lista_transacciones = self.transacciones_ordenadas[b.acronimo]#actualiza las transacciones de la crypto
        else:
            for a in self.transacciones_ordenadas:
                crypto = Crypto(monedas.crypto[a],a,self.transacciones_ordenadas[a])
                self.list_monedas.append(crypto)
        return self.list_monedas
        
    def calculo_depositado(self):# 
        for i in self.list_monedas:
            depositado = i.calculo_depositado()
            total = i.calculo_total()
            self.depositado = self.depositado + depositado
            self.balance = self.balance + total 
        self.balance = round(self.balance, 2)
        self.depositado = round(self.depositado, 2)
        #self.ganado = round(self.balance-self.depositado,2)


    #def cantidad_de_crypto():#devuelve la cantidad de cryptos

import requests
import json
import time
import threading
from crypto import Crypto
import archivo 
from wallet import Wallet
import navegador.navegador as navegador
from gui.gui import Gui

if __name__ == "__main__": 
    dic={}
    dic['operaciones']=[]
    wallet=Wallet(dic)
    
    dato= "doge",39.9,0.6711,20000,0
    dato1= "btc",0.000476,56551.36,20000,0
    dato2= "btc",0.000546,49000,20000,0
    dato3= "eth",0.09306,2769.93,200000,0
    dato4= "eth",0.10637,2485.32,200000,0
    dato5= "eth","usd",0.1813,3353.76,0,0
    dato6= "eth",0.1812,3350.69,0,0
    dato7= "eth",0.1812,3350.69,0,0
    wallet.add_compra(dato)
    wallet.add_compra(dato1)
    wallet.add_compra(dato2)
    wallet.add_compra(dato3)
    wallet.add_compra(dato4)
    wallet.add_venta(dato5)
    wallet.add_compra(dato6)
    wallet.transacciones_ordenadas=wallet.separa_por_crypto()
    wallet.crea_crypto()
    
    archivo.guardar_json(wallet.transacciones, 'data.json')
    data = archivo.leer_json('data.json')

    dic_currency = wallet.transacciones
    
    def timer():
        for i in range(10):
            print("a")
            wallet.calculo_depositado()
            time.sleep(30)
    #hilo = threading.Thread(target=timer)
    #hilo.start()
    wallet.calculo_depositado()
    print(wallet.depositado)
    print(wallet.balance)
    print(wallet.ganado)
    
    #hilo = threading.Thread(target=timer)
    #hilo.start()

    a=Gui(wallet)   
    navegador.setGui(a)
    #navegador.iniciar_homepage()
    exit;
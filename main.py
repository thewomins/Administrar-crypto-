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
    wallet=Wallet()
    
    #dato "cuenta origen", "cuenta destino, catidad crypto, precio crypto, cantidad gastada clp, estado"
    #dato= "USD" , "DOGE", 39.9, 0.6711, 20000
    #dato1= "USD", "BTC", 0.000476 , 56551.36, 20000
    #dato2= "USD", "BTC", 0.000546 , 49000, 20000
    #dato3= "USD", "ETH", 0.09306, 2769.93, 200000
    #dato4= "USD", "ETH", 0.10637, 2485.32, 200000
    #dato5= "ETH", "USD", 0.1813, 3353.76
    #dato6= "USD", "ETH", 0.1812, 3350.69, 0 
    #dato7= "CLP", "USD", 602, 460000
    #dato8= "BTC", "USD", 0.00101, 54587.45 #comision 0.05513332
    #wallet.add_compra_usd(dato7)
    #wallet.add_compra(dato1)
    #wallet.add_compra(dato2)
    #wallet.add_compra(dato3)
    #wallet.add_compra(dato4)
    #wallet.add_venta(dato5)
    #wallet.add_venta(dato8)
    #wallet.add_compra(dato6)
    #wallet.add_compra(dato)
    
    
    #archivo.guardar_json(wallet.transacciones, 'data.json')
    data = archivo.leer_json('data.json')
    wallet.transacciones=data
    wallet.crea_crypto()
    dic_currency = wallet.transacciones
    
    #def timer():
    #    for i in range(10):
    #        print("a")
    #        wallet.calculo_depositado()
    #        time.sleep(30)
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
#singleton, herencia o modulo

def setGui(Gui):
    global gui
    gui= Gui
    gui.crea_ventana()
    iniciar_homepage()
    gui.ventana_loop()

def iniciar_homepage():
    gui.home_page()

def notify(param):
    print(param)
    if(param == 'Agregar compra dolares'):
        iniciar_menu_compra_dolar()
    elif(param == 'Agregar transaccion crypto'):
        iniciar_menu_compra_crypto()
    elif(param == 'Volver'):
        iniciar_homepage()
        gui.actualizar_wallet()


def iniciar_menu_compra_dolar():
    gui.menu_compra_dolar()

def iniciar_menu_compra_crypto():
    gui.menu_compra_crypto()
#singleton, herencia o modulo

def setGui(Gui):
    global gui
    gui= Gui
    gui.crea_ventana()
    iniciar_homepage()
    gui.ventana_loop()

def iniciar_homepage():
    gui.home_page()

def notify():
    iniciar_otra()
    print("a")

def iniciar_otra():
    gui.prueba()
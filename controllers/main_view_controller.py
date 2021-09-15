from gui.menu_lateral import Menu_lateral
from gui.menu_principal import Menu_principal

class Controller:
    def __init__(self, vista, Wallet):
        self.wallet = Wallet
        self.vista = vista

    def home_view(self):
        self.mostrar_menu_lateral()
        self.mostrar_menu_balances()

    def mostrar_menu_lateral(self):
        a = Menu_lateral(self.vista)
        a.frame_menu_lateral().place(relheight=1, relwidth=0.32)

    def mostrar_menu_balances(self):
        a = Menu_principal(self.vista)
        a.menu(self.wallet.balance,
                self.wallet.ganado,
                self.wallet.depositado,
                self.wallet.list_monedas).place(relx=0.32, relheight=1, relwidth=0.68)

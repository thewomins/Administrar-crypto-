

class Controller:
    def __init__(self, wallet):
        self.wallet= wallet
    
    def view_balance(self):
        return self.wallet.balance
    
    def view_ganado(self):
        return self.wallet.ganado

    def view_depositado(self):
        return self.wallet.depositado

    def view_monedas(self):
        return self.wallet.list_monedas
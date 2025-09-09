from Prodotto import Prodotto

class Magazzino():
    
    def __init__(self, inventario: list[Prodotto]):
        self.inventario = inventario
        
    def getInventario(self):
        return self.inventario
    
    def aggiungiProdotto(self, prodottoDaAggiungere: Prodotto):
        self.inventario.append(prodottoDaAggiungere)
    
    def rimuoviProdotto(self, prodottoDaRimuovere: Prodotto):
        self.inventario.remove(prodottoDaRimuovere)
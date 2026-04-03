from Model.Magazzino.Magazzino import Magazzino, Prodotto, StatoProdotto
from Model.Dati import Dati

class GestoreMagazzino:
    
    def __init__(self, magazzino: Magazzino, dati: Dati ):
        self.magazzino = magazzino
        self.dati = dati
        
    def creaNuovoProdotto(self, nome, quantita, prezzo, costo, fornitore, avvisi, soglia):
        nuovoProdotto = Prodotto(nome, quantita, prezzo, costo, fornitore, avvisi, soglia)
        self.magazzino.aggiungiProdotto(nuovoProdotto)
        self.dati.setDirty()
        
    def modificaDettagliProdotto(self, prodotto: Prodotto, **kwargs):
        p = self.cercaProdotto(prodotto)
        
        if p is None:
            return False
        
        for attr, valore in kwargs.items():
            if not hasattr(p, attr):
                return False
            setattr(p, attr, valore)
        self.dati.setDirty()
        return True
          
    def cercaProdotto(self, prodotto: Prodotto):
        for p in self.magazzino.getInventario():
            if p.nome == prodotto.getNomeProdotto():
                return p
        return None
    
    def modificaStatoProdotto(self, prodotto: Prodotto, statoProdotto: StatoProdotto):
        prodotto.setStatoProdotto(statoProdotto)
        self.dati.setDirty()
        
    def eliminaProdotto(self, nomeProdotto: str):
        inventario = self.magazzino.getInventario()
        for prodotto in inventario:
            if nomeProdotto == prodotto.getNomeProdotto():
                inventario.remove(prodotto)
                self.dati.setDirty()
                return True
        return False

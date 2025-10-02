    
from Implementazione.Model.Magazzino import Magazzino, Prodotto, StatoProdotto

class GestoreMagazzino:
    @staticmethod
    def creaNuovoProdotto(magazzino: Magazzino, nome, quantita, prezzo, costo, fornitore, avvisi, soglia):
        nuovoProdotto = Prodotto(nome, quantita, prezzo, costo, fornitore, avvisi, soglia)
        magazzino.aggiungiProdotto(nuovoProdotto)
    
    @staticmethod
    def modificaStatoProdotto(prodotto: Prodotto, statoProdotto: StatoProdotto):
        prodotto.setStatoProdotto(statoProdotto)
        
    @staticmethod
    def eliminaProdotto(nomeProdotto: str, magazzino: Magazzino):
        inventario = magazzino.getInventario()
        for prodotto in magazzino.inventario:
            if nomeProdotto == prodotto.getNome():
                inventario.remove(prodotto)
                return True
        return False
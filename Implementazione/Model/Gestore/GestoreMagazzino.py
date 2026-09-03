from Model.Magazzino import Magazzino, Prodotto, StatoProdotto

class GestoreMagazzino:
    @staticmethod
    def creaNuovoProdotto(magazzino: Magazzino, nome: str, quantita: int, prezzo: float, costo: float, fornitore: str, avvisi: bool, soglia: int):
        nuovoProdotto = Prodotto(nome, quantita, prezzo, costo, fornitore, avvisi, soglia)
        magazzino.aggiungiProdotto(nuovoProdotto)
        
    @staticmethod
    def modificaDettagliProdotto(prodotto: Prodotto, **kwargs):
        if prodotto is None:
            return False
        
        for attr, valore_attr in kwargs.items():
            if hasattr(prodotto, attr):
                setattr(prodotto, attr, valore_attr)
                
            else:
                print("Attributo non esistente")
                return False
        return True
    
    @staticmethod
    def modificaStatoProdotto(prodotto: Prodotto, statoProdotto: StatoProdotto):
        if prodotto is not None:
            prodotto.setStatoProdotto(statoProdotto)
            return True
        return False
    
    @staticmethod
    def eliminaProdotto(magazzino: Magazzino, prodotto: Prodotto):
        if prodotto in magazzino.getInventario():
            magazzino.getInventario().remove(prodotto)
            return True

        return False
from Model.Dati import Dati
from Model.Magazzino import Prodotto, StatoProdotto

class GestoreMagazzino:
    def __init__(self, dati: Dati):
        self.dati = dati

    def creaNuovoProdotto(self, nome: str, quantita: int, prezzo: float, costo: float, fornitore: str, avvisi: bool, soglia: int) -> Prodotto:
        nuovoProdotto = Prodotto(nome, quantita, prezzo, costo, fornitore, avvisi, soglia)
        self.dati.prodotti.append(nuovoProdotto)
        return nuovoProdotto
        
    def modificaDettagliProdotto(self, prodotto: Prodotto, **kwargs) -> bool:
        if prodotto is None:
            return False
        
        for attr, valore_attr in kwargs.items():
            if hasattr(prodotto, attr):
                setattr(prodotto, attr, valore_attr)
            else:
                print("Attributo non esistente")
                return False
        return True
    
    def modificaStatoProdotto(self, prodotto: Prodotto, statoProdotto: StatoProdotto) -> bool:
        if prodotto is not None:
            prodotto.setStatoProdotto(statoProdotto)
            return True
        return False
    
    def eliminaProdotto(self, prodotto: Prodotto) -> bool:
        if prodotto in self.dati.prodotti:
            self.dati.prodotti.remove(prodotto)
            return True
        return False
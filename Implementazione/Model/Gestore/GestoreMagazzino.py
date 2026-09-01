from Model.Magazzino import Magazzino, Prodotto, StatoProdotto

class GestoreMagazzino:
    @staticmethod
    def creaNuovoProdotto(magazzino: Magazzino, nome: str, quantita: int, prezzo: float, costo: float, fornitore: str, avvisi: bool, soglia: int):
        nuovoProdotto = Prodotto(nome, quantita, prezzo, costo, fornitore, avvisi, soglia)
        magazzino.aggiungiProdotto(nuovoProdotto)
        
    @staticmethod
    def modificaDettagliProdotto(magazzino: Magazzino, nomeProdotto: str, **kwargs):
        p = GestoreMagazzino.cercaProdotto(magazzino, nomeProdotto)
        
        if p is None:
            return False
        
        for attr, valore_attr in kwargs:
            if hasattr(p, attr):
                setattr(p, attr, valore_attr)
                return True
            else:
                print("Attributo non esistente")
                return False
    
    @staticmethod
    def cercaProdotto(magazzino: Magazzino, nomeProdotto: str):
        for p in magazzino.inventario:
            if p.getNome() == nomeProdotto:
                return p
        return None
    
    @staticmethod
    def modificaStatoProdotto(magazzino: Magazzino, nomeProdotto: str, statoProdotto: StatoProdotto):
        prodotto = GestoreMagazzino.cercaProdotto(magazzino, nomeProdotto)
        prodotto.setStatoProdotto(statoProdotto)
        
    @staticmethod
    def eliminaProdotto(magazzino: Magazzino, nomeProdotto: str):
        inventario = magazzino.getInventario()
        for prodotto in inventario:
            if nomeProdotto == prodotto.getNome():
                inventario.remove(prodotto)
                return True
        return False

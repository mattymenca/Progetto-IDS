from Model.Magazzino import Magazzino, Prodotto, StatoProdotto

class GestoreMagazzino:
    @staticmethod
    def creaNuovoProdotto(magazzino: Magazzino, nome, quantita, prezzo, costo, fornitore, avvisi, soglia):
        nuovoProdotto = Prodotto(nome, quantita, prezzo, costo, fornitore, avvisi, soglia)
        magazzino.aggiungiProdotto(nuovoProdotto)
        
    @staticmethod
    def modificaDettagliProdotto(prodotto: Prodotto, **kwargs):
        p = GestoreMagazzino.cercaProdotto(prodotto)
        
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
    def cercaProdotto(magazzino: Magazzino, prodotto: Prodotto):
        for p in magazzino.inventario:
            if p.nome == prodotto.nome:
                return p
        return None
    
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

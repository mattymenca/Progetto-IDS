from StatoProdotto import StatoProdotto

class Prodotto:
    
    def __init__(self, nome, quantita, prezzo, costo, fornitore, avvisi, soglia, statoProdotto: StatoProdotto):
        self.nome = nome
        self.quantita = quantita
        self.prezzo = prezzo
        self.costo = costo
        self.fornitore = fornitore
        self.avvisi = avvisi
        self.soglia = soglia
        self.statoProdotto = statoProdotto
        
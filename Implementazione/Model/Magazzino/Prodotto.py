from .StatoProdotto import StatoProdotto

class Prodotto:
    
    def __init__(self, nome: str, quantita: int, prezzo: float, costo: float, fornitore: str, avvisi: bool, soglia: int):
        self.nome = nome
        self.quantita = quantita
        self.prezzo = prezzo
        self.costo = costo
        self.fornitore = fornitore
        self.avvisi = avvisi
        self.soglia = soglia
        self.statoProdotto = StatoProdotto.RIFORNITO
        
        self.aggiornaStatoProdotto()

    def aggiornaStatoProdotto(self):
        if self.quantita == 0:
            self.statoProdotto = StatoProdotto.ESAURITO
        elif self.quantita <= self.soglia:
            self.statoProdotto = StatoProdotto.QUASI_FINITO
        else:
            self.statoProdotto = StatoProdotto.RIFORNITO
        
    def getNomeProdotto(self):
        return self.nome

    def getQuantita(self):
        return self.quantita
    
    def getPrezzo(self):
        return self.prezzo
    
    def getCosto(self):
        return self.costo
    
    def getFornitore(self):
        return self.fornitore
    
    def getAvvisi(self):
        return self.avvisi
    
    def getSoglia(self):
        return self.soglia
    
    def getStatoProdotto(self):
        return self.statoProdotto
    
    def setNomeProdotto(self, nome: str):
        self.nome = nome

    def setPrezzo(self, prezzo: float):
        self.prezzo = prezzo

    def setCosto(self, costo: float):
        self.costo = costo

    def setQuantita(self, quantita: int):
        self.quantita = quantita
        self.aggiornaStatoProdotto()

    def setFornitore(self, fornitore: str):
        self.fornitore = fornitore

    def setSoglia(self, soglia: int):
        self.soglia = soglia
        self.aggiornaStatoProdotto()

    def setAvvisi(self, avvisi: bool):
        self.avvisi = avvisi

    def setStatoProdotto(self, statoProdotto: StatoProdotto):
        self.statoProdotto = statoProdotto
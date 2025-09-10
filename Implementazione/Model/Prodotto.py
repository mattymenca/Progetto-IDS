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
        
    def getNome(self):
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
    
    def setNome(self, nome: str):
        self.nome = nome

    def setPrezzo(self, prezzo: float):
        self.prezzo = prezzo

    def setCosto(self, costo: float):
        self.costo = costo

    def modificaQuantita(self, quantita: int):
        self.quantita = quantita

    def modificaFornitore(self, fornitore: str):
        self.fornitore = fornitore

    def setSoglia(self, soglia: int):
        self.soglia = soglia

    def modificaAvvisi(self, avvisi:bool):
        self.avvisi = avvisi

    def modificaStatoProdotto(self, statoProdotto:StatoProdotto):
        self.statoProdotto = statoProdotto
    


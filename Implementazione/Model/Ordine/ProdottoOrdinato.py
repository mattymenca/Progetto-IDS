class ProdottoOrdinato:

    def __init__(self, nome, prezzo, quantitaOrdinata):
        self.nome = nome
        self.prezzo = prezzo
        self.quantitaOrdinata = quantitaOrdinata
        
    def getNome(self):
        return self.nome
    
    def getPrezzo(self):
        return self.prezzo

    def getQuantita(self):
        return self.quantitaOrdinata
    
    def setPrezzo(self, prezzo):
        self.prezzo = prezzo

    def setQuantita(self, quantita: int):
        self.quantitaOrdinata = quantita
        

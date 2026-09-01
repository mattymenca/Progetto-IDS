from Model.Ordine.ordine import Ordine

class Persona:
    def __init__(self, nome, cognome, eta, ordini: list[Ordine]):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.ordini = ordini if ordini is not None else []

    def getNome(self):
        return self.nome
    
    def getCognome(self):
        return self.cognome
    
    def getEta(self):
        return self.eta
    
    def getOrdini(self):
        return self.ordini
    
    def setNome(self, nome: str):
        self.nome = nome

    def setCognome(self, cognome: str):
        self.cognome = cognome

    def setEta(self, eta: int):
        self.eta = eta

    def aggiungiOrdine(self, ordine: Ordine):
        self.ordini.append(ordine)
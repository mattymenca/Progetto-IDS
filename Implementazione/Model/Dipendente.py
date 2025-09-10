import StatoDipendente
from Contratto import Contratto
from Persona import Persona

class Dipendente:

    def __init__(self, nome, cognome, eta, ordini, storicoContratti: list[Contratto], statoDipendente: StatoDipendente):
        super().__init__(nome, cognome, eta, ordini)
        self.storicoContratti = storicoContratti
        self.statoDipendente = statoDipendente

    def getStoricoContratti(self):
        return self.storicoContratti
    
    def getStatoDipendente(self):
        return self.statoDipendente
    
    def modificaStatoDipendente(self, statoDipendente: StatoDipendente):
        self.statoDipendente = statoDipendente

    def aggiungiContratto(self, contratto: Contratto):
        self.getStoricoContratti.append(contratto)
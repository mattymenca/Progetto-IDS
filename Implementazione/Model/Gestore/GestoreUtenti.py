from Model.Dati import Dati
from Model.Utente import Contratto, Dipendente, Manager

class GestoreUtenti:
    def __init__(self, dati: Dati):
        self.dati = dati
        
    def aggiungiContratto(self,contratto: Contratto):
        self.dati.contratti.append(contratto)
    
    
    def aggiungiDipendente(self, dipendente: Dipendente):
        if not dipendente in self.dati.dipendenti():
            self.dati.dipendenti.append(dipendente)
            return True
        return False
    
     
    def eliminaContratto(self, contratto: Contratto):
        if contratto in self.dati.contratti:
            self.dati.contratti.remove(contratto)
            return True
        return False
    
    
    def eliminaDipendente(self, dipendente: Dipendente):
        if dipendente in self.dati.dipendenti:
            self.dati.dipendenti.remove(dipendente)
            return True
        return False
    
    
    def cambiaManager(self, manager: Manager):
        if not self.dati.manager is manager:
            self.dati.manager = manager
    
    
    def validaCredenziali(self, nome, password):
        if nome != self.dati.manager.nome or password != self.dati.manager.password:
            return False
        return True
    
    
    def modificaCredenziali(self, nome, nuovaPassword):
        if GestoreUtenti.validaCredenziali(nome, nuovaPassword):
            print("Reinserire nome e password")
            return False
        
        self.dati.manager.password = nuovaPassword
        print("Password modificata")
        return True
    
    def cercaDipendente(self, dipendente: Dipendente):
        for d in self.dati.dipendenti:
            if d.nome == dipendente.nome and d.cognome == dipendente.cognome:
                return d
        return None
    
    
    def modificaDettagliDipendente(self, dipendente: Dipendente, **kwargs):
        d = self.cercaDipendente(dipendente)
        
        if d is None:
            return False
        
        for attr, valore_attr in kwargs:
            if hasattr(d, attr):
                setattr(d, attr, valore_attr)
                return True
            else:
                print("Attributo non esistente")
                return False
    
    
    def licenziaDipendente(self, dipendente: Dipendente):
        d = self.cercaDipendente(dipendente)
        
        if d is None:
            return False
        
        self.modificaDettagliDipendente(statoDipendente="licenziato")
        return True
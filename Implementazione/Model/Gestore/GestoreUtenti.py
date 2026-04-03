from Model.Dati import Dati
from Model.Utente.Contratto import Contratto
from Model.Utente.Dipendente import Dipendente
from Model.Utente.Manager import Manager
from Model.Utente.StatoDipendente import StatoDipendente

class GestoreUtenti:
    
    def __init__(self, dati: Dati):
        self.dati = dati
        
    def aggiungiContratto(self,contratto: Contratto):
        self.dati.contratti.append(contratto)
    
    def aggiungiDipendente(self, dipendente: Dipendente):
        if not dipendente in self.dati.dipendenti:
            self.dati.dipendenti.append(dipendente)
            self.dati.setDirty()
            return True
        return False
     
    def eliminaContratto(self, contratto: Contratto):
        if contratto in self.dati.contratti:
            self.dati.contratti.remove(contratto)
            self.dati.setDirty()
            return True
        return False 
    
    def eliminaDipendente(self, dipendente: Dipendente):
        if dipendente in self.dati.dipendenti:
            self.dati.dipendenti.remove(dipendente)
            self.dati.setDirty()
            return True
        return False
    
    def cambiaManager(self, manager: Manager):
        if not self.dati.manager is manager:
            self.dati.manager = manager
            self.dati.setDirty()
            return True
        return False
    
    def validaCredenziali(self, nome, password):
        if self.dati.manager is None:
            return False
        if nome != self.dati.manager.nome or password != self.dati.manager.password:
            return False
        return True
    
    #funzione che controlla prima se le vecchie credenziali sono corrette, in tal caso le modifica, altrimenti restituisce falso
    def modificaCredenziali(self, nome, vecchiaPassword, nuovaPassword):
        if self.validaCredenziali(nome, vecchiaPassword):
            self.dati.manager.password = nuovaPassword
            print("Password modificata")
            self.dati.setDirty()
            return True
        
        print("Nome utente o vecchia password errati")
        return False
         
    def cercaDipendente(self, dipendente: Dipendente):
        for d in self.dati.dipendenti:
            if d.nome == dipendente.nome and d.cognome == dipendente.cognome:
                return d
        return None
    
    #modifica gli attributi passati come argomento se esistenti, altrimenti restituisce falso
    def modificaDettagliDipendente(self, d: Dipendente, **kwargs):
      
        for attr, valore in kwargs.items():
            if not hasattr(d, attr):
                return False
            setattr(d, attr, valore)
        self.dati.setDirty()
        return True
    
    def licenziaDipendente(self, dipendente: Dipendente):
        return self.modificaDettagliDipendente(dipendente, stato=StatoDipendente.LICENZIATO)
    
    def logout(self, path: str):
        return self.dati.salvaTutto(path)
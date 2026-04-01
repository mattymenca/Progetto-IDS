from Model.Dati import Dati
from Model.Utente import Contratto, Dipendente, Manager

class GestoreUtenti:
    def __init__(self, dati: Dati):
        self.dati = dati
        
    def aggiungiContratto(self,contratto: Contratto):
        self.dati.contratti.append(contratto)
    
    
    def aggiungiDipendente(self, dipendente: Dipendente):
        if not dipendente in self.dati.dipendenti:
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
    
    #funzione che controlla prima se le vecchie credenziali sono corrette, in tal caso le modifica, altrimenti restituisce falso
    def modificaCredenziali(self, nome, vecchiaPassword, nuovaPassword):
        if self.validaCredenziali(nome, vecchiaPassword):
            self.dati.manager.password = nuovaPassword
            print("Password modificata")
            return True
        else:
            print("Nome utente o vecchia password errati")
            return False
         
    def cercaDipendente(self, dipendente: Dipendente):
        for d in self.dati.dipendenti:
            if d.nome == dipendente.nome and d.cognome == dipendente.cognome:
                return d
        return None
    
    #modifica gli attributi passati come argomento se esistenti, altrimenti restituisce falso
    def modificaDettagliDipendente(self, d: Dipendente, **kwargs):
      
        for attr, valore_attr in kwargs.items():
            if hasattr(d, attr):
                setattr(d, attr, valore_attr)
            else:
                print("Attributo non esistente")
                return False
        return True
    
    def licenziaDipendente(self, dipendente: Dipendente):
        self.modificaDettagliDipendente(dipendente, statoDipendente="licenziato")
        return True
    
    def logout():
        Dati.salvaTutto("dati.txt")
        return True
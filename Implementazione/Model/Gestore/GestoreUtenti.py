from Model.Dati import Dati
from Model.Utente import Contratto, Dipendente, Manager
from Model.Utente.StatoDipendente import StatoDipendente

class GestoreUtenti:
    def __init__(self, dati: Dati):
        self.dati = dati
        
    def aggiungiContratto(self, contratto: Contratto):
        self.dati.contratti.append(contratto)
    
    def aggiungiDipendente(self, dipendente: Dipendente) -> bool:
        if dipendente not in self.dati.dipendenti:
            self.dati.dipendenti.append(dipendente)
            return True
        return False
     
    def eliminaContratto(self, contratto: Contratto) -> bool:
        if contratto in self.dati.contratti:
            self.dati.contratti.remove(contratto)
            return True
        return False
    
    def eliminaDipendente(self, dipendente: Dipendente) -> bool:
        if dipendente in self.dati.dipendenti:
            self.dati.dipendenti.remove(dipendente)
            return True
        return False
    
    def cambiaManager(self, manager: Manager):
        if self.dati.manager is not manager:
            self.dati.manager = manager
    
    def validaCredenziali(self, nome: str, password: str) -> bool:
        if not self.dati.manager:
            return False
        return self.dati.manager.nome == nome and self.dati.manager.password == password
    
    def modificaCredenziali(self, nome: str, vecchiaPassword: str, nuovaPassword: str) -> bool:
        if self.validaCredenziali(nome, vecchiaPassword):
            self.dati.manager.password = nuovaPassword
            print("Password modificata")
            return True
        print("Nome utente o vecchia password errati")
        return False
         
    def cercaDipendente(self, nome: str, cognome: str):
        for d in self.dati.dipendenti:
            if d.nome == nome and d.cognome == cognome:
                return d
        return None
    
    def modificaDettagliDipendente(self, dipendente: Dipendente, **kwargs) -> bool:
        for attr, valore_attr in kwargs.items():
            if hasattr(dipendente, attr):
                setattr(dipendente, attr, valore_attr)
            else:
                print("Attributo non esistente")
                return False
        return True
    
    def licenziaDipendente(self, dipendente: Dipendente) -> bool:
        return self.modificaDettagliDipendente(dipendente, statoDipendente=StatoDipendente.LICENZIATO) 
    
    def logout(self) -> bool:
        self.dati.salvaTutto("dati.pkl")
        return True
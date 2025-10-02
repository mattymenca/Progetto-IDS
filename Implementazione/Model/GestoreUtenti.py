from Implementazione.Model.Dati import Dati
from Implementazione.Model.Utente import Contratto, Dipendente, Manager

class GestoreUtenti:
    @staticmethod
    def aggiungiContratto(contratto: Contratto, dati: Dati):
        dati.contratti.append(contratto)
    
    @staticmethod
    def aggiungiDipendente(dipendente: Dipendente, dati: Dati):
        if not dipendente in dati.dipendenti():
            dati.dipendenti.append(dipendente)
            return True
        return False
    
    @staticmethod
    def eliminaContratto(contratto: Contratto, dati: Dati):
        if contratto in dati.contratti:
            dati.contratti.remove(contratto)
            return True
        return False
    
    @staticmethod
    def eliminaDipendente(dipendente: Dipendente, dati: Dati):
        if dipendente in dati.dipendenti:
            dati.dipendenti.remove(dipendente)
            return True
        return False
    
    @staticmethod
    def cambiaManager(manager: Manager, dati: Dati):
        if not dati.manager is manager:
            dati.manager = manager
    
    @staticmethod
    def validaCredenziali(nome, password, dati: Dati):
        if nome != dati.manager.nome or password != dati.manager.password:
            print("Credenziali errate\n")
            return False
        return True
    
    @staticmethod
    def modificaCredenziali(nome, password, nuovaPassword, dati: Dati):
        if GestoreUtenti.validaCredenziali(nome, password) == False:
            print("Reinserire nome e password")
            return False
        
        dati.manager.password = nuovaPassword
        print("password modificata")
        return True
    
    def cercaDipendente(dati: Dati, dipendente: Dipendente):
        for d in dati.dipendenti():
            if d.nome == dipendente.nome and d.cognome == dipendente.cognome:
                return d
        return None
    
    @staticmethod
    def modificaDettagliDipendente(dipendente: Dipendente, **kwargs):
        d = GestoreUtenti.cercaDipendente(dipendente)
        
        if d is None:
            return False
        
        for chiave, valore in kwargs:
            if hasattr(d, chiave):
                setattr(d, chiave, valore)
                return True
            else:
                print("Attributo non esistente")
                return False
    
    @staticmethod
    def licenziaDipendente(dipendente: Dipendente):
        d = GestoreUtenti.cercaDipendente(dipendente)
        
        if d is None:
            return False
        
        GestoreUtenti.modificaDettagliDipendente(statoDipendente="licenziato")
        return True
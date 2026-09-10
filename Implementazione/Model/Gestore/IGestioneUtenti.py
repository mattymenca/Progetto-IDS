from abc import ABC, abstractmethod

class IGestioneUtenti(ABC):

    @abstractmethod
    def validaCredenziali(self, nome, password):
        # Verifica le credenziali di accesso del manager
        pass

    @abstractmethod
    def assumiDipendente(self, nome, cognome, eta, tipo_contratto, salario, data_inizio, data_fine):
        # Crea e registra un nuovo dipendente con relativo contratto
        pass

    @abstractmethod
    def cambiaStatoDipendente(self, dipendente, nuovo_stato):
        # Aggiorna lo stato lavorativo del dipendente
        pass

    @abstractmethod
    def modificaDatiDipendente(self, dipendente, column, valore_testo):
        # Modifica l'attributo specifico del dipendente o del suo contratto
        pass
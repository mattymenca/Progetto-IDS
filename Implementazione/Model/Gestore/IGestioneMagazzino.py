from abc import ABC, abstractmethod

class IGestioneMagazzino(ABC):

    @abstractmethod
    def aggiungiProdotto(self, nome, qta, prezzo, costo, fornitore, soglia):
        # Aggiunge un nuovo prodotto al magazzino
        pass

    @abstractmethod
    def rifornisciProdotto(self, prodotto, qta_aggiuntiva):
        # Incrementa la quantita disponibile di un prodotto
        pass

    @abstractmethod
    def eliminaProdotto(self, indice_prodotto):
        # Rimuove un prodotto dalla lista tramite il suo indice
        pass

    @abstractmethod
    def modificaDatiProdotto(self, prodotto, column, valore_testo):
        # Aggiorna il campo del prodotto in base alla colonna modificata
        pass
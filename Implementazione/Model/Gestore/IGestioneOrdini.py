from abc import ABC, abstractmethod

class IGestioneOrdini(ABC):

    @abstractmethod
    def creaOrdine(self, persona, prodotti_carrello, coperti):
        # Crea un nuovo ordine, scala le quantita dal magazzino e lo assegna all'operatore
        pass

    @abstractmethod
    def annullaOrdine(self, ordine):
        # Annulla l'ordine e ripristina le scorte dei prodotti a magazzino
        pass

    @abstractmethod
    def modificaOrdine(self, ordine_vecchio, persona, nuovi_prodotti_carrello, nuovi_coperti):
        # Annulla l'ordine precedente e crea il nuovo ordine aggiornato
        pass
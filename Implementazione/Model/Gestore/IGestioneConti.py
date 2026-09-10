from abc import ABC, abstractmethod

class IGestioneConti(ABC):

    @abstractmethod
    def calcolaTotale(self, ordine) -> float:
        # Calcola il totale dell'ordine comprensivo di coperti e prodotti.
        pass

    @abstractmethod
    def emettiContoEChiudi(self, ordine, metodo_pagamento):
        # Genera il conto, aggiorna lo stato dell'ordine e salva i dati.
        pass
from Model.Dati import Dati
from Model.Conto import Conto, MetodoPagamento
from Model.Ordine.ordine import Ordine
from Model.Gestore.GestoreOrdini import GestoreOrdini

class GestoreConti:
    def __init__(self, dati: Dati, gestoreOrdini: GestoreOrdini):
        self.dati = dati
        self.gestoreOrdini = gestoreOrdini

    def creaConto(self, ordine: Ordine, metodoPagamento: MetodoPagamento) -> Conto:
        nuovoConto = Conto(ordine.getId(), metodoPagamento)
        nuovoConto.calcolaTotale()
        
        # Conclude l'ordine e lo sposta automaticamente nello storico
        self.gestoreOrdini.concludiOrdine(ordine)
        return nuovoConto
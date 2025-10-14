from Implementazione.Model import GestoreOrdini
from Implementazione.Model.Conto import Conto, MetodoPagamento
from Implementazione.Model.Dati import Dati
from Implementazione.Model.Ordine.ordine import Ordine


class GestoreConti:

    @staticmethod     
    def creaConto(ordine: Ordine, metodoPagamento: MetodoPagamento, dati: Dati) -> Conto:
        nuovoConto = Conto(ordine.getId(), metodoPagamento)
        nuovoConto.calcolaTotale()
        GestoreOrdini.concludiOrdine(ordine)
        
        return nuovoConto
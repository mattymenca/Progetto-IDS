from Implementazione.Model import GestoreOrdini
from Implementazione.Model.Conto import Conto, MetodoPagamento
from Implementazione.Model.Ordine.Ordine import Ordine


class GestoreConti:

    @staticmethod     
    def creaConto(ordine: Ordine, metodoPagamento: MetodoPagamento) -> Conto:
        nuovoConto = Conto(ordine.getId(), metodoPagamento)
        nuovoConto.calcolaTotale()
        GestoreOrdini.concludiOrdine(ordine)
        return nuovoConto

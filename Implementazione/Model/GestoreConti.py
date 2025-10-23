from Model.GestoreOrdini import GestoreOrdini
from Model.Conto import Conto, MetodoPagamento
from Model.Ordine.ordine import Ordine


class GestoreConti:

    @staticmethod     
    def creaConto(ordine: Ordine, metodoPagamento: MetodoPagamento) -> Conto:
        nuovoConto = Conto(ordine.getId(), metodoPagamento)
        nuovoConto.calcolaTotale()
        GestoreOrdini.concludiOrdine(ordine)
        return nuovoConto

from Model.Conto.Conto import Conto
from Model.Ordine.StatoOrdine import StatoOrdine


class GestoreConti:
    def __init__(self, dati):
        self.dati = dati

    def calcolaTotale(self, ordine):
        if not ordine:
            return 0.0

        totale = 2.0 * ordine.getNumeroCoperti()

        for p in ordine.getProdottiOrdinati():
            totale += p.getPrezzo() * p.getQuantita()

        return totale

    def emettiContoEChiudi(self, ordine, metodo_pagamento):
        if not ordine:
            return None

        conto = Conto(ordine, metodo_pagamento)
        conto.calcolaTotale()

        ordine.setStatoOrdine(StatoOrdine.CONCLUSO)

        if ordine in self.dati.ordini:
            self.dati.ordini.remove(ordine)

        if ordine not in self.dati.storico_ordini:
            self.dati.storico_ordini.append(ordine)

        self.dati.salvaTutto("dati.pkl")

        return conto
from Model.Conto.Conto import Conto
from Model.Ordine.StatoOrdine import StatoOrdine


class GestoreConti:

    @staticmethod
    def calcolaTotale(ordine):
        if not ordine:
            return 0.0

        totale = 2.0 * ordine.getNumeroCoperti()

        for p in ordine.getProdottiOrdinati():
            totale += p.getPrezzo() * p.getQuantita()

        return totale

    @staticmethod
    def emettiContoEChiudi(dati, ordine, metodo_pagamento):
        if not ordine:
            return None

        conto = Conto(ordine, metodo_pagamento)
        conto.calcolaTotale()

        ordine.setStatoOrdine(StatoOrdine.CONCLUSO)

        if ordine in dati.ordini:
            dati.ordini.remove(ordine)

        if ordine not in dati.storico_ordini:
            dati.storico_ordini.append(ordine)

        dati.salvaTutto("dati.pkl")

        return conto

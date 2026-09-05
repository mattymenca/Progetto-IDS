from Model.Conto.Conto import Conto
from Model.Ordine.StatoOrdine import StatoOrdine

class GestoreConti:
    @staticmethod
    def calcolaTotale(ordine):
        """Calcola il totale complessivo dell'ordine (Coperti + Consumazioni)"""
        if not ordine:
            return 0.0
        totale = 2.0 * ordine.getNumeroCoperti() # 2.00 € per coperto
        for p in ordine.getProdottiOrdinati():
            totale += p.getPrezzo() * p.getQuantita()
        return totale

    @staticmethod
    def emettiContoEChiudi(dati, ordine, metodo_pagamento):
        """Crea il conto, imposta lo stato CONCLUSO e sposta l'ordine nello storico permanente"""
        if not ordine or ordine not in dati.ordini:
            return None

        # 1. Crea il conto
        conto = Conto(ordine, metodo_pagamento)
        conto.calcolaTotale()

        # 2. Imposta stato ordine a CONCLUSO
        ordine.setStato(StatoOrdine.CONCLUSO)

        # 3. Sposta dagli ordini attivi allo storico permanente
        dati.ordini.remove(ordine)
        dati.storicoOrdini.append(ordine)

        # 4. Salvataggio persistente
        dati.salvaTutto("dati.pkl")
        return conto
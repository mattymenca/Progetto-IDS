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

        # 1. Crea conto e calcola il totale
        conto = Conto(ordine, metodo_pagamento)
        conto.calcolaTotale()

        # 2. Imposta lo stato a CONCLUSO
        if hasattr(ordine, 'setStato'):
            ordine.setStato(StatoOrdine.CONCLUSO)
        elif hasattr(ordine, 'setStatoOrdine'):
            ordine.setStatoOrdine(StatoOrdine.CONCLUSO)

        # 3. Rimuove dagli ordini attivi e sposta nello storico permanente
        if ordine in dati.ordini:
            dati.ordini.remove(ordine)

        if hasattr(dati, 'storico_ordini') and isinstance(dati.storico_ordini, list):
            if ordine not in dati.storico_ordini:
                dati.storico_ordini.append(ordine)

        # 4. Salvataggio su disco
        dati.salvaTutto("dati.pkl")
        return conto
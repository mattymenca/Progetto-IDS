from Model.Ordine.ordine import Ordine
from Model.Ordine.StatoOrdine import StatoOrdine

class GestoreOrdini:
    @staticmethod
    def _gen_id(dati):
        if hasattr(dati, 'genera_nuovo_id_ordine'):
            return dati.genera_nuovo_id_ordine()
        elif hasattr(dati, 'generaNuovoIdOrdine'):
            return dati.generaNuovoIdOrdine()
        return getattr(dati, 'prossimo_id_ordine', len(dati.ordini) + 1)

    @staticmethod
    def _set_qta(prodotto, quantita):
        if hasattr(prodotto, 'modificaQuantita'):
            prodotto.modificaQuantita(quantita)
        elif hasattr(prodotto, 'setQuantita'):
            prodotto.setQuantita(quantita)
        else:
            prodotto.quantita = quantita

    @staticmethod
    def creaOrdine(dati, operatore, prodotti_carrello, coperti):
        id_ordine = GestoreOrdini._gen_id(dati)
        
        lista_po = []
        for po, prod_originale in prodotti_carrello:
            lista_po.append(po)
            GestoreOrdini._set_qta(prod_originale, prod_originale.getQuantita() - po.getQuantita())

        nuovo_ordine = Ordine(id_ordine, lista_po, coperti)
        if hasattr(nuovo_ordine, 'setStato'): 
            nuovo_ordine.setStato(StatoOrdine.IN_CORSO)
        elif hasattr(nuovo_ordine, 'setStatoOrdine'): 
            nuovo_ordine.setStatoOrdine(StatoOrdine.IN_CORSO)
        
        dati.ordini.append(nuovo_ordine)

        # Associazione sicura all'operatore/cameriere
        if operatore:
            try:
                if hasattr(operatore, 'ordini') and isinstance(operatore.ordini, list):
                    operatore.ordini.append(nuovo_ordine)
                elif hasattr(operatore, 'aggiungiOrdine'):
                    operatore.aggiungiOrdine(nuovo_ordine)
            except Exception:
                pass

        dati.salvaTutto("dati.pkl")
        return nuovo_ordine

    @staticmethod
    def annullaOrdine(dati, ordine):
        if ordine in dati.ordini:
            for po in ordine.getProdottiOrdinati():
                for p in dati.prodotti:
                    if p.getNomeProdotto() == po.getNome():
                        GestoreOrdini._set_qta(p, p.getQuantita() + po.getQuantita())

            dati.ordini.remove(ordine)
            dati.salvaTutto("dati.pkl")
            return True
        return False

    @staticmethod
    def modificaOrdine(dati, ordine_vecchio, operatore, nuovi_prodotti_carrello, nuovi_coperti):
        GestoreOrdini.annullaOrdine(dati, ordine_vecchio)
        return GestoreOrdini.creaOrdine(dati, operatore, nuovi_prodotti_carrello, nuovi_coperti)
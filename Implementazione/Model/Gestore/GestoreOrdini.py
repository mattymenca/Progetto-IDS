from Model.Ordine.ordine import Ordine
from Model.Ordine.ProdottoOrdinato import ProdottoOrdinato
from Model.Ordine.StatoOrdine import StatoOrdine

class GestoreOrdini:
    @staticmethod
    def creaOrdine(dati, operatore, prodotti_carrello, coperti):
        """Crea un nuovo ordine, scala le scorte dal magazzino e lo associa all'operatore"""
        id_ordine = dati.genera_nuovo_id_ordine()
        
        lista_po = []
        for po, prod_originale in prodotti_carrello:
            lista_po.append(po)
            # Scala la quantità dal magazzino
            prod_originale.modificaQuantita(prod_originale.getQuantita() - po.getQuantita())

        nuovo_ordine = Ordine(id_ordine, lista_po, coperti)
        nuovo_ordine.setStato(StatoOrdine.IN_CORSO)
        
        dati.ordini.append(nuovo_ordine)

        # Associa l'ordine alla Persona (Dipendente o Manager)
        if operatore and hasattr(operatore, 'aggiungiOrdine'):
            operatore.aggiungiOrdine(nuovo_ordine)

        dati.salvaTutto("dati.pkl")
        return nuovo_ordine

    @staticmethod
    def annullaOrdine(dati, ordine):
        """Annulla un ordine attivo e ripristina le scorte in magazzino"""
        if ordine in dati.ordini:
            # Ripristina scorte
            for po in ordine.getProdottiOrdinati():
                for p in dati.prodotti:
                    if p.getNomeProdotto() == po.getNome():
                        p.modificaQuantita(p.getQuantita() + po.getQuantita())

            dati.ordini.remove(ordine)
            dati.salvaTutto("dati.pkl")
            return True
        return False

    @staticmethod
    def modificaOrdine(dati, ordine_vecchio, operatore, nuovi_prodotti_carrello, nuovi_coperti):
        """Modifica un ordine esistente ripristinando prima le vecchie scorte"""
        GestoreOrdini.annullaOrdine(dati, ordine_vecchio)
        return GestoreOrdini.creaOrdine(dati, operatore, nuovi_prodotti_carrello, nuovi_coperti)
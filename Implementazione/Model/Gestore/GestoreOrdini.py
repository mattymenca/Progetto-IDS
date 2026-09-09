from Model.Ordine.ordine import Ordine
from Model.Ordine.StatoOrdine import StatoOrdine

class GestoreOrdini:

    @staticmethod
    def creaOrdine(dati, persona, prodotti_carrello, coperti):
        id_ordine = dati.generaNuovoIdOrdine()
        lista_po = []

        for po, prod_originale in prodotti_carrello:
            lista_po.append(po)

            nuova_qta = prod_originale.getQuantita() - po.getQuantita()
            prod_originale.setQuantita(nuova_qta)

        nuovo_ordine = Ordine(id_ordine, lista_po, coperti)
        nuovo_ordine.setStatoOrdine(StatoOrdine.IN_CORSO)

        dati.ordini.append(nuovo_ordine)

        if persona:
            persona.aggiungiOrdine(nuovo_ordine)

        dati.salvaTutto("dati.pkl")

        return nuovo_ordine

    @staticmethod
    def annullaOrdine(dati, ordine):
        if ordine in dati.ordini:

            for po in ordine.getProdottiOrdinati():
                for p in dati.prodotti:

                    if p.getNomeProdotto() == po.getNome():
                        nuova_qta = p.getQuantita() + po.getQuantita()
                        p.setQuantita(nuova_qta)

            dati.ordini.remove(ordine)
            dati.salvaTutto("dati.pkl")

            return True

        return False

    @staticmethod
    def modificaOrdine(dati, ordine_vecchio, persona, nuovi_prodotti_carrello, nuovi_coperti):
        GestoreOrdini.annullaOrdine(dati, ordine_vecchio)
        return GestoreOrdini.creaOrdine(dati, persona, nuovi_prodotti_carrello, nuovi_coperti)

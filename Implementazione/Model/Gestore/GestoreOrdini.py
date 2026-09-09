from Model.Ordine.ordine import Ordine
from Model.Ordine.StatoOrdine import StatoOrdine

class GestoreOrdini:
    def __init__(self, dati):
        self.dati = dati

    def creaOrdine(self, persona, prodotti_carrello, coperti):
        id_ordine = self.dati.generaNuovoIdOrdine()
        lista_po = []

        for po, prod_originale in prodotti_carrello:
            lista_po.append(po)

            nuova_qta = prod_originale.getQuantita() - po.getQuantita()
            prod_originale.setQuantita(nuova_qta)

        nuovo_ordine = Ordine(id_ordine, lista_po, coperti)
        nuovo_ordine.setStatoOrdine(StatoOrdine.IN_CORSO)

        self.dati.ordini.append(nuovo_ordine)

        if persona:
            persona.aggiungiOrdine(nuovo_ordine)

        self.dati.salvaTutto("dati.pkl")

        return nuovo_ordine

    def annullaOrdine(self, ordine):
        if ordine in self.dati.ordini:

            for po in ordine.getProdottiOrdinati():
                for p in self.dati.prodotti:

                    if p.getNomeProdotto() == po.getNome():
                        nuova_qta = p.getQuantita() + po.getQuantita()
                        p.setQuantita(nuova_qta)

            self.dati.ordini.remove(ordine)
            self.dati.salvaTutto("dati.pkl")

            return True

        return False

    def modificaOrdine(self, ordine_vecchio, persona, nuovi_prodotti_carrello, nuovi_coperti):
        self.annullaOrdine(ordine_vecchio)
        return self.creaOrdine(persona, nuovi_prodotti_carrello, nuovi_coperti)
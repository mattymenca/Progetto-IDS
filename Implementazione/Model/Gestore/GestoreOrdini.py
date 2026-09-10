from Model.Gestore.IGestioneOrdini import IGestioneOrdini
from Model.Ordine.ordine import Ordine
from Model.Ordine.StatoOrdine import StatoOrdine

class GestoreOrdini(IGestioneOrdini):
    def __init__(self, dati):
        self.dati = dati

    def creaOrdine(self, persona, prodotti_carrello, coperti):
        # 1. Controllo preventivo di sicurezza sulle scorte disponibili
        for po, prod_originale in prodotti_carrello:
            if po.getQuantita() > prod_originale.getQuantita():
                raise ValueError(
                    f"Quantità insufficiente per '{prod_originale.getNomeProdotto()}'. "
                    f"Disponibili: {prod_originale.getQuantita()}."
                )

        # 2. Creazione dell'ordine e aggiornamento quantità
        id_ordine = self.dati.generaNuovoIdOrdine()
        lista_po = []

        for po, prod_originale in prodotti_carrello:
            lista_po.append(po)

            nuova_qta = prod_originale.getQuantita() - po.getQuantita()
            prod_originale.setQuantita(nuova_qta)  # Aggiorna anche statoProdotto tramite la classe Prodotto

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
                        p.setQuantita(nuova_qta)  # Ripristina quantità e statoProdotto in automatico

            self.dati.ordini.remove(ordine)
            self.dati.salvaTutto("dati.pkl")

            return True

        return False

    def modificaOrdine(self, ordine_vecchio, persona, nuovi_prodotti_carrello, nuovi_coperti):
        self.annullaOrdine(ordine_vecchio)
        return self.creaOrdine(persona, nuovi_prodotti_carrello, nuovi_coperti)
from Model.Dati import Dati
from Model.Ordine import StatoOrdine
from Model.Ordine.ProdottoOrdinato import ProdottoOrdinato
from Model.Ordine.ordine import Ordine

class GestoreOrdini:
    def __init__(self, dati: Dati):
        self.dati = dati

    def creaNuovoOrdine(self, prodottiOrdinati: list[ProdottoOrdinato], numeroCoperti: int) -> Ordine:
        id_ordine = self.dati.generaNuovoIdOrdine()
        nuovoOrdine = Ordine(id_ordine, prodottiOrdinati, numeroCoperti)
        
        self.dati.ordini.append(nuovoOrdine)
        self.approvaOrdine(nuovoOrdine)
        return nuovoOrdine

    def approvaOrdine(self, ordine: Ordine) -> bool:
        if ordine is None:
            return False
        
        for prodottoOrdinato in ordine.getProdottiOrdinati():
            nomeProdotto = prodottoOrdinato.getNome()
            prodotto = next((p for p in self.dati.prodotti if p.getNome() == nomeProdotto), None)

            if prodotto is None or prodottoOrdinato.getQuantita() > prodotto.getQuantita():
                self.impostaStatoOrdine(ordine, StatoOrdine.NON_APPROVATO)
                print("Ordine non approvato\n")
                return False

        self.impostaStatoOrdine(ordine, StatoOrdine.IN_CORSO)
        print("Ordine in corso\n")
        return True

    def impostaStatoOrdine(self, ordine: Ordine, stato: StatoOrdine) -> bool:
        if ordine is not None:
            ordine.setStatoOrdine(stato)
            return True
        return False

    def concludiOrdine(self, ordine: Ordine) -> bool:
        if ordine is None:
            return False
        
        self.impostaStatoOrdine(ordine, StatoOrdine.CONCLUSO)
        
        if ordine in self.dati.ordini:
            self.dati.ordini.remove(ordine)
            self.dati.storicoOrdini.append(ordine)
            return True
        return False

    def restituisciOrdine(self, idOrdine: int):
        for ordine in self.dati.ordini:
            if idOrdine == ordine.getId():
                return ordine
        return None

    def eliminaOrdine(self, ordine: Ordine) -> bool:
        if ordine in self.dati.ordini:
            self.dati.ordini.remove(ordine)
            return True
        return False
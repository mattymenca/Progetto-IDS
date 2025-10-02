from Implementazione.Model.Dati import Dati
from Implementazione.Model.Magazzino import Magazzino
from Implementazione.Model.Ordine import StatoOrdine
from Implementazione.Model.Ordine.ordine import Ordine

class GestoreOrdini:
    @staticmethod
    def approvaOrdine(ordine: Ordine, magazzino: Magazzino) -> bool:
        for prodottoOrdinato in ordine.getProdottiOrdinati():
            nomeProdotto = prodottoOrdinato.getNome()
            if prodottoOrdinato.getQuantita() > magazzino.prodottoDaInventario(nomeProdotto).getQuantita():
                GestoreOrdini.impostaStatoOrdine("non approvato")
                print("Ordine non approvato\n")
                return False
        GestoreOrdini.impostaStatoOrdine("in corso")
        print("Ordine in corso\n")
        return True
    
    # @staticmethod
    # def valida_ordine(ordine: Ordine, magazzino: Magazzino) -> bool:
    #     return all(
    #         p.getQuantita() <= magazzino.prodottoDaInventario(p.getNome()).getQuantita()
    #         for p in ordine.getProdottiOrdinati()
    #     )
    def impostaStatoOrdine(ordine: Ordine, stato: StatoOrdine):
        ordine.setStato(stato)
    
    @staticmethod
    def concludiOrdine(ordine: Ordine, dati: Dati):
        GestoreOrdini.impostaStatoOrdine("concluso")
        dati.ordini.append(ordine)
    
    @staticmethod
    def restituisciOrdine(idOrdine, ordini: list[Ordine]) -> Ordine:
        for ordine in ordini:
            if idOrdine == ordine.getId():
                return ordine
    
    @staticmethod
    def eliminaOrdine(idOrdine: int, ordini: list[Ordine]):
        for ordine in ordini:
            if idOrdine == ordine.getId():
                ordini.remove(ordine)    

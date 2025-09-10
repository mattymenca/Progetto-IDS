from StatoOrdine import StatoOrdine
from Ordine import Ordine
from Magazzino import Magazzino
from Prodotto import Prodotto
class Gestore:
    
    @staticmethod
    def validaOrdine(ordine: Ordine, magazzino: Magazzino) -> bool:
        for prodottoOrdinato in ordine.getProdottiOrdinati():
            nomeProdotto = prodottoOrdinato.getNome()
            if prodottoOrdinato.getQuantita() > magazzino.prodottoDaInventario(nomeProdotto).getQuantita():
                impostaStatoOrdine("non approvato")
                return False
        return True
    
    # @staticmethod
    # def valida_ordine(ordine: Ordine, magazzino: Magazzino) -> bool:
    #     return all(
    #         p.getQuantita() <= magazzino.prodottoDaInventario(p.getNome()).getQuantita()
    #         for p in ordine.getProdottiOrdinati()
    #     )

    @staticmethod
    def impostaStatoOrdine(ordine: Ordine, stato: StatoOrdine):
        ordine.setStato(stato)
    

from Model.Magazzino.Prodotto import Prodotto
from Model.Magazzino.StatoProdotto import StatoProdotto

class GestoreMagazzino:
    @staticmethod
    def _imposta_quantita(prodotto, nuova_quantita):
        """Metodo sicuro per impostare la quantità in qualsiasi variante del Modello"""
        if hasattr(prodotto, 'modificaQuantita'):
            prodotto.modificaQuantita(nuova_quantita)
        elif hasattr(prodotto, 'setQuantita'):
            prodotto.setQuantita(nuova_quantita)
        else:
            prodotto.quantita = nuova_quantita

    @staticmethod
    def aggiungiProdotto(dati, nome, qta, prezzo, costo, fornitore, soglia):
        nuovo = Prodotto(nome, qta, prezzo, costo, fornitore, True, soglia)
        dati.prodotti.append(nuovo)
        dati.salvaTutto("dati.pkl")
        return nuovo

    @staticmethod
    def rifornisciProdotto(dati, prodotto, qta_aggiuntiva):
        nuova_qta = prodotto.getQuantita() + qta_aggiuntiva
        GestoreMagazzino._imposta_quantita(prodotto, nuova_qta)
        
        if hasattr(prodotto, 'setStatoProdotto'):
            prodotto.setStatoProdotto(StatoProdotto.RIFORNITO)
        elif hasattr(prodotto, 'modificaStatoProdotto'):
            prodotto.modificaStatoProdotto(StatoProdotto.RIFORNITO)

        dati.salvaTutto("dati.pkl")

    @staticmethod
    def eliminaProdotto(dati, indice_prodotto):
        if 0 <= indice_prodotto < len(dati.prodotti):
            dati.prodotti.pop(indice_prodotto)
            dati.salvaTutto("dati.pkl")
            return True
        return False

    @staticmethod
    def salvaModificaCella(dati, prodotto, column, valore_testo):
        if column == 0 and hasattr(prodotto, 'setNome'): 
            prodotto.setNome(valore_testo)
        elif column == 1: 
            GestoreMagazzino._imposta_quantita(prodotto, int(valore_testo))
        elif column == 2 and hasattr(prodotto, 'setSoglia'): 
            prodotto.setSoglia(int(valore_testo))
        elif column == 3 and hasattr(prodotto, 'setPrezzo'): 
            prodotto.setPrezzo(float(valore_testo))
        elif column == 4 and hasattr(prodotto, 'setCosto'): 
            prodotto.setCosto(float(valore_testo))
        elif column == 5:
            if hasattr(prodotto, 'modificaFornitore'): prodotto.modificaFornitore(valore_testo)
            elif hasattr(prodotto, 'setFornitore'): prodotto.setFornitore(valore_testo)

        dati.salvaTutto("dati.pkl")
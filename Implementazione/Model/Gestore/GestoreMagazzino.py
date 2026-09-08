from Model.Magazzino.Prodotto import Prodotto
from Model.Magazzino.StatoProdotto import StatoProdotto

class GestoreMagazzino:
    
    @staticmethod
    def aggiungiProdotto(dati, nome, qta, prezzo, costo, fornitore, soglia):
        nuovo = Prodotto(nome, qta, prezzo, costo, fornitore, True, soglia)
        dati.prodotti.append(nuovo)
        dati.salvaTutto("dati.pkl")
        return nuovo

    @staticmethod
    def rifornisciProdotto(dati, prodotto, qta_aggiuntiva):
        nuova_qta = prodotto.getQuantita() + qta_aggiuntiva
        prodotto.setQuantita(nuova_qta)
        prodotto.setStatoProdotto(StatoProdotto.RIFORNITO)
        dati.salvaTutto("dati.pkl")

    @staticmethod
    def eliminaProdotto(dati, indice_prodotto):
        if 0 <= indice_prodotto < len(dati.prodotti):
            dati.prodotti.pop(indice_prodotto)
            dati.salvaTutto("dati.pkl")
            return True
        return False

    @staticmethod
    def modificaDatiProdotto(dati, prodotto, column, valore_testo):
        if column == 0:
            prodotto.setNomeProdotto(valore_testo)

        elif column == 1:
            GestoreMagazzino.modificaQuantita(
                prodotto,
                int(valore_testo)
            )

        elif column == 2:
            prodotto.setSoglia(int(valore_testo))

        elif column == 3:
            prodotto.setPrezzo(float(valore_testo))

        elif column == 4:
            prodotto.setCosto(float(valore_testo))

        elif column == 5:
            prodotto.setFornitore(valore_testo)

        dati.salvaTutto("dati.pkl")

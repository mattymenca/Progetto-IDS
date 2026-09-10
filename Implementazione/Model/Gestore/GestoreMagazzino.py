from Model.Gestore.IGestioneMagazzino import IGestioneMagazzino
from Model.Magazzino.Prodotto import Prodotto
from Model.Magazzino.StatoProdotto import StatoProdotto

class GestoreMagazzino(IGestioneMagazzino):
    def __init__(self, dati):
        self.dati = dati
        
        for p in self.dati.prodotti:
            p.aggiornaStatoProdotto()

    def aggiungiProdotto(self, nome, qta, prezzo, costo, fornitore, soglia):
        nuovo = Prodotto(nome, qta, prezzo, costo, fornitore, True, soglia)
        self.dati.prodotti.append(nuovo)
        self.dati.salvaTutto("dati.pkl")
        return nuovo

    def rifornisciProdotto(self, prodotto, qta_aggiuntiva):
        nuova_qta = prodotto.getQuantita() + qta_aggiuntiva
        prodotto.setQuantita(nuova_qta)
        prodotto.setStatoProdotto(StatoProdotto.RIFORNITO)
        self.dati.salvaTutto("dati.pkl")

    def eliminaProdotto(self, indice_prodotto):
        if 0 <= indice_prodotto < len(self.dati.prodotti):
            self.dati.prodotti.pop(indice_prodotto)
            self.dati.salvaTutto("dati.pkl")
            return True
        return False

    def modificaDatiProdotto(self, prodotto, column, valore_testo):
        if column == 0:
            prodotto.setNomeProdotto(valore_testo)

        elif column == 1:
            self.modificaQuantita(
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

        self.dati.salvaTutto("dati.pkl")
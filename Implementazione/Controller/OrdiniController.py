from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.ordini import Ui_OrdiniWindow
from Model.Ordine.ProdottoOrdinato import ProdottoOrdinato
from Model.Ordine.ordine import Ordine

class OrdiniController(QMainWindow, Ui_OrdiniWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        self.primary_controller = primary_controller
        self.carrello = []

        self.btn_aggiungi_prod.clicked.connect(self.aggiungi_al_carrello)
        self.btn_invia.clicked.connect(self.invia_ordine)
        self.btn_indietro.clicked.connect(self.torna_indietro)

        self.aggiorna_vista()

    def aggiorna_vista(self):
        self.combo_prodotti.clear()
        for p in self.primary_controller.dati.prodotti:
            if p.getQuantita() > 0:
                self.combo_prodotti.addItem(f"{p.getNomeProdotto()} (Disponibili: {p.getQuantita()})", p)
        self.carrello.clear()
        self.list_riepilogo.clear()

    def aggiungi_al_carrello(self):
        prodotto_obj = self.combo_prodotti.currentData()
        qta = self.spin_qta.value()

        if not prodotto_obj:
            QMessageBox.warning(self, "Errore", "Nessun prodotto disponibile selezionato.")
            return

        if qta > prodotto_obj.getQuantita():
            QMessageBox.warning(self, "Attenzione", f"Quantità insufficiente in magazzino! Disponibili solo {prodotto_obj.getQuantita()} pezzi.")
            return

        po = ProdottoOrdinato(prodotto_obj.getNomeProdotto(), prodotto_obj.getPrezzo(), qta)
        self.carrello.append((po, prodotto_obj))
        self.list_riepilogo.addItem(f"{qta}x {prodotto_obj.getNomeProdotto()} ({prodotto_obj.getPrezzo():.2f}€ cad.)")

    def invia_ordine(self):
        if not self.carrello:
            QMessageBox.warning(self, "Attenzione", "L'ordine non contiene alcun prodotto.")
            return

        ordine_id = self.spin_id.value()
        coperti = self.spin_coperti.value()

        lista_prodotti_ordinati = []
        for po, prod_originale in self.carrello:
            lista_prodotti_ordinati.append(po)
            # Sottrae la quantità dal magazzino
            prod_originale.modificaQuantita(prod_originale.getQuantita() - po.getQuantita())

        nuovo_ordine = Ordine(ordine_id, lista_prodotti_ordinati, coperti)
        self.primary_controller.dati.ordini.append(nuovo_ordine)
        self.primary_controller.salva_dati()  #salvo subito

        QMessageBox.information(self, "Successo", f"Ordine registrato con successo per il Tavolo {ordine_id}!")
        self.aggiorna_vista()

    def torna_indietro(self):
        from Controller.Dipendenti import DipendentiController
        self.primary_controller.mostra_finestra(DipendentiController, start_maximized=self.isMaximized())
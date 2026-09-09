from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.conti import Ui_ContiWindow
from Model.Conto.MetodoPagamento import MetodoPagamento

class ContiController(QMainWindow, Ui_ContiWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        self.primary_controller = primary_controller

        self.btn_calcola.clicked.connect(self.calcola_totale)
        self.btn_chiudi.clicked.connect(self.paga_e_chiudi)
        self.btn_indietro.clicked.connect(self.torna_indietro)

        self.aggiorna_vista()

    def aggiorna_vista(self):
        self.combo_ordini.clear()
        self.combo_pagamento.clear()

        for m in MetodoPagamento:
            self.combo_pagamento.addItem(m.value.upper(), m)

        ordini = self.primary_controller.dati.ordini
        for ord in ordini:
            self.combo_ordini.addItem(f"Ordine #{ord.getId()} ({ord.getNumeroCoperti()} coperti)", ord)

    def calcola_totale(self):
        ordine = self.combo_ordini.currentData()
        if not ordine:
            QMessageBox.warning(self, "Attenzione", "Nessun ordine aperto selezionato.")
            return

        try:
            totale = self.primary_controller.gestore_conti.calcolaTotale(ordine)
            self.lbl_totale.setText(f"Totale da Pagare: {totale:.2f} €")
        except Exception as e:
            QMessageBox.critical(self, "Errore Calcola Totale", f"Si è verificato un errore: {e}")

    def paga_e_chiudi(self):
        ordine = self.combo_ordini.currentData()
        metodo = self.combo_pagamento.currentData()

        if not ordine:
            QMessageBox.warning(self, "Attenzione", "Nessun ordine selezionato.")
            return

        try:
            conto = self.primary_controller.gestore_conti.emettiContoEChiudi(ordine, metodo)

            if conto:
                totale_incassato = conto.getTotale() if hasattr(conto, 'getTotale') else self.primary_controller.gestore_conti.calcolaTotale(ordine)
                QMessageBox.information(
                    self, 
                    "Pagamento Effettuato", 
                    f"Conto di {totale_incassato:.2f}€ incassato con successo!\nScontrino emesso."
                )
            else:
                QMessageBox.warning(self, "Attenzione", "Impossibile completare il conto per questo ordine.")

            # RITORNA AL MENU OPERATIVO
            self.torna_indietro()
        except Exception as e:
            QMessageBox.critical(self, "Errore Chiusura Conto", f"Si è verificato un errore durante l'incasso: {e}")

    def torna_indietro(self):
        from Controller.DipendentiController import DipendentiController
        self.primary_controller.mostra_finestra(DipendentiController, start_maximized=self.isMaximized())
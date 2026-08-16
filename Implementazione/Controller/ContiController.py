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

        # Delega il calcolo al GestoreConti
        totale = self.primary_controller.gestore_conti.calcola_totale(ordine)
        self.lbl_totale.setText(f"Totale da Pagare: {totale:.2f} €")

    def paga_e_chiudi(self):
        ordine = self.combo_ordini.currentData()
        metodo = self.combo_pagamento.currentData()

        if not ordine:
            return

        # Delega l'incasso e lo spostamento allo storico al GestoreConti
        totale = self.primary_controller.gestore_conti.chiudi_e_incassa_conto(
            ordine, self.primary_controller.dati
        )

        self.primary_controller.salva_dati()
        QMessageBox.information(self, "Pagamento Effettuato", f"Conto di {totale:.2f}€ incassato con successo!")
        self.torna_indietro()

    def torna_indietro(self):
        from Controller.DipendentiController import DipendentiController
        self.primary_controller.mostra_finestra(DipendentiController, start_maximized=self.isMaximized())

    def closeEvent(self, event):
        self.primary_controller.chiusura_sicura()
        event.accept()
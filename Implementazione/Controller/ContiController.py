from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.conti import Ui_ContiWindow
from Model.Conto.MetodoPagamento import MetodoPagamento
from Model.Gestore.GestoreConti import GestoreConti

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

        # DELEGA AL GESTORE CONTI
        totale = GestoreConti.calcolaTotale(ordine)
        self.lbl_totale.setText(f"Totale da Pagare: {totale:.2f} €")

    def paga_e_chiudi(self):
        ordine = self.combo_ordini.currentData()
        metodo = self.combo_pagamento.currentData()

        if not ordine: return

        # DELEGA AL GESTORE CONTI
        conto = GestoreConti.emettiContoEChiudi(self.primary_controller.dati, ordine, metodo)

        QMessageBox.information(self, "Pagamento Effettuato", f"Conto di {conto.getTotale():.2f}€ incassato con successo!")
        self.torna_indietro()

    def torna_indietro(self):
        from Controller.Dipendenti import DipendentiController
        self.primary_controller.mostra_finestra(DipendentiController, start_maximized=self.isMaximized())
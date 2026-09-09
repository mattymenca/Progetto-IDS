from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5.QtGui import QColor
from View.magazzino import Ui_MagazzinoWindow

class MagazzinoController(QMainWindow, Ui_MagazzinoWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        self.primary_controller = primary_controller

        self.btn_aggiungi.clicked.connect(self.aggiungi_prodotto)
        self.btn_rifornisci.clicked.connect(self.rifornisci_prodotto)
        self.btn_elimina.clicked.connect(self.elimina_prodotto)
        self.btn_indietro.clicked.connect(self.torna_indietro)

        self.tableWidget.cellChanged.connect(self.salva_modifica_cella)
        self.aggiorna_vista()

    def aggiorna_vista(self):
        self.tableWidget.blockSignals(True)
        self.tableWidget.setRowCount(0)
        prodotti = self.primary_controller.dati.prodotti
        
        for row, p in enumerate(prodotti):
            self.tableWidget.insertRow(row)
            
            item_nome = QTableWidgetItem(str(p.getNomeProdotto()))
            item_qta = QTableWidgetItem(str(p.getQuantita()))
            item_soglia = QTableWidgetItem(str(p.getSoglia()))
            item_prezzo = QTableWidgetItem(f"{p.getPrezzo():.2f}")
            item_costo = QTableWidgetItem(f"{p.getCosto():.2f}")
            item_fornitore = QTableWidgetItem(str(p.getFornitore()))

            # Evidenzia in rosso se sotto o pari alla soglia minima
            if p.getQuantita() <= p.getSoglia():
                color_rosso = QColor(231, 76, 60, 180)
                item_qta.setBackground(color_rosso)
                item_nome.setBackground(color_rosso)

            self.tableWidget.setItem(row, 0, item_nome)
            self.tableWidget.setItem(row, 1, item_qta)
            self.tableWidget.setItem(row, 2, item_soglia)
            self.tableWidget.setItem(row, 3, item_prezzo)
            self.tableWidget.setItem(row, 4, item_costo)
            self.tableWidget.setItem(row, 5, item_fornitore)
            
        self.tableWidget.blockSignals(False)

    def rifornisci_prodotto(self):
        row = self.tableWidget.currentRow()
        if row >= 0:
            try:
                prodotto = self.primary_controller.dati.prodotti[row]
                qta_aggiuntiva, ok = QInputDialog.getInt(
                    self, "Rifornisci Prodotto", 
                    f"Quanti pezzi vuoi aggiungere a '{prodotto.getNomeProdotto()}'?",
                    value=10, min=1, max=1000
                )
                if ok:
                    self.primary_controller.gestore_magazzino.rifornisciProdotto(prodotto, qta_aggiuntiva)
                    self.aggiorna_vista()
                    QMessageBox.information(self, "Rifornito", f"Aggiunti {qta_aggiuntiva} pezzi a {prodotto.getNomeProdotto()}!")
            except Exception as e:
                QMessageBox.critical(self, "Errore", f"Si è verificato un errore durante il rifornimento: {e}")
        else:
            QMessageBox.warning(self, "Attenzione", "Seleziona prima un prodotto dalla tabella.")

    def salva_modifica_cella(self, row, column):
        try:
            prodotto = self.primary_controller.dati.prodotti[row]
            valore_testo = self.tableWidget.item(row, column).text()

            self.primary_controller.gestore_magazzino.modificaDatiProdotto(prodotto, column, valore_testo)
            self.aggiorna_vista()
        except Exception:
            QMessageBox.warning(self, "Errore", "Valore inserito non valido!")
            self.aggiorna_vista()

    def aggiungi_prodotto(self):
        try:
            nome = self.input_nome.text()
            qta = int(self.input_qta.text())
            soglia = int(self.input_soglia.text() if self.input_soglia.text() else 5)
            prezzo = float(self.input_prezzo.text())
            costo = float(self.input_costo.text())
            fornitore = self.input_fornitore.text()

            if not nome:
                raise ValueError()

            self.primary_controller.gestore_magazzino.aggiungiProdotto(nome, qta, prezzo, costo, fornitore, soglia)
            self.aggiorna_vista()
            self.pulisci_input()
            QMessageBox.information(self, "Successo", "Prodotto aggiunto al magazzino!")
        except ValueError:
            QMessageBox.warning(self, "Errore", "Dati inseriti non validi.")

    def elimina_prodotto(self):
        row = self.tableWidget.currentRow()
        if row >= 0:
            self.primary_controller.gestore_magazzino.eliminaProdotto(row)
            self.aggiorna_vista()
            QMessageBox.information(self, "Successo", "Prodotto rimosso!")
        else:
            QMessageBox.warning(self, "Attenzione", "Seleziona una riga da eliminare.")

    def pulisci_input(self):
        self.input_nome.clear()
        self.input_qta.clear()
        self.input_soglia.clear()
        self.input_prezzo.clear()
        self.input_costo.clear()
        self.input_fornitore.clear()

    def torna_indietro(self):
        from Controller.DipendentiController import DipendentiController
        self.primary_controller.mostra_finestra(DipendentiController, start_maximized=self.isMaximized())
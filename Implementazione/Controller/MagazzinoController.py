from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
from View.magazzino import Ui_MagazzinoWindow
from Model.Magazzino.Prodotto import Prodotto
from Model.Magazzino.StatoProdotto import StatoProdotto

class MagazzinoController(QMainWindow, Ui_MagazzinoWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        self.primary_controller = primary_controller

        self.btn_aggiungi.clicked.connect(self.aggiungi_prodotto)
        self.btn_rifornisci.clicked.connect(self.rifornisci_prodotto)
        self.btn_elimina.clicked.connect(self.elimina_prodotto)
        self.btn_indietro.clicked.connect(self.torna_indietro)

        # Rileva modifiche manuali sulle celle della tabella
        self.tableWidget.cellChanged.connect(self.salva_modifica_cella)

        self.aggiorna_vista()

    def aggiorna_vista(self):
        # Disabilita temporaneamente il segnale per evitare di salvare mentre carichiamo la tabella
        self.tableWidget.blockSignals(True)
        self.tableWidget.setRowCount(0)
        prodotti = self.primary_controller.dati.prodotti
        for row, p in enumerate(prodotti):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(p.getNomeProdotto())))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(p.getQuantita())))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{p.getPrezzo():.2f}"))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{p.getCosto():.2f}"))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(p.getFornitore())))
        self.tableWidget.blockSignals(False)

    def rifornisci_prodotto(self):
        row = self.tableWidget.currentRow()
        if row >= 0:
            prodotto = self.primary_controller.dati.prodotti[row]
            qta_aggiuntiva, ok = QInputDialog.getInt(
                self, 
                "Rifornisci Prodotto", 
                f"Quanti pezzi vuoi aggiungere a '{prodotto.getNomeProdotto()}'?",
                value=10, min=1, max=1000
            )
            if ok:
                nuova_qta = prodotto.getQuantita() + qta_aggiuntiva
                prodotto.modificaQuantita(nuova_qta)
                prodotto.setStatoProdotto(StatoProdotto.RIFORNITO)
                
                # Salvataggio immediato su disco
                self.primary_controller.salva_dati()
                self.aggiorna_vista()
                QMessageBox.information(self, "Rifornito", f"Nuova quantità di {prodotto.getNomeProdotto()}: {nuova_qta}")
        else:
            QMessageBox.warning(self, "Attenzione", "Seleziona prima un prodotto da rifornire.")

    def salva_modifica_cella(self, row, column):
        """Salva nel modello quando l'utente modifica direttamente una cella della tabella"""
        try:
            prodotto = self.primary_controller.dati.prodotti[row]
            nuovo_valore = self.tableWidget.item(row, column).text()

            if column == 0: # Nome
                prodotto.setNome(nuovo_valore)
            elif column == 1: # Quantità
                prodotto.modificaQuantita(int(nuovo_valore))
            elif column == 2: # Prezzo
                prodotto.setPrezzo(float(nuovo_valore))
            elif column == 3: # Costo
                prodotto.setCosto(float(nuovo_valore))
            elif column == 4: # Fornitore
                prodotto.modificaFornitore(nuovo_valore)

            # Salva subito su disco
            self.primary_controller.salva_dati()
        except Exception:
            QMessageBox.warning(self, "Errore", "Valore inserito nella cella non valido!")
            self.aggiorna_vista()

    def aggiungi_prodotto(self):
        try:
            nome = self.input_nome.text()
            qta = int(self.input_qta.text())
            prezzo = float(self.input_prezzo.text())
            costo = float(self.input_costo.text())
            fornitore = self.input_fornitore.text()

            if not nome:
                raise ValueError("Nome vuoto")

            nuovo = Prodotto(nome, qta, prezzo, costo, fornitore, True, 5)
            self.primary_controller.dati.prodotti.append(nuovo)
            
            self.primary_controller.salva_dati()
            self.aggiorna_vista()
            self.pulisci_input()
            QMessageBox.information(self, "Successo", "Prodotto aggiunto al magazzino!")
        except ValueError:
            QMessageBox.warning(self, "Errore", "Dati non validi nei campi di inserimento.")

    def elimina_prodotto(self):
        row = self.tableWidget.currentRow()
        if row >= 0:
            self.primary_controller.dati.prodotti.pop(row)
            self.primary_controller.salva_dati()
            self.aggiorna_vista()
            QMessageBox.information(self, "Successo", "Prodotto rimosso!")
        else:
            QMessageBox.warning(self, "Attenzione", "Seleziona prima una riga da eliminare.")

    def pulisci_input(self):
        self.input_nome.clear()
        self.input_qta.clear()
        self.input_prezzo.clear()
        self.input_costo.clear()
        self.input_fornitore.clear()

    def torna_indietro(self):
        from Controller.Dipendenti import DipendentiController
        self.primary_controller.mostra_finestra(DipendentiController, start_maximized=self.isMaximized())
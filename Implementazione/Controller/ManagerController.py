from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog, QDialog, QVBoxLayout, QListWidget, QTabWidget, QWidget
from View.manager import Ui_ManagerWindow
from Model.Utente.Dipendente import Dipendente
from Model.Utente.StatoDipendente import StatoDipendente
from Model.Utente.Contratto import Contratto
from Model.Utente.TipoContratto import TipoContratto

class DettagliPersonaDialog(QDialog):
    """Finestra Pop-up generica per mostrare lo storico ordini (e contratti) di qualsiasi Persona (Manager o Dipendente)"""
    def __init__(self, persona, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Scheda e Storico: {persona.getNome()} {persona.getCognome()}")
        self.resize(650, 450)
        self.setStyleSheet("background-color: #2c3e50; color: white;")

        layout = QVBoxLayout(self)
        tabs = QTabWidget()
        tabs.setStyleSheet("QTabBar::tab { background: #34495e; color: white; padding: 8px; } QTabBar::tab:selected { background: #8e44ad; }")

        # TAB 1: STORICO ORDINI PRESI
        tab_ordini = QWidget()
        layout_o = QVBoxLayout(tab_ordini)
        list_o = QListWidget()
        list_o.setStyleSheet("background-color: #34495e; color: white; font-size: 14px;")
        
        ordini = persona.getOrdini() if hasattr(persona, 'getOrdini') else []
        if ordini:
            for o in ordini:
                tot = 2 * o.getNumeroCoperti() + sum(p.getPrezzo() * p.getQuantita() for p in o.getProdottiOrdinati())
                list_o.addItem(f"Ordine #{o.getId()} | Coperti: {o.getNumeroCoperti()} | Totale: {tot:.2f}€")
        else:
            list_o.addItem("Nessun ordine effettuato da questo operatore.")
            
        layout_o.addWidget(list_o)
        tabs.addTab(tab_ordini, "Storico Ordini Presi")

        # TAB 2: CONTRATTI (Se è un Dipendente)
        if hasattr(persona, 'getStoricoContratti') and persona.getStoricoContratti():
            tab_contratti = QWidget()
            layout_c = QVBoxLayout(tab_contratti)
            list_c = QListWidget()
            list_c.setStyleSheet("background-color: #34495e; color: white;")
            
            for c in persona.getStoricoContratti():
                tipo = c.getTipoContratto().value.title() if isinstance(c.getTipoContratto(), TipoContratto) else str(c.getTipoContratto())
                list_c.addItem(f"Contratto: {tipo} | Salario: {c.getSalario():.2f}€ | Inizio: {c.getDataInizio()} - Fine: {c.getDataFine()}")
            
            layout_c.addWidget(list_c)
            tabs.addTab(tab_contratti, "Storico Contratti")

        layout.addWidget(tabs)

class ManagerController(QMainWindow, Ui_ManagerWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        self.primary_controller = primary_controller

        self.btn_assumi.clicked.connect(self.assumi)
        self.btn_licenzia.clicked.connect(self.cambia_stato_dipendente)
        self.btn_profilo_manager.clicked.connect(self.apri_profilo_manager)
        self.btn_indietro.clicked.connect(self.logout)

        self.tableWidget.itemDoubleClicked.connect(self.apri_dettagli_dipendente)
        self.tableWidget.cellChanged.connect(self.salva_modifica_cella)

        self.aggiorna_vista()

    def aggiorna_vista(self):
        self.tableWidget.blockSignals(True)
        self.combo_tipo_contratto.clear()
        
        for tipo in TipoContratto:
            self.combo_tipo_contratto.addItem(tipo.value.title(), tipo)

        self.tableWidget.setRowCount(0)
        dipendenti = self.primary_controller.dati.dipendenti

        for row, d in enumerate(dipendenti):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(d.getNome()))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(d.getCognome()))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(d.getEta())))

            storico = d.getStoricoContratti()
            if storico:
                ultimo = storico[-1]
                tipo_str = ultimo.getTipoContratto().value.title() if isinstance(ultimo.getTipoContratto(), TipoContratto) else str(ultimo.getTipoContratto())
                salario_str = f"{ultimo.getSalario():.2f}"
                d_inizio = str(ultimo.getDataInizio())
                d_fine = str(ultimo.getDataFine())
            else:
                tipo_str, salario_str, d_inizio, d_fine = "N/D", "0.00", "N/D", "N/D"

            self.tableWidget.setItem(row, 3, QTableWidgetItem(tipo_str))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(salario_str))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(d_inizio))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(d_fine))

            stato_str = d.getStatoDipendente().value.upper() if isinstance(d.getStatoDipendente(), StatoDipendente) else str(d.getStatoDipendente())
            self.tableWidget.setItem(row, 7, QTableWidgetItem(stato_str))

        self.tableWidget.blockSignals(False)

    def apri_profilo_manager(self):
        manager = self.primary_controller.dati.manager
        if manager:
            dialog = DettagliPersonaDialog(manager, self)
            dialog.exec_()
        else:
            QMessageBox.warning(self, "Errore", "Nessun Manager registrato.")

    def apri_dettagli_dipendente(self, item):
        row = item.row()
        dipendente = self.primary_controller.dati.dipendenti[row]
        dialog = DettagliPersonaDialog(dipendente, self)
        dialog.exec_()

    def assumi(self):
        try:
            nome = self.input_nome.text()
            cognome = self.input_cognome.text()
            eta = int(self.input_eta.text())
            salario = float(self.input_salario.text())
            tipo_contratto = self.combo_tipo_contratto.currentData()

            d_inizio = self.date_inizio.date().toString("yyyy-MM-dd")
            d_fine = self.date_fine.date().toString("yyyy-MM-dd")

            nuovo_contratto = Contratto(tipo_contratto, d_inizio, d_fine, salario)
            nuovo_dipendente = Dipendente(nome, cognome, eta, [], [nuovo_contratto], StatoDipendente.IMPIEGATO)

            self.primary_controller.dati.dipendenti.append(nuovo_dipendente)
            self.primary_controller.salva_dati()

            self.aggiorna_vista()
            self.pulisci_input()
            QMessageBox.information(self, "Successo", f"Dipendente {nome} assunto!")
        except ValueError:
            QMessageBox.warning(self, "Errore", "Dati inseriti non validi.")

    def salva_modifica_cella(self, row, column):
        try:
            dipendente = self.primary_controller.dati.dipendenti[row]
            nuovo_valore = self.tableWidget.item(row, column).text()

            if column == 0: dipendente.setNome(nuovo_valore)
            elif column == 1: dipendente.setCognome(nuovo_valore)
            elif column == 2: dipendente.setEta(int(nuovo_valore))
            elif column in [3, 4, 5, 6]:
                storico = dipendente.getStoricoContratti()
                if storico:
                    c = storico[-1]
                    if column == 4: c.modificaSalario(float(nuovo_valore))
                    elif column == 5: c.setDataInizio(nuovo_valore)
                    elif column == 6: c.setDataFine(nuovo_valore)

            self.primary_controller.salva_dati()
        except Exception:
            QMessageBox.warning(self, "Errore", "Valore non valido!")
            self.aggiorna_vista()

    def cambia_stato_dipendente(self):
        row = self.tableWidget.currentRow()
        if row >= 0:
            dipendente = self.primary_controller.dati.dipendenti[row]
            stati = [s.value.upper() for s in StatoDipendente]
            scelta, ok = QInputDialog.getItem(self, "Stato", f"Nuovo stato per {dipendente.getNome()}:", stati, 0, False)
            if ok and scelta:
                for s in StatoDipendente:
                    if s.value.upper() == scelta:
                        dipendente.modificaStatoDipendente(s)
                        break
                self.primary_controller.salva_dati()
                self.aggiorna_vista()

    def pulisci_input(self):
        self.input_nome.clear(); self.input_cognome.clear()
        self.input_eta.clear(); self.input_salario.clear()

    def logout(self):
        from Controller.Inizio import InizioController
        self.primary_controller.mostra_finestra(InizioController, start_maximized=self.isMaximized())
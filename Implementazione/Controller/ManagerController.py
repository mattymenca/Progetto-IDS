from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5.QtCore import QDate
from View.manager import Ui_ManagerWindow
from Model.Utente.Dipendente import Dipendente
from Model.Utente.StatoDipendente import StatoDipendente
from Model.Utente.Contratto import Contratto
from Model.Utente.TipoContratto import TipoContratto

class ManagerController(QMainWindow, Ui_ManagerWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        self.primary_controller = primary_controller

        self.btn_assumi.clicked.connect(self.assumi)
        self.btn_licenzia.clicked.connect(self.cambia_stato_dipendente)
        self.btn_indietro.clicked.connect(self.logout)

        # Salva subito le modifiche fatte cliccando sulle celle della tabella
        self.tableWidget.cellChanged.connect(self.salva_modifica_cella)

        self.aggiorna_vista()

    def aggiorna_vista(self):
        self.tableWidget.blockSignals(True)
        self.combo_tipo_contratto.clear()
        
        # Popola tipi di contratto nella ComboBox
        for tipo in TipoContratto:
            self.combo_tipo_contratto.addItem(tipo.value.title(), tipo)

        # Popola Tabella
        self.tableWidget.setRowCount(0)
        dipendenti = self.primary_controller.dati.dipendenti

        for row, d in enumerate(dipendenti):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(d.getNome()))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(d.getCognome()))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(d.getEta())))

            # Ultimo contratto attivo
            storico = d.getStoricoContratti()
            if storico:
                ultimo_contratto = storico[-1]
                tipo_str = ultimo_contratto.getTipoContratto().value.title() if isinstance(ultimo_contratto.getTipoContratto(), TipoContratto) else str(ultimo_contratto.getTipoContratto())
                salario_str = f"{ultimo_contratto.getSalario():.2f}"
                d_inizio = str(ultimo_contratto.getDataInizio())
                d_fine = str(ultimo_contratto.getDataFine())
            else:
                tipo_str, salario_str, d_inizio, d_fine = "N/D", "0.00", "N/D", "N/D"

            self.tableWidget.setItem(row, 3, QTableWidgetItem(tipo_str))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(salario_str))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(d_inizio))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(d_fine))

            # Stato Dipendente
            stato_str = d.getStatoDipendente().value.upper() if isinstance(d.getStatoDipendente(), StatoDipendente) else str(d.getStatoDipendente())
            self.tableWidget.setItem(row, 7, QTableWidgetItem(stato_str))

        self.tableWidget.blockSignals(False)

    def assumi(self):
        try:
            nome = self.input_nome.text()
            cognome = self.input_cognome.text()
            eta = int(self.input_eta.text())
            salario = float(self.input_salario.text())
            tipo_contratto = self.combo_tipo_contratto.currentData()

            d_inizio = self.date_inizio.date().toString("yyyy-MM-dd")
            d_fine = self.date_fine.date().toString("yyyy-MM-dd")

            if not nome or not cognome:
                raise ValueError("Nome o cognome mancante")

            # 1. Creazione oggetto Contratto
            nuovo_contratto = Contratto(tipo_contratto, d_inizio, d_fine, salario)

            # 2. Creazione oggetto Dipendente
            nuovo_dipendente = Dipendente(
                nome=nome,
                cognome=cognome,
                eta=eta,
                ordini=[],
                storicoContratti=[nuovo_contratto],
                statoDipendente=StatoDipendente.IMPIEGATO
            )

            # 3. Aggiunta ai Dati e salvataggio
            self.primary_controller.dati.dipendenti.append(nuovo_dipendente)
            self.primary_controller.salva_dati()

            self.aggiorna_vista()
            self.pulisci_input()
            QMessageBox.information(self, "Successo", f"Dipendente {nome} {cognome} assunto con successo!")
        except ValueError:
            QMessageBox.warning(self, "Errore Inserimento", "Controlla di aver compilato tutti i campi correttamente.")

    def salva_modifica_cella(self, row, column):
        """Aggiorna sia il Dipendente che il suo Contratto quando una cella viene modificata direttamente"""
        try:
            dipendente = self.primary_controller.dati.dipendenti[row]
            nuovo_valore = self.tableWidget.item(row, column).text()

            # Modifica dati anagrafici
            if column == 0:
                dipendente.setNome(nuovo_valore)
            elif column == 1:
                dipendente.setCognome(nuovo_valore)
            elif column == 2:
                dipendente.setEta(int(nuovo_valore))

            # Modifica dati contratto
            elif column in [3, 4, 5, 6]:
                storico = dipendente.getStoricoContratti()
                if storico:
                    contratto_attuale = storico[-1]
                    if column == 4: # Salario
                        contratto_attuale.modificaSalario(float(nuovo_valore))
                    elif column == 5: # Data Inizio
                        contratto_attuale.setDataInizio(nuovo_valore)
                    elif column == 6: # Data Fine
                        contratto_attuale.setDataFine(nuovo_valore)

            # Salva subito su disco
            self.primary_controller.salva_dati()
        except Exception:
            QMessageBox.warning(self, "Errore", "Valore inserito non valido!")
            self.aggiorna_vista()

    def cambia_stato_dipendente(self):
        row = self.tableWidget.currentRow()
        if row >= 0:
            dipendente = self.primary_controller.dati.dipendenti[row]
            stati = [s.value.upper() for s in StatoDipendente]
            
            scelta, ok = QInputDialog.getItem(
                self, "Cambia Stato Dipendente", 
                f"Seleziona nuovo stato per {dipendente.getNome()}:", 
                stati, 0, False
            )
            
            if ok and scelta:
                for s in StatoDipendente:
                    if s.value.upper() == scelta:
                        dipendente.modificaStatoDipendente(s)
                        break
                
                self.primary_controller.salva_dati()
                self.aggiorna_vista()
                QMessageBox.information(self, "Aggiornato", f"Stato di {dipendente.getNome()} cambiato in {scelta}")
        else:
            QMessageBox.warning(self, "Attenzione", "Seleziona un dipendente dalla tabella.")

    def pulisci_input(self):
        self.input_nome.clear()
        self.input_cognome.clear()
        self.input_eta.clear()
        self.input_salario.clear()

    def logout(self):
        from Controller.Inizio import InizioController
        self.primary_controller.mostra_finestra(InizioController, start_maximized=self.isMaximized())
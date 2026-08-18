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
        self.ordine_in_modifica = None
        self.id_corrente = None

        self.btn_aggiungi_prod.clicked.connect(self.aggiungi_al_carrello)
        self.btn_invia.clicked.connect(self.salva_ordine)
        self.btn_nuovo.clicked.connect(self.prepara_nuovo_ordine)
        self.btn_carica_ordine.clicked.connect(self.carica_ordine_selezionato)
        self.btn_annulla_ordine.clicked.connect(self.annulla_ordine_selezionato)
        self.btn_indietro.clicked.connect(self.torna_indietro)

        # Ricerca dinamica prodotti e ordini mentre si digita
        self.input_filtro_prod.textChanged.connect(self.filtra_prodotti)
        self.input_cerca_id.textChanged.connect(self.filtra_ordini_attivi)

        self.aggiorna_vista()

    def genera_id_incrementale(self):
        return self.primary_controller.dati.genera_nuovo_id_ordine()

    def aggiorna_vista(self):
        # Popola Operatori
        self.combo_operatore.clear()
        for d in self.primary_controller.dati.dipendenti:
            self.combo_operatore.addItem(f"{d.getNome()} {d.getCognome()}", d)
        if self.primary_controller.dati.manager:
            m = self.primary_controller.dati.manager
            self.combo_operatore.addItem(f"Manager: {m.getNome()} {m.getCognome()}", m)

        self.popola_prodotti()
        self.filtra_ordini_attivi("")
        self.prepara_nuovo_ordine()

    # --- RICERCA PRODOTTI ---
    def popola_prodotti(self, filtro=""):
        self.combo_prodotti.clear()
        for p in self.primary_controller.dati.prodotti:
            if filtro.lower() in p.getNomeProdotto().lower():
                self.combo_prodotti.addItem(f"{p.getNomeProdotto()} ({p.getPrezzo():.2f}€) - Qta: {p.getQuantita()}", p)

    def filtra_prodotti(self, testo):
        self.popola_prodotti(testo)

    # --- RICERCA DINAMICA ORDINI ESISTENTI ---
    def popola_ordini_attivi(self, filtro=""):
        self.combo_ordini_trovati.clear()
        ordini = self.primary_controller.dati.ordini
        for ord in ordini:
            id_str = str(ord.getId())
            if filtro == "" or filtro in id_str:
                self.combo_ordini_trovati.addItem(f"Ordine #{ord.getId()} ({ord.getNumeroCoperti()} coperti)", ord)

    def filtra_ordini_attivi(self, testo):
        self.popola_ordini_attivi(testo)

    def prepara_nuovo_ordine(self):
        self.ordine_in_modifica = None
        self.id_corrente = self.genera_id_incrementale()
        self.lbl_id_generato.setText(f"ID Ordine: #{self.id_corrente}")
        self.carrello.clear()
        self.list_riepilogo.clear()

    def aggiungi_al_carrello(self):
        prodotto_obj = self.combo_prodotti.currentData()
        qta = self.spin_qta.value()

        if not prodotto_obj: return

        if qta > prodotto_obj.getQuantita():
            QMessageBox.warning(self, "Attenzione", f"Quantità insufficiente! Disponibili solo {prodotto_obj.getQuantita()} pezzi.")
            return

        po = ProdottoOrdinato(prodotto_obj.getNomeProdotto(), prodotto_obj.getPrezzo(), qta)
        self.carrello.append((po, prodotto_obj))
        self.list_riepilogo.addItem(f"{qta}x {prodotto_obj.getNomeProdotto()} ({prodotto_obj.getPrezzo():.2f}€ cad.)")

    def salva_ordine(self):
        if not self.carrello:
            QMessageBox.warning(self, "Attenzione", "Il carrello è vuoto!")
            return

        operatore = self.combo_operatore.currentData()
        coperti = self.spin_coperti.value()

        if self.ordine_in_modifica:
            self.primary_controller.dati.ordini.remove(self.ordine_in_modifica)

        lista_po = []
        for po, prod_orig in self.carrello:
            lista_po.append(po)
            prod_orig.setQuantita(prod_orig.getQuantita() - po.getQuantita())

        nuovo_ordine = Ordine(self.id_corrente, lista_po, coperti)
        self.primary_controller.dati.ordini.append(nuovo_ordine)

        if operatore and hasattr(operatore, 'aggiungiOrdine'):
            operatore.aggiungiOrdine(nuovo_ordine)

        self.primary_controller.salva_dati()
        QMessageBox.information(self, "Successo", f"Ordine #{self.id_corrente} salvato con successo!")
        self.torna_indietro()

    def carica_ordine_selezionato(self):
        ordine_selezionato = self.combo_ordini_trovati.currentData()
        if ordine_selezionato:
            self.ordine_in_modifica = ordine_selezionato
            self.id_corrente = ordine_selezionato.getId()
            self.lbl_id_generato.setText(f"ID Ordine (In Modifica): #{self.id_corrente}")
            self.spin_coperti.setValue(ordine_selezionato.getNumeroCoperti())
            
            # Ripristina temporaneamente le scorte per consentire la nuova modifica
            for po in ordine_selezionato.getProdottiOrdinati():
                for p in self.primary_controller.dati.prodotti:
                    if p.getNomeProdotto() == po.getNome():
                        p.setQuantita(p.getQuantita() + po.getQuantita())

            self.carrello.clear()
            self.list_riepilogo.clear()
            for po in ordine_selezionato.getProdottiOrdinati():
                for p in self.primary_controller.dati.prodotti:
                    if p.getNomeProdotto() == po.getNome():
                        self.carrello.append((po, p))
                        self.list_riepilogo.addItem(f"{po.getQuantita()}x {po.getNome()} ({po.getPrezzo():.2f}€ cad.)")

            QMessageBox.information(self, "Ordine Caricato", f"Ordine #{self.id_corrente} caricato nel riepilogo.")
        else:
            QMessageBox.warning(self, "Attenzione", "Nessun ordine selezionato dalla lista.")

    def annulla_ordine_selezionato(self):
        ordine_selezionato = self.combo_ordini_trovati.currentData()
        if ordine_selezionato:
            # Ripristina scorte
            for po in ordine_selezionato.getProdottiOrdinati():
                for p in self.primary_controller.dati.prodotti:
                    if p.getNomeProdotto() == po.getNome():
                        p.setQuantita(p.getQuantita() + po.getQuantita())

            self.primary_controller.dati.ordini.remove(ordine_selezionato)
            self.primary_controller.salva_dati()
            QMessageBox.information(self, "Annullato", f"Ordine #{ordine_selezionato.getId()} annullato e scorte ripristinate!")
            self.aggiorna_vista()
        else:
            QMessageBox.warning(self, "Attenzione", "Nessun ordine selezionato dalla lista.")

    def torna_indietro(self):
        from Controller.Dipendenti import DipendentiController
        self.primary_controller.mostra_finestra(DipendentiController, start_maximized=self.isMaximized())
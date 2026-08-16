from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

class PrimaryController:
    """
    Router centrale dell'applicazione: gestisce lo stato delle finestre,
    la navigazione e il passaggio dei dati.
    """
    def __init__(self, gestore_utenti):
        # Mappa per memorizzare i riferimenti: {NomeClasse: IstanzaController}
        self.active_controllers = {}
        self.current_controller = None
        self.gestore_utenti = gestore_utenti

    def mostra_finestra(self, ControllerClass, *args, **kwargs):
        start_maximized = kwargs.pop('start_maximized', False)
        controller_name = ControllerClass.__name__

        # 1. Se la finestra esiste già nel registro, la riutilizziamo
        if controller_name in self.active_controllers:
            new_controller = self.active_controllers[controller_name]
            # Se la schermata ha dati dinamici (es. tabelle), la aggiorniamo
            if hasattr(new_controller, 'aggiorna_vista'):
                new_controller.aggiorna_vista()
        else:
            # 2. Altrimenti crea una nuova istanza passando 'self'
            new_controller = ControllerClass(self, *args, **kwargs)
            self.active_controllers[controller_name] = new_controller

        # 3. Gestisce la visibilità della finestra precedente
        if self.current_controller is not None:
            was_maximized = self.current_controller.isMaximized()
            self.current_controller.hide()
        else:
            was_maximized = False

        # 4. Aggiorna e prepara la nuova finestra
        self.current_controller = new_controller

        # 5. APPLICA LO STATO ALLA NUOVA FINESTRA
        if was_maximized or start_maximized:
            self.current_controller.setWindowState(self.current_controller.windowState() | Qt.WindowMaximized)
            self.current_controller.show()
        else:
            self.current_controller.show()

    # Alias di compatibilità per vecchie chiamate
    mostraFinestra = mostra_finestra

    def chiudi_e_rimuovi(self, controller_instance):
        controller_name = controller_instance.__class__.__name__
        if controller_name in self.active_controllers:
            self.active_controllers.pop(controller_name)
        if self.current_controller == controller_instance:
            self.current_controller = None
        controller_instance.deleteLater()

    def chiusura_sicura(self):
        # Metodo centralizzato per spegnere l'applicazione salvando i dati.
        print("Salvataggio dati in corso...")
        
        # Chiamiamo il logout/salvataggio nel Gestore
        successo = self.gestore_utenti.logout(path="dati.pkl")

        if not successo:
            QMessageBox.critical(
                None, 
                "Errore di Salvataggio", 
                "Non è stato possibile salvare i dati su 'dati.pkl'.\n"
            )            
        # Chiudiamo tutte le finestre attive nel registro
        for controller in list(self.active_controllers.values()):
            controller.close()
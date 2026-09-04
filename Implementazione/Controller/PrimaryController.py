from PyQt5.QtWidgets import QMainWindow

# Import dei gestori ad istanza
from Model.Gestore.GestoreUtenti import GestoreUtenti
from Model.Gestore.GestoreMagazzino import GestoreMagazzino
from Model.Gestore.GestoreOrdini import GestoreOrdini
from Model.Gestore.GestoreConti import GestoreConti

class PrimaryController:
    """
    Router centrale dell'applicazione: gestisce lo stato delle finestre,
    la navigazione e il passaggio dei dati.
    """
    def __init__(self, dati):
        self.dati = dati
        self.active_controllers = {}
        self.current_controller = None
        
        # Inizializzazione centralizzata dei gestori ad istanza
        self.gestore_utenti = GestoreUtenti(self.dati)
        self.gestore_magazzino = GestoreMagazzino(self.dati)
        self.gestore_ordini = GestoreOrdini(self.dati)
        self.gestore_conti = GestoreConti(self.dati, self.gestore_ordini)

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

        # 3. Nascondi la finestra attuale
        if self.current_controller is not None:
            self.current_controller.hide()
            
        self.current_controller = new_controller
        
        # 4. Mostra la nuova finestra mantenendo lo stato (massimizzato o no)
        if start_maximized:
            self.current_controller.showMaximized()
        else:
            self.current_controller.show()

    # Alias di compatibilità
    mostraFinestra = mostra_finestra

    def chiudi_e_rimuovi(self, controller_instance):
        controller_name = controller_instance.__class__.__name__
        if controller_name in self.active_controllers:
            self.active_controllers.pop(controller_name)
            if self.current_controller == controller_instance:
                self.current_controller = None
            controller_instance.deleteLater()
            
    def chiusura_sicura(self):
        print("Salvataggio dati in corso...")
        self.dati.salvaTutto("dati.pkl")

    def salva_dati(self):
        self.dati.salvaTutto("dati.pkl")
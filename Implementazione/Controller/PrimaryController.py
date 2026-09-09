from Model.Gestore.GestoreUtenti import GestoreUtenti
from Model.Gestore.GestoreConti import GestoreConti
from Model.Gestore.GestoreMagazzino import GestoreMagazzino
from Model.Gestore.GestoreOrdini import GestoreOrdini

class PrimaryController:
    """
    Router centrale dell'applicazione: gestisce lo stato delle finestre,
    la navigazione e la persistenza dei dati.
    """
    def __init__(self, dati):
        self.dati = dati
        self.active_controllers = {}
        self.current_controller = None
        
        # Istanziamento unificato di tutti i gestori
        self.gestore_utenti = GestoreUtenti(dati)
        self.gestore_conti = GestoreConti(dati)
        self.gestore_magazzino = GestoreMagazzino(dati)
        self.gestore_ordini = GestoreOrdini(dati)

    def mostra_finestra(self, ControllerClass, *args, **kwargs):
        start_maximized = kwargs.pop('start_maximized', False)
        controller_name = ControllerClass.__name__
        
        if controller_name in self.active_controllers:
            new_controller = self.active_controllers[controller_name]
            if hasattr(new_controller, 'aggiorna_vista'):
                new_controller.aggiorna_vista()
        else:
            new_controller = ControllerClass(self, *args, **kwargs)
            self.active_controllers[controller_name] = new_controller

        if self.current_controller is not None:
            self.current_controller.hide()
            
        self.current_controller = new_controller
        
        if start_maximized:
            self.current_controller.showMaximized()
        else:
            self.current_controller.show()

    def salva_dati(self):
        self.dati.salvaTutto()

    def chiudi_e_rimuovi(self, controller_instance):
        controller_name = controller_instance.__class__.__name__
        if controller_name in self.active_controllers:
            self.active_controllers.pop(controller_name)
            if self.current_controller == controller_instance:
                self.current_controller = None
            controller_instance.deleteLater()
            
    def chiusura_sicura(self):
        print("Salvataggio dati in corso...")
        self.dati.salvaTutto()